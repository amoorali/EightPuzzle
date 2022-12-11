state = [[1, 2, 3], [4, 7, 8], [5, 0, 6]]
points = 0
print(state[0])
print(state[1])
print(state[2])
for row, nums in enumerate(state):
    for col in range(3):
        state_row, state_col = int(row / 3), col % 3
        goal_row, goal_col = row, col
        points += abs(state_row - goal_row) + abs(state_col - goal_col)

print(points)