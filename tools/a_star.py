import puzzle

class AStarSolution:
    def __init__(self):
        # heuristic value
        self._h_value = 0
        # state
        self.matrix = puzzle.goal_state()
        # depth of the node
        self._depth = 0
        # parent
        self._parent = None

    def solve(self):
        print(self.initial_state)
        print('*' * 5)
        print(self.goal_state)
        print(self._calc_manhattan(self.initial_state))

    def _calc_manhattan(self, state):
        points = 0
        for row in range(3):
            for col in range(3):
                item = state[row][col]
                goal_row, goal_col = int(item / 3) - 1, (item % 3) - 1
                if item == 0:
                    goal_row, goal_col = 2, 2
                points += abs(row - goal_row) + abs(col - goal_col)
        
        return points

    def _valid_moves(self):
        pass

    def _generate_moves(self):
        pass