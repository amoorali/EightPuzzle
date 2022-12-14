from tools.a_star import AStarSolution


state = [[8, 0, 6], [5, 4, 7], [2, 3, 1]]
# state = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
p = AStarSolution(state)
path, moves = p.solve_manhattan()
path = reversed(path)
print(moves)
for p in path:
    print("*" * 10)
    print(p)
    print