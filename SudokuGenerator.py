from sudokuLib import Sudoku

puzzle = Sudoku(3).difficulty(0.5)
#puzzle.show()

solution = puzzle.solve()
#solution.show()

solution = solution.board
puzzle = puzzle.board

for i in range(len(puzzle)):
    for n in range(len(puzzle[i])):
        if puzzle[i][n] == None:
            puzzle[i][n] = 0

for i in range(len(solution)):
    for n in range(len(solution[i])):
        if solution[i][n] == None:
            solution[i][n] = 0
