import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_value = None

    def set_cell_value(self, value):
        # Set the final value
        self.value = value

    def set_sketched_value(self, value):
        # Set a temporary value
        self.sketched_value = value

    def draw(self):
        # Draw the cell background
        cell_rect = pygame.Rect(self.col * 60, self.row * 60, 60, 60)
        pygame.draw.rect(self.screen, (255, 255, 255), cell_rect)

        # Highlight if selected
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), cell_rect, 3)  # Red border
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), cell_rect, 1)  # Black border

        # Draw the value or sketched value
        font = pygame.font.Font(None, 40)
        if self.value != 0:
            # Draw final value
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (self.col * 60 + 20, self.row * 60 + 10))
        elif self.sketched_value:
            # Draw temporary value
            text = font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(text, (self.col * 60 + 5, self.row * 60 + 5))
