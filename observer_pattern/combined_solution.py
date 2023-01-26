from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class Subject(ABC):

    _observers = []

    def attach_observer(self, observer):
        self._observers.append(observer)

    def detach_observer(self, observer):
        self._observers.remove(observer)

    def notify_observer(self):
        for observer in self._observers:
            observer.update()


class DataSource(Subject):
    _value: int

    def __init__(self):
        self._value = self.get_value()

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
        self.notify_observer()


class SpreadSheet(Observer):

    def __init__(self, data_source):
        self._data_source = data_source

    def update(self):
        print(f"Spreadsheet got notified: {self._data_source.get_value()}")


class Chart(Observer):
    def __init__(self, data_source):
        self._data_source = data_source

    def update(self):
        print(f"Chart got updated {self._data_source.get_value()}")


data_source = DataSource()
sheet1 = SpreadSheet(data_source)
sheet2 = SpreadSheet(data_source)
chart = Chart(data_source)

data_source.attach_observer(sheet1)
data_source.attach_observer(sheet2)
data_source.attach_observer(chart)

data_source.get_value()
