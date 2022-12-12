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
        row, col = self.puzzle_object.find(0)
        dirs = [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]
        valid_dirs = []

        for dir in dirs:
            row, col = dirs
            if 0 <= row < 3 and 0 <= col < 3:
                valid_dirs.append(dir)
        
        return valid_dirs

    def _generate_moves(self):
        pass