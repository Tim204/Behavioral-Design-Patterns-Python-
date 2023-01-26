from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class AddCustomerCommand(Command):

    def __init__(self, service):
        self.service = service

    def execute(self):
        self.service.add_customer()


class CompositeCommands(Command):
    commands = []

    def add_commands(self, command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()


class ResizeCommand(Command):

    def execute(self):
        print("Resizing")


class BlackAndWhiteCommand(Command):

    def execute(self):
        print("Black and white")


class CustomerService:
    def add_customer(self):
        print("Adding customer")


class Button:
    _label: str

    def __init__(self, command):
        self.command = command

    def click(self):
        self.command.execute()


service = CustomerService()


# Dealing with Multiple commands
cmds = CompositeCommands()
cmds.add_commands(ResizeCommand())
cmds.add_commands(BlackAndWhiteCommand())

# Dealing with a single command
cmd = AddCustomerCommand(service)

but = Button(cmds)
but.click()
