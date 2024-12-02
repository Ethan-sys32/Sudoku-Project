import pygame
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.temporary_value = None

    def set_cell_value(self, value):
        # Sets the final chosen value for the cell
        self.value = value

    def set_temporary_value(self, value):
        # Shows the value that the user wants to input before entering
        self.temporary_value = value

    def draw(self):
        # makes the outline for each square and has white background for each grid cell
        rectangle = pygame.Rect(self.col * 60, self.row * 60, 60, 60)
        pygame.draw.rect(self.screen, (255, 255, 255), rectangle)

        # if the square on grid is selected it will turn red otherwise it will stay black
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), rectangle, 3)  # Red grid cell
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), rectangle, 1)  # Black grid cell

        # Shows the value before entering it in and shows the finale value, with the font size and colors accordingly
        font_size = pygame.font.Font(None, 40)
        if self.value != 0:
            # Shows the final value that the user selects in black
            text = font_size.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (self.col * 60 + 20, self.row * 60 + 10))
        elif self.temporary_value is not None:
            # shows the value that the user is going to enter in gray before they finalize it
            text = font_size.render(str(self.temporary_value), True, (128, 128, 128))
            self.screen.blit(text, (self.col * 60 + 5, self.row * 60 + 5))
