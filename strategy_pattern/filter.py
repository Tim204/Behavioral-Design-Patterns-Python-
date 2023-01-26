from abc import ABC, abstractmethod


class Filter(ABC):
    @abstractmethod
    def filter(self, file_name):
        pass


class BlackAndWhiteFilter(Filter):
    def filter(self, file_name):
        print(f"Applying B&W to {file_name}")
        pass


class HighContrast(Filter):
    def filter(self, file_name):
        print(f"Applying high contrast to {file_name}")

