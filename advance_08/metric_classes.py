import time
from types import TracebackType
from typing import Union, Optional, Type, Dict, List
from typing_extensions import Literal

Scalar = Union[int, float]


class BaseMetric(object):
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def get_value(self):
        pass

    def add(self, value):
        pass

    def clear(self):
        pass


class MetricTimer(BaseMetric):
    def __init__(self, name):
        super().__init__(name)
        self.cum_time = 0
        self.start_time = 0

    def add(self, value: float) -> None:
        self.cum_time += value

    def clear(self) -> None:
        self.cum_time = 0

    def get_value(self) -> float:
        return self.cum_time

    def __enter__(self) -> None:
        self.start_time = time.time()

    def __exit__(self,
                 type: Optional[Type[BaseException]],
                 value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> Literal[False]:
        result_time = time.time() - self.start_time

        self.add(result_time)
        self.start_time = 0
        return False


class MetricAvg(BaseMetric):
    def __init__(self, name: str):
        super().__init__(name)
        self.avg_data: List[Scalar] = [0.0, 0]

    def add(self, value: Scalar) -> None:
        val, nums = self.avg_data
        sum_ = val * nums
        avg = (sum_ + value) / (nums + 1)
        self.avg_data = [avg, nums + 1]

    def clear(self) -> None:
        self.avg_data = [0, 0]

    def get_value(self) -> Scalar:
        return self.avg_data[0]


class MetricCount(BaseMetric):
    def __init__(self, name: str):
        super().__init__(name)
        self.counter = 0

    def add(self, *args) -> None:
        self.counter += 1

    def clear(self) -> None:
        self.counter = 0

    def get_value(self) -> int:
        return self.counter


class Stats:

    timer_buff: Dict[str, MetricTimer] = {}
    avg_buff: Dict[str, MetricAvg] = {}
    cnt_buff: Dict[str, MetricCount] = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Stats, cls).__new__(cls)
        return cls.instance

    def timer(self, name: str) -> MetricTimer:
        if name in self.timer_buff:
            return self.timer_buff[name]
        self.timer_buff[name] = MetricTimer(name)
        return self.timer_buff[name]

    def avg(self, name: str) -> MetricAvg:
        if name in self.avg_buff:
            return self.avg_buff[name]
        self.avg_buff[name] = MetricAvg(name)
        return self.avg_buff[name]

    def count(self, name: str) -> MetricCount:
        if name in self.cnt_buff:
            return self.cnt_buff[name]
        self.cnt_buff[name] = MetricCount(name)
        return self.cnt_buff[name]

    def collect(self) -> dict:
        result = {}
        for (stat_buff, method_name) in zip([self.timer_buff,
                                             self.avg_buff,
                                             self.cnt_buff],
                                            ["timer", "avg", "count"]):
            assert isinstance(stat_buff, dict)  # for mypy purposes
            for name, class_metric in stat_buff.items():
                value = class_metric.get_value()
                if value == 0:
                    continue
                result[f"{name}.{method_name}"] = value
                class_metric.clear()
        return result


if __name__ == "__main__":

    st = Stats()

    def calc() -> float:
        time.sleep(0.5)
        return 5

    with st.timer("calc"):  # 0.1
        RESULT = calc()  # 3

    st.count("calc").add()
    st.count("calc").add()

    t1 = time.time()
    TEST_RES = calc()  # 7
    t2 = time.time()
    st.timer("calc").add(t2 - t1)  # 0.3
    st.count("calc").add()
    st.avg("calc").add(TEST_RES)

    st.count("http_get_data").add()
    st.avg("http_get_data").add(0.7)

    st.count("no_used")  # не попадет в результат collect

    metrics = st.collect()
    print(metrics)

    metrics = st.collect()
    print(metrics)
    assert not metrics
