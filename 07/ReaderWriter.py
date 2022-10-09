from abc import ABC, abstractmethod
import json
import csv
# насколько я понял, нужно было сделать абстрактный базовый класс
# а потом в наследниках переопределить методы, но этого вроде не было на 7 лекции
# поэтому я опирался на этот источник https://docs-python.ru/tutorial/klassy-jazyke-python/abstraktnye-klassy/
class BaseReader(ABC):
    @abstractmethod
    def read(self):
        pass

class BaseWriter(ABC):
    @abstractmethod
    def dump():
        pass

class TxtReader(BaseReader):
    def read(self, fileobj):
        with open(fileobj, 'r') as f:
            data = f.read().splitlines()
        return data

class TxtWriter(BaseWriter):
    def dump(self, fileobj, data):
        with open(fileobj, 'a') as f:
            f.writelines(data)

class CsvReader(BaseReader):
    def read(self, fileobj):
        data = []
        with open(fileobj, 'r') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                data.append(','.join([elem for elem in row]))
        return data
    
class CsvWriter(BaseWriter):
    def dump(self, fileobj, data):
        with open(fileobj, 'a') as f:
            csvwriter = csv.writer(f, delimiter = ',')
            csvwriter.writerow(data)

class JsonReader(BaseReader):
    def read(self, fileobj):
        with open(fileobj, 'r') as f:
            return json.load(f)

class JsonWriter(BaseWriter):
    def dump(self, fileobj, data):
        with open(fileobj, 'a') as f:
            json.dump(data, f)

def read_data(fileobj, reader: BaseReader):
    return reader.read(fileobj)

def dump_data(data, fileobj, writer: BaseWriter):
    writer.dump(fileobj, data)

if __name__ == '__main__':
    print(read_data('tt.txt', reader = TxtReader()))
    dump_data(['hello', '\nhow are', '\n u'], 'test_file.txt', writer = TxtWriter())
    print(read_data('tt2.csv', reader = CsvReader()))
    dump_data(['1,2,3,4', '5,6,7,8'], 'test_file_csv.csv', writer = CsvWriter())
    print(read_data('test_json.json', reader = JsonReader()))
    dump_data({"x": "1"}, 'write_json.json', writer=JsonWriter())


