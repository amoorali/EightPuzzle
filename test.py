from tools.a_star import AStarSolution
import time
start_time = time.time()

def create_state(num):
    result = [[], [], []]
    for i in range(3):
        result[i] = num[i * 3:(i * 3) + 3]
    return result
        

state = [[8, 0, 6], [5, 4, 7], [2, 3, 1]]
# state = create_state([1, 0, 2, 5, 3, 4, 6, 7, 8])
# state = create_state([3, 1, 2, 4, 0, 5, 6, 7, 8])

p = AStarSolution(state)
# print(p.solve_misplaced_tiles())
path, moves = p.solve_manhattan()
path = reversed(path)
print(moves)
for p in path:
    print("*" * 10)
    print(p)

print("--- %s seconds ---" % (time.time() - start_time))
