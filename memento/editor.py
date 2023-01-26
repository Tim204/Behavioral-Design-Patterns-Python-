from editor_state import EditorSate


class Editor(EditorSate):

    def create_state(self):
        return EditorSate(self.content)

    def restore(self, state):
        self.content = state.get_content()

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content
