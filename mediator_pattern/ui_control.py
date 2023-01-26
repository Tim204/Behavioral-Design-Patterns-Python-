from abc import ABC, abstractmethod


class Observer:
    def update(self):
        pass


class UIControl(ABC):
    _observers: list

    def attach_observer(self, observer):
        self._observers.append(observer)

    def __notify_observers(self):
        for observer in self._observers:
            observer.update()


class ListBox(UIControl):

    _selection: str

    def get_selection(self):
        return self._selection

    def set_selection(self, selection):
        self._selection = selection
        self.__notify_observers()


class TextBox(UIControl):
    _content: str

    def get_content(self):
        return self._content

    def set_content(self, content):
        self._content = content
        self.__notify_observers()


class Button(UIControl):
    _is_enabled: bool

    def is_enabled(self):
        return self._is_enabled

    def set_enable(self, enable):
        self._is_enabled = enable
        self.__notify_observers()


class ArticleDialogueBox:

    def __init__(self):
        self.list_box = ListBox()
        self.text_box = TextBox()
        self.save_button = Button()

    def changed(self, ui_control):
        if ui_control == self.list_box:
            self.text_box.set_content(self.list_box.set_selection(self))
            
