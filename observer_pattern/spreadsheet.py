from observer_pattern.data_source import DataSource
from observer_pattern.observer_interface import Observer


class SpreadSheet(Observer):

    def __init__(self, data_source):
        self._data_source = data_source

    def update(self):
        print(f"Spreadsheet got notified: {self._data_source.get_value()}")

