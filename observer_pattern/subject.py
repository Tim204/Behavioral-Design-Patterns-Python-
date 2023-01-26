from abc import ABC, abstractmethod


class Subject(ABC):

    _observers = []

    def attach_observer(self, observer):
        self._observers.append(observer)

    def detach_observer(self, observer):
        self._observers.remove(observer)

    def notify_observer(self):
        for observer in self._observers:
            observer.update()



