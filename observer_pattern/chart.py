from observer_pattern.data_source import DataSource
from observer_pattern.observer_interface import Observer


class Chart(Observer):
    def __init__(self):
        self._data_source = DataSource()

    def update(self):
        print(f"Chart got updated {self._data_source.get_value()}")
