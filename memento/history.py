

class History:
    states = []

    def push(self, state):
        self.states.append(state)

    def pop(self):
        last_state = self.states.pop()
        return last_state

