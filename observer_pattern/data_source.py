from observer_pattern.chart import Chart
from observer_pattern.spreadsheet import SpreadSheet
from observer_pattern.subject import Subject


class DataSource(Subject):
    _value: int

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
        self.notify_observer()


data_source = DataSource()
sheet1 = SpreadSheet()
sheet2 = SpreadSheet()
chart = Chart()

data_source.attach_observer(sheet1)
data_source.attach_observer(sheet2)
data_source.attach_observer(chart)

data_source.set_value(1)
