from abc import ABC,abstractmethod


class HtmlNode(ABC):
    @abstractmethod
    def execute(self, operation):
        pass


class Operation(ABC):
    @abstractmethod
    def apply(self, operation):
        pass


class PlainTextOperation(Operation):

    def apply(self, operation):
        print(f"text-{operation}")


class HighlightOperation(Operation):

    def apply(self, operation):
        print(f"highlight-{operation}")


class HeadingNode(HtmlNode):
    def execute(self, operation):
        operation.apply(self)

    def __str__(self):
        return "heading"


class AnchorNode(HtmlNode):
    def execute(self, operation):
        operation.apply(self)

    def __str__(self):
        return "anchor"


class HtmlDocument:
    _nodes = []

    def add(self, node):
        self._nodes.append(node)

    def execute(self, operation):
        for node in self._nodes:
            node.execute(operation)


document = HtmlDocument()

document.add(HeadingNode())
document.add(AnchorNode())

document.execute(HighlightOperation())
document.execute(PlainTextOperation())

