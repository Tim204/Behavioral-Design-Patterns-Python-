from abc import ABC, abstractmethod
from audit import AuditTrail


class Task(ABC):
    def __init__(self):
        self._audit_trail = AuditTrail()

    def execute(self):
        self._audit_trail.record()
        self._do_execute()

    @abstractmethod
    def _do_execute(self):
        pass


class TransferMoney(Task):
    def _do_execute(self):
        print("Transfer Money")


class GenerateReportTask(Task):
    def _do_execute(self):
        print("Generating Report")


def bank(abstract_class):
    abstract_class.execute()


bank(TransferMoney())
bank(GenerateReportTask())





