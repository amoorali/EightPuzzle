from tools.puzzle import Puzzle

def index(item, list):
    try:
        return list.index(item)
    except:
        return -1

class AStarSolution:
    def __init__(self, matrix):
        # puzzle object
        self.puzzle_object = Puzzle(matrix)
        self.path = []

    def solve_misplaced_tiles(self):
        return self._calc_misplaced_tiles(self.puzzle_object)

    def solve_manhattan(self):
        """Solve the puzzle with A* algorithm"""
        def is_solved(puzzle):
            return puzzle.matrix == puzzle.goal_state()

        openl = [self.puzzle_object]
        closel = []
        move_count = 0

        while openl:
            puz = openl.pop(0)
            move_count += 1
            if is_solved(puz):
                return self._generate_path(puz), move_count

            successors = puz._generate_moves()
            openl_idx = closel_idx = -1

            for move in successors:
                openl_idx = index(move, openl)
                closel_idx = index(move, closel_idx)
                hval = self._calc_manhattan(move)
                fval = hval + move._depth

                # if it's not visited, add to the open list
                if openl_idx == -1 and closel_idx == -1:
                    move._h_value = hval
                    openl.append(move)

                # if it's in open list, check if it has smaller fval
                elif openl_idx != -1:
                    copy = openl[openl_idx]
                    if fval < copy._h_value + copy._depth:
                        copy._parent = move._parent
                        copy._h_value = hval
                        copy._depth = move._depth
                
                # if it's in close list, check if it has smaller fval, if so add it to open list
                elif closel_idx != -1:
                    copy = closel[closel_idx]
                    if fval < copy._h_value + copy._depth:
                        move._h_value = hval
                        closel.remove(copy)
                        openl.append(move)
            
            closel.append(puz)
            openl = sorted(openl, key=lambda p: p._h_value + p._depth)
        
        return [], 0

    def _calc_manhattan(self, puzzle):
        points = 0
        for row in range(3):
            for col in range(3):
                val = puzzle.matrix[row][col]
                goal_row, goal_col = int(val / 3), (val % 3)
                points += abs(row - goal_row) + abs(col - goal_col)
        
        return points

    def _calc_misplaced_tiles(self, puzzle):
        points = 0
        for row in range(3):
            for col in range(3):
                goal_val, curr_val = puzzle.goal_state()[row][col], puzzle.matrix[row][col]
                if goal_val != curr_val:
                    points += 1
        return points

    def _generate_path(self, node):
        if node is None:
            return None

        self.path.append(node)
        self._generate_path(node._parent)
        return self.path