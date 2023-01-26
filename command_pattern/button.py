from command import Command
from costomer_app import CustomerService


class Button:
    _label: str

    def __init__(self):
        self.command = command

    def click(self):
        self.command.execute()

    def get_label(self):
        return self._label

    def set_label(self, label):
        self._label = label


service = Button(Command)