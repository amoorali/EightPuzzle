from random import sample

class Puzzle:
    def __init__(self):
        pass

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        
        return self.matrix == other.matrix
    
    def __str__(self, input: list[list]=None) -> str:
        if not input:
            input = self._nums
        txt = ''
        for i in range(3):
            for j in range(3):
                txt += f'{input[i][j]} '
            txt += '\n'
        
        return txt.strip()

    def toString(self, input) -> str:
        return self.__str__(input)

    def getNums(self) -> list[list]:
        return self._nums

    def _peek(self, row, col):
        """Return the value at the specified row, col"""
        return self.matrix[row][col]

    def _poke(self, row, col, value):
        """Replace the value at the specified row, col"""
        self.matrix[row][col] = value

    def _swap(self, pos1, pos2):
        """Swap the values at the specified positions"""
        temp = self.peek(*pos1)
        self.poke(*pos1, value=self.peek(*pos2))
        self.poke(*pos2, value=temp)

    def _clone(self):
        """Return a clone object with same matrix values"""
        matrix = Puzzle()
        for i in range(3):
            matrix[i] = self.matrix[i][:]
        return matrix

    def goal_state(self) -> list[list]:
        return [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]]
        
    def create_random(self):
        temp = sample(range(9), 9)
        return [[temp.pop() for _ in range(3)] for _ in range(3)]