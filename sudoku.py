# Lauren Hill

import pygame
import sys
from board import Board

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 540, 600  # 540 for 9x9 board, extra space for buttons
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")

# Fonts
FONT = pygame.font.SysFont("comicsans", 40)
BUTTON_FONT = pygame.font.SysFont("comicsans", 30)

# Colors
BG_COLOR = (255, 255, 255)

# Global state
current_screen = "start"
difficulty = None
board = None

def draw_text_center(text, font, color, surface, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(WIDTH // 2, y))
    surface.blit(text_obj, text_rect)

def draw_button(text, x, y, w, h, surface):
    pygame.draw.rect(surface, (200, 200, 200), (x, y, w, h))
    label = BUTTON_FONT.render(text, True, (0, 0, 0))
    label_rect = label.get_rect(center=(x + w//2, y + h//2))
    surface.blit(label, label_rect)
    return pygame.Rect(x, y, w, h)

def start_screen():
    SCREEN.fill(BG_COLOR)
    draw_text_center("Sudoku", FONT, (0, 0, 0), SCREEN, 100)
    easy_btn = draw_button("Easy", 200, 200, 140, 50, SCREEN)
    med_btn = draw_button("Medium", 200, 270, 140, 50, SCREEN)
    hard_btn = draw_button("Hard", 200, 340, 140, 50, SCREEN)
    pygame.display.update()
    return easy_btn, med_btn, hard_btn

def end_screen(won):
    SCREEN.fill(BG_COLOR)
    if won:
        draw_text_center("You Win!", FONT, (0, 200, 0), SCREEN, 200)
    else:
        draw_text_center("Game Over", FONT, (200, 0, 0), SCREEN, 200)
    restart_btn = draw_button("Restart", 200, 300, 140, 50, SCREEN)
    pygame.display.update()
    return restart_btn

def draw_buttons():
    reset_btn = draw_button("Reset", 30, 550, 100, 40, SCREEN)
    restart_btn = draw_button("Restart", 220, 550, 100, 40, SCREEN)
    exit_btn = draw_button("Exit", 410, 550, 100, 40, SCREEN)
    return reset_btn, restart_btn, exit_btn

def main():
    global current_screen, difficulty, board
    selected = None
    running = True

    while running:
        if current_screen == "start":
            easy_btn, med_btn, hard_btn = start_screen()
        elif current_screen == "game":
            SCREEN.fill(BG_COLOR)
            board.draw()
            reset_btn, restart_btn, exit_btn = draw_buttons()
            pygame.display.update()
        elif current_screen == "win":
            restart_btn = end_screen(True)
        elif current_screen == "lose":
            restart_btn = end_screen(False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if current_screen == "start":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_btn.collidepoint(event.pos):
                        difficulty = "easy"
                        board = Board(WIDTH, HEIGHT - 60, SCREEN, difficulty)
                        current_screen = "game"
                    elif med_btn.collidepoint(event.pos):
                        difficulty = "medium"
                        board = Board(WIDTH, HEIGHT - 60, SCREEN, difficulty)
                        current_screen = "game"
                    elif hard_btn.collidepoint(event.pos):
                        difficulty = "hard"
                        board = Board(WIDTH, HEIGHT - 60, SCREEN, difficulty)
                        current_screen = "game"

            elif current_screen == "game":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if y < HEIGHT - 60:
                        pos = board.click(x, y)
                        if pos:
                            board.select(pos[0], pos[1])
                    elif reset_btn.collidepoint(event.pos):
                        board.reset_to_original()
                    elif restart_btn.collidepoint(event.pos):
                        current_screen = "start"
                        board = None
                    elif exit_btn.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if board.selected:
                        if event.key in [pygame.K_1, pygame.K_KP1]: value = 1
                        elif event.key in [pygame.K_2, pygame.K_KP2]: value = 2
                        elif event.key in [pygame.K_3, pygame.K_KP3]: value = 3
                        elif event.key in [pygame.K_4, pygame.K_KP4]: value = 4
                        elif event.key in [pygame.K_5, pygame.K_KP5]: value = 5
                        elif event.key in [pygame.K_6, pygame.K_KP6]: value = 6
                        elif event.key in [pygame.K_7, pygame.K_KP7]: value = 7
                        elif event.key in [pygame.K_8, pygame.K_KP8]: value = 8
                        elif event.key in [pygame.K_9, pygame.K_KP9]: value = 9
                        else: value = None

                        if value is not None:
                            board.sketch(value)

                        if event.key == pygame.K_RETURN:
                            board.place_number(board.get_sketched_value())
                            if board.is_full():
                                if board.check_board():
                                    current_screen = "win"
                                else:
                                    current_screen = "lose"

                    # Arrow key navigation
                    elif event.key == pygame.K_UP:
                        board.move_selection("up")
                    elif event.key == pygame.K_DOWN:
                        board.move_selection("down")
                    elif event.key == pygame.K_LEFT:
                        board.move_selection("left")
                    elif event.key == pygame.K_RIGHT:
                        board.move_selection("right")

            elif current_screen in ["win", "lose"]:
                if event.type == pygame.MOUSEBUTTONDOWN and restart_btn.collidepoint(event.pos):
                    current_screen = "start"
                    board = None

if __name__ == "__main__":
    main()
