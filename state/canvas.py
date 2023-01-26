from state.toolType import BrushTool, SelectionTool


class Canvas:

    def __init__(self, current_tool):
        self._current_tool = current_tool

    def mouse_up(self):
        self._current_tool.mouse_up()

    def mouse_down(self):
        self._current_tool.mouse_down()


canvas = Canvas(SelectionTool())

canvas.mouse_down()
canvas.mouse_up()




