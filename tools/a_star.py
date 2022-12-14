from tools.puzzle import Puzzle

class AStarSolution:
    def __init__(self, matrix):
        # puzzle object
        self.puzzle_object = Puzzle(matrix)

    def solve_misplaced_tiles(self):
        pass

    def solve_manhattan(self):
        """Solve the puzzle with A* algorithm"""
        def is_solved(self):
            return self.matrix == Puzzle.goal_state()

        open = [self.puzzle_object]
        close = []
        c = 10
        while open:
            puz = open.pop()
            print(puz.matrix)
            movelist = puz._generate_moves()
            print(movelist[0])
            print()
            # p = movelist.pop()
            # open.append(p)
            # print(p)
            # print()
            # c -= 1
            # if c == 0:
            #     return


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
        