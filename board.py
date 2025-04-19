# board class
# Nicholas St. Onge
import pygame, sys

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.box_w = width / 9
        self.box_h = height / 9
        self.selected_cell = None

    def draw(self):
        for i in range(1, 3):
            pygame.draw.line(self.screen, "black",(0, (self.height / 3) * i),
                             (self.width, (self.height / 3) * i), 3)
            pygame.draw.line(self.screen, "black",((self.width / 3) * i, 0),
                             ((self.width / 3) * i, self.height), 3)
        for i in range(1, 9):
            if i == 3 or i == 6:
                continue
            pygame.draw.line(self.screen, "black", (0, self.box_h * i),
                         (self.width, self.box_h * i), 1)
            pygame.draw.line(self.screen, "black", (self.box_w * i, 0),
                             (self.box_w * i, self.height), 1)

    def select(self, row, col):
        self.selected_cell = row, col
    #     Marks the cell at (row, col) in the board as the current selected cell.
    #     Once a cell has been selected, the user can edit its value or sketched value.
    #
    def click(self, x, y):
        col = int(x // self.box_w)
        row = int(y // self.box_h)
        if row <= 8 and col <= 8:
            return row, col
        return None
    #     If a tuple of (x,y) coordinates is within the displayed board,
    # this function returns a tuple of the (row, col) of the cell which was clicked.
    # Otherwise, this function returns None.
    #
    # def clear(self)
    #     Clears the value cell.
    # Note that the user can only remove the cell values and
    # sketched values that are filled by themselves.
    #
    # def sketch(self, value)
    #     Sets the sketched value of the current selected cell equal to the user entered value.
    #     It will be displayed at the top left corner of the cell using the draw() function.
    #
    # def place_number(self, value)
    #     Sets the value of the current selected cell equal to the user entered value.
    # Called when the user presses the Enter key.
    #
    # def reset_to_original(self)
    #     Resets all cells in the board to their original values
    # (0 if cleared, otherwise the corresponding digit).
    #
    #
    # def is_full(self)
    #     Returns a Boolean value indicating whether the board is full or not.
    #
    # def update_board(self)
    #     Updates the underlying 2D board with the values in all cells.
    #
    # def find_empty(self)
    #     Finds an empty cell and returns its row and col as a tuple (x,y).
    #
    # def check_board(self)
    # Check whether the Sudoku board is solved correctly.


# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width = 600
window_height = 600

# Create the window
screen = pygame.display.set_mode((window_width, window_height))

# Initialize Board
board = Board(window_width, window_height, screen, "easy")

# Set the window title
pygame.display.set_caption("Pygame Window")

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # print(board.click(x, y))
            row, col = board.click(x, y)
            board.select(row, col)

    # Fill the screen with a color (e.g., white)
    screen.fill((255, 255, 255))

    # Draw lines
    board.draw()

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()