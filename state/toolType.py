from abc import ABC, abstractmethod


class ToolType:
    SELECTION, BRUSH, ERASER = range(3)


class Tool(ABC):
    @abstractmethod
    def mouse_down(self):
        pass

    @abstractmethod
    def mouse_up(self):
        pass


class SelectionTool(Tool):

    def mouse_down(self):
        print("Selection icon")

    def mouse_up(self):
        print("Drawing a dashed rectangle")


class BrushTool(Tool):
    def mouse_down(self):
        print("Brush Icon")

    def mouse_up(self):
        print("Draw a line")




