import pygame
import sys
from board import Board

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((540, 600))
pygame.display.set_caption("Sudoku")


def game_start_screen(screen):
    # Show the game start screen
    font_large = pygame.font.Font(None, 50)
    font_medium = pygame.font.Font(None, 30)


    running = True
    while running:
        screen.fill((255, 255, 255))

        # Draw text
        title_text = font_large.render("Welcome to Sudoku", True, (0, 0, 0))
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))

        select_text = font_medium.render("Select Game Mode:", True, (0, 0, 0))
        screen.blit(select_text, (screen.get_width() // 2 - select_text.get_width() // 2, 200))
# Draw buttons
        button_width, button_height = 120, 50
        spacing = 20
        total_width = 3 * button_width + 2 * spacing
        start_x = (screen.get_width() - total_width) // 2
        easy_button = pygame.Rect(start_x, 300, button_width, button_height)
        medium_button = pygame.Rect(start_x + button_width + spacing, 300, button_width, button_height)
        hard_button = pygame.Rect(start_x + 2 * (button_width + spacing), 300, button_width, button_height)

        pygame.draw.rect(screen, (255, 140, 0), easy_button)
        pygame.draw.rect(screen, (255, 140, 0), medium_button)
        pygame.draw.rect(screen, (255, 140, 0), hard_button)

# Draw button text
        easy_text = font_medium.render("EASY", True, (255, 255, 255))
        medium_text = font_medium.render("MEDIUM", True, (255, 255, 255))
        hard_text = font_medium.render("HARD", True, (255, 255, 255))

        screen.blit(easy_text, (easy_button.x + button_width // 2 - easy_text.get_width() // 2,
                                easy_button.y + button_height // 2 - easy_text.get_height() // 2))
        screen.blit(medium_text, (medium_button.x + button_width // 2 - medium_text.get_width() // 2,
                                  medium_button.y + button_height // 2 - medium_text.get_height() // 2))
        screen.blit(hard_text, (hard_button.x + button_width // 2 - hard_text.get_width() // 2,
                                hard_button.y + button_height // 2 - hard_text.get_height() // 2))

# Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if easy_button.collidepoint(pos):
                    return 30
                elif medium_button.collidepoint(pos):
                    return 40
                elif hard_button.collidepoint(pos):
                    return 50

        pygame.display.flip()


def draw_game_buttons(screen):
# Draw reset, restart, and exit buttons
    font = pygame.font.Font(None, 30)
    button_width, button_height = 100, 40
    spacing = 20
    total_width = 3 * button_width + 2 * spacing
    start_x = (screen.get_width() - total_width) // 2

    reset_button = pygame.Rect(start_x, 550, button_width, button_height)
    restart_button = pygame.Rect(start_x + button_width + spacing, 550, button_width, button_height)
    exit_button = pygame.Rect(start_x + 2 * (button_width + spacing), 550, button_width, button_height)

    pygame.draw.rect(screen, (255, 140, 0), reset_button)
    pygame.draw.rect(screen, (255, 140, 0), restart_button)
    pygame.draw.rect(screen, (255, 140, 0), exit_button)

    reset_text = font.render("RESET", True, (255, 255, 255))
    restart_text = font.render("RESTART", True, (255, 255, 255))
    exit_text = font.render("EXIT", True, (255, 255, 255))

    screen.blit(reset_text, (reset_button.x + button_width // 2 - reset_text.get_width() // 2,
                             reset_button.y + button_height // 2 - reset_text.get_height() // 2))
    screen.blit(restart_text, (restart_button.x + button_width // 2 - restart_text.get_width() // 2,
                               restart_button.y + button_height // 2 - restart_text.get_height() // 2))
    screen.blit(exit_text, (exit_button.x + button_width // 2 - exit_text.get_width() // 2,
                            exit_button.y + button_height // 2 - exit_text.get_height() // 2))

    return reset_button, restart_button, exit_button


def game_won_screen(screen):
# Show the game won screen
    font_large = pygame.font.Font(None, 60)
    font_medium = pygame.font.Font(None, 40)

    running = True
    while running:
        screen.fill((255, 255, 255))

        # Draw text
        win_text = font_large.render("Game Won!", True, (0, 128, 0))
        screen.blit(win_text, (screen.get_width() // 2 - win_text.get_width() // 2, 200))

        # Draw button
        button_width, button_height = 150, 50
        restart_button = pygame.Rect(
            screen.get_width() // 2 - button_width // 2, 350, button_width, button_height
        )
        pygame.draw.rect(screen, (255, 140, 0), restart_button)

        restart_text = font_medium.render("RESTART", True, (255, 255, 255))
        screen.blit(
            restart_text,
            (
                restart_button.x + button_width // 2 - restart_text.get_width() // 2,
                restart_button.y + button_height // 2 - restart_text.get_height() // 2,
            ),
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if restart_button.collidepoint(pos):
                    return "restart"

        pygame.display.flip()


def game_over_screen(screen):
    # Show the game over screen
    font_large = pygame.font.Font(None, 60)
    font_medium = pygame.font.Font(None, 40)

    running = True
    while running:
        screen.fill((255, 255, 255))

        # Draw text
        lose_text = font_large.render("Game Over :(", True, (255, 0, 0))
        screen.blit(lose_text, (screen.get_width() // 2 - lose_text.get_width() // 2, 200))

        # Draw button
        button_width, button_height = 150, 50
        restart_button = pygame.Rect(
            screen.get_width() // 2 - button_width // 2, 350, button_width, button_height
        )
        pygame.draw.rect(screen, (255, 140, 0), restart_button)

        restart_text = font_medium.render("RESTART", True, (255, 255, 255))
        screen.blit(
            restart_text,
            (
                restart_button.x + button_width // 2 - restart_text.get_width() // 2,
                restart_button.y + button_height // 2 - restart_text.get_height() // 2,
            ),
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if restart_button.collidepoint(pos):
                    return "restart"

        pygame.display.flip()


def main():
    # Run the main game loop
    difficulty = game_start_screen(screen)
    board = Board(540, 540, screen, difficulty)

    while True:
        screen.fill((255, 255, 255))
        board.draw()

        reset_button, restart_button, exit_button = draw_game_buttons(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if reset_button.collidepoint(pos):
                    board.reset_to_original()
                elif restart_button.collidepoint(pos):
                    return main()
                elif exit_button.collidepoint(pos):
                    pygame.quit()
                    sys.exit()
                else:
                    row, col = pos[1] // 60, pos[0] // 60
                    if row < 9 and col < 9:
                        board.select(row, col)

            elif event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    value = event.key - pygame.K_0
                    board.sketch(value)
                elif event.key == pygame.K_RETURN:
                    if board.selected_cell and board.selected_cell.sketched_value:
                        board.place_number(board.selected_cell.sketched_value)

        if board.is_full():
            if board.check_board():
                if game_won_screen(screen) == "restart":
                    return main()
            else:
                if game_over_screen(screen) == "restart":
                    return main()

        pygame.display.flip()


if __name__ == "__main__":
    main()
