from tools.puzzle import *
from tools.funcs import index


class BiDirectional:
    def __init__(self, matrix) -> None:
        self.initial_state = Puzzle(matrix)
        self.goal_state = Puzzle(goal_state())
        self.finished = False
    
    def solve(self):
        top_openl = [self.initial_state]
        bot_openl = [self.goal_state]
            
        moves = 0

        def expand(side_list, opposite_list):
            puz = side_list.pop(0)
            successors = puz._generate_moves()
            sidel_idx = oppositel_idx = -1

            for move in successors:
                sidel_idx = index(move, side_list)
                oppositel_idx = index(move, opposite_list)

                # if it's not visited, add to the open list
                if sidel_idx == -1 and oppositel_idx != -1:
                    self.finished = True
                    return self._generate_path(move, opposite_list[oppositel_idx])

                elif sidel_idx == -1:
                    side_list.append(move)

            return None


        while top_openl and bot_openl:
            moves += 1
            temp = expand(top_openl, bot_openl)
            if self.finished:
                return temp, moves
            temp = expand(bot_openl, top_openl)
            if self.finished:
                return temp, moves
        
        return [], 0, 0

    def _generate_path(self, top_puzzle, bot_puzzle):
        result = []
        def bot_path(puzzle):
            if puzzle is None:
                return None
            
            result.append(puzzle)
            bot_path(puzzle._parent)

        def top_path(puzzle):
            if puzzle is None:
                return None
            
            result.append(puzzle)
            top_path(puzzle._parent)

        bot_path(bot_puzzle) 
        result.reverse()
        top_path(top_puzzle)

        return result