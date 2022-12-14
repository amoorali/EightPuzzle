from tools.a_star import AStarSolution
import time


def create_state(num):
    result = [[], [], []]
    for i in range(3):
        result[i] = num[i * 3:(i * 3) + 3]
    return result
        
def main():
    test_cases = [create_state([8, 0, 6, 5, 4, 7, 2, 3, 1]),
                  create_state([1, 0, 2, 5, 3, 4, 6, 7, 8]),
                  create_state([3, 1, 2, 4, 0, 5, 6, 7, 8]),
                  create_state([5, 4, 3, 2, 1, 0, 6, 7 ,8])]
    test_cases = [AStarSolution(mat) for mat in test_cases]
    print('Test Cases:')
    [print(f'{i + 1}.\n{test_case.puzzle_object}' + '*' * 5) for i, test_case in enumerate(test_cases)]
    p = test_cases[int(input(f'Choose a test case: ')) - 1]

    funcs = [p.solve_manhattan, p.solve_misplaced_tiles]

    msg = """Choose an algorithm:
    1. A* Manhattan Distance
    2. A* Misplaced Tiles
    3. BiDirectional\n"""
    path, moves = funcs[int(input(msg)) - 1]()

    path_len = len(path)
    path = reversed(path)
    for p in path:
        print("*" * 10)
        print(p)
    
    print(f"Created Nodes: {moves}")
    print(f"Solution steps: {path_len}")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))