

class GenerateReportTask:
    def __init__(self, audit_trail):
        self._audit_trail = audit_trail

    def execute(self):
        self._audit_trail.record()
        print("Generate report")

