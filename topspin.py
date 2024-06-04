
class TopSpinState:

    def __init__(self, state, k=4):
        self.state = state
        self.k = k
        self.n = len(state)
        self.goal = sorted(state)

    def is_goal(self):
        if self.state == self.goal:
            return True
        return False

    def get_state_as_list(self):
        return self.state

    def get_neighbors(self):
        neighbors = []

        # flip action
        to_flip = self.state[:self.k]
        to_flip.reverse()
        flip_state = to_flip + self.state[self.k:]
        neighbors.append(flip_state)

        # clockwise action
        clock_state = self.state[self.n - 1] + self.state[: self.n - 1]
        neighbors.append(clock_state)

        # counterclock action
        counterclock_state = self.state[1:] + self.state[0]
        neighbors.append(counterclock_state)

        return neighbors


state = [1,2,3,4]
a = TopSpinState(state)