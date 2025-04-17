import pygame
import sys
import SudokuGenerator

pygame.init()

# constants

width = 450
height = 450
grid_size = 9
total_cells = grid_size * grid_size
cell_size = width / grid_size

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FONT = pygame.font.SysFont(None, 40)

solution = SudokuGenerator.solution
board = SudokuGenerator.puzzle

screen = pygame.display.set_mode((width, height))

pygame.mixer.music.load("Python/fun/Games/Pygame/Sudoku/Never gonna give you up.mp3")
pygame.mixer.music.play(3)

# Functions

# draw the grid
def draw_grid_and_nums():
    for i in range(grid_size):
        if i % 3 == 0 and i != 0:
            pygame.draw.line(screen, BLACK, (0, i * cell_size), (width, i * cell_size), 3)
            pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, height), 3)
        else:
            pygame.draw.line(screen, BLACK, (0, i * cell_size), (width, i * cell_size))
            pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, height))

    for i in range(grid_size):
        for j in range(grid_size):
            if board[i][j] != 0:
                number = FONT.render(str(board[i][j]), True, BLACK)
                screen.blit(number, (j * cell_size + grid_size / 2 + number.get_width() / 2, i * cell_size + grid_size / 2 + number.get_height() / 3))

# color cells
def color_cell(cell, color):
    if cell:
        if cell != None:
                pygame.draw.rect(screen, color, (cell[1]*cell_size, cell[0]*cell_size, cell_size, cell_size), 3)

# draw the numbers
def draw_numbers():
    for i in range(grid_size):
        for j in range(grid_size):
            if board[i][j] != 0:
                number = FONT.render(str(board[i][j]), True, BLACK)
                screen.blit(number, (j * cell_size + grid_size / 2 + number.get_width() / 2, i * cell_size + grid_size / 2 + number.get_height() / 3))

# make cells when clicked
def handle_click(mouse_pos):
    row = int(mouse_pos[1] / cell_size)
    column = int(mouse_pos[0] / cell_size)
    if board[row][column] == 0:
        return (row, column)
    return None

    # replace cells
def replace_cell(cell, input):
    board[cell[0]][cell[1]] = input

def check_answer():
    correct_answers = 0
    for i in range(len(board)):
        for n in range(len(board[i])):
            if board[i][n] == solution[i][n]:
                correct_answers += 1
                color_cell((i, n), GREEN)
            else:
                color_cell((i, n), RED)  

    if correct_answers == total_cells:
        print("You got it right, HURRAY!")
    else:
        print("Some answers are incorrect, keep trying!")

    # main function
def main():
    selected_cell = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selected_cell = handle_click(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    if selected_cell != None:
                        if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
                            selected_cell = replace_cell(selected_cell, event.key-48)
                    if event.key == 13: #enter
                        check_answer()
                        running = False
                        draw_grid_and_nums()
                        pygame.display.flip()
                        
                    if event.key == 8: #delete
                        print("delete")

        if running == True:
            screen.fill(WHITE)
            draw_grid_and_nums()
            color_cell(selected_cell, BLUE)
            pygame.display.flip()

if __name__ == "__main__":
    main()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
