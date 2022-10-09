from abc import ABC, abstractmethod
import json
import csv
import io
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
        return fileobj.read().splitlines()

class TxtWriter(BaseWriter):
    def dump(self, fileobj, data):
        if isinstance(data, list):
            fileobj.write('\n'.join(data))
        else:
            fileobj.write(data)

class CsvReader(BaseReader):
    def read(self, fileobj):
        data = []
        csvreader = csv.reader(fileobj, delimiter = ',')
        for row in csvreader:
            data.append(','.join(row))
        return data
    
class CsvWriter(BaseWriter):
    def dump(self, fileobj, data):
        csvwriter = csv.writer(fileobj)
        csvwriter.writerow(data)

class JsonReader(BaseReader):
    def read(self, fileobj):
        return json.loads(fileobj)

class JsonWriter(BaseWriter):
    def dump(self, fileobj, data):
        json.dump(data, fileobj)

def read_data(fileobj, reader: BaseReader):
    return reader.read(fileobj)

def dump_data(data, fileobj, writer: BaseWriter):
    writer.dump(fileobj, data)

    
