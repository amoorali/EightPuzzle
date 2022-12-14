from random import sample

class Puzzle:
    def __init__(self, state=None, parent=None, hval=0, depth=0):
        # heuristic value
        self._h_value = hval
        # state
        self.matrix = state
        # depth of the node
        self._depth = depth
        # parent
        self._parent = parent

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        
        return self.matrix == other.matrix
    
    def __str__(self, input: list[list]=None) -> str:
        if not input:
            input = self.matrix
        txt = ''
        for i in range(3):
            for j in range(3):
                txt += f'{input[i][j]} '
            txt += '\n'
        
        txt = txt.replace('0', ' ')
        return txt

    def toString(self, input) -> str:
        return self.__str__(input)

    def _peek(self, row, col):
        """Return the value at the specified row, col"""
        return self.matrix[row][col]

    def _poke(self, row, col, value):
        """Replace the value at the specified row, col"""
        self.matrix[row][col] = value

    def _swap(self, pos1, pos2):
        """Swap the values at the specified positions"""
        # print(f"before swap:\n{self}")
        temp = self._peek(*pos1)
        self._poke(*pos1, value=self._peek(*pos2))
        self._poke(*pos2, value=temp)
        # print(f"after swap:\n{self}")

    def _clone(self):
        """Return a clone object with same matrix values"""
        temp = Puzzle([[], [], []])
        for i in range(3):
            temp.matrix[i] = self.matrix[i][:]
        return temp

    def swap_and_clone(self, coordinates):
        """Clone a new puzzle obj and swap specified values in the clone"""
        temp = self._clone()
        temp._swap(self.find(0), coordinates)
        temp._parent = self
        temp._depth = self._depth + 1
        return temp

    def find(self, value):
        """Return the row, col of the specified value in the matrix"""
        if value < 0 or value > 8:
            return Exception('Value must be between 0 and 8')

        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == value:
                    return (i, j)

    
    def _valid_moves(self):
        row, col = self.find(0)
        dirs = [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]
        valid_dirs = []

        for dir in dirs:
            i, j = dir
            if 0 <= i < 3 and 0 <= j < 3:
                valid_dirs.append(dir)
        
        return valid_dirs

    def _generate_moves(self):
        movelist = []
        dirs = self._valid_moves()
        for dir in dirs:
            movelist.append(self.swap_and_clone(dir))
        
        return movelist
            

    def goal_state(self) -> list[list]:
        return [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]]
        
    def create_random(self):
        temp = sample(range(9), 9)
        return [[temp.pop() for _ in range(3)] for _ in range(3)]