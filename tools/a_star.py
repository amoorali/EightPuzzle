import puzzle

class AStarSolution:
    def __init__(self, matrix):
        # puzzle object
        self.puzzle_object = puzzle.Puzzle
        # heuristic value
        self._h_value = 0
        # state
        self.matrix = matrix
        # depth of the node
        self._depth = 0
        # parent
        self._parent = None

    def solve(self):
        print(self._calc_manhattan(self.matrix))

    def _calc_manhattan(self):
        points = 0
        for row in range(3):
            for col in range(3):
                item = self.matrix[row][col]
                goal_row, goal_col = int(item / 3) - 1, (item % 3) - 1
                if item == 0:
                    goal_row, goal_col = 2, 2
                points += abs(row - goal_row) + abs(col - goal_col)
        
        return points

    def _valid_moves(self):
        puzzle.find

    def _generate_moves(self):
        pass