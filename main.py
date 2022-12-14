from tools.a_star import AStarSolution
from tools.bidirectional import BiDirectional
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
                  create_state([5, 4, 3, 2, 1, 0, 6, 7, 8])]

    def choose_testcase(test_cases):
        print('Test Cases:')
        [print(f'{i + 1}.\n{test_case.initial_state}' + '*' * 5) for i, test_case in enumerate(test_cases)]
        return test_cases[int(input(f'Choose a test case: ')) - 1]

    msg = """Choose an algorithm:
    1. A* Manhattan Distance
    2. A* Misplaced Tiles
    3. BiDirectional\n"""

    func = int(input(msg)) - 1
    
    if func == 2:
        p = choose_testcase([BiDirectional(mat) for mat in test_cases])
        path, moves = p.solve()
        for p in path:
            print("*" * 10)
            print(p)
        print(f"Created Nodes: {moves}")
        print(f"Solution steps: {len(path)}")

    else:
        p = choose_testcase([AStarSolution(mat) for mat in test_cases])
        funcs = [p.solve_manhattan, p.solve_misplaced_tiles]    
        path, moves = funcs[func]()
        path.reverse()
        for p in path:
            print("*" * 10)
            print(p)
        
        print(f"Created Nodes: {moves}")
        print(f"Solution steps: {len(path)}")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))