from random import sample

class Puzzle:
    def __init__(self):
        temp = sample(range(9), 9)
        self._nums = [[temp.pop() for _ in range(3)] for _ in range(3)]
    
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

    def goal_state(self) -> list[list]:
        return [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]]