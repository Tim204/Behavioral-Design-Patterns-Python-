from editor import Editor
from history import History

class Undo:

    def un(self):
        content1 = "a"
        content2 = "b"
        self.editor = Editor()
        editor = Editor(content1)
        history = History()

        editor.set_content(content1)
        history.push(editor.create_state())

        editor.set_content(content2)
        history.push(editor.create_state())

        editor.restore(history.pop())

        print(editor.content)


undo = Undo()
undo.un()


