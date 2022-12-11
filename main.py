from tools import puzzle, a_star, bidirectional


def main():
    rand_puzzle = puzzle.Puzzle()
    a_sta_solution = a_star.AStarSolution(rand_puzzle.getNums(),\
                                          rand_puzzle.getNums(),\
                                          rand_puzzle.goal_state())\
                                          .solve()



if __name__ == '__main__':
    main()
