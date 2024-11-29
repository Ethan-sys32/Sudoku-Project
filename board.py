import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # Generate the board
        self.sudoku_generator = SudokuGenerator(9, difficulty)
        self.sudoku_generator.fill_values()
        self.sudoku_generator.remove_cells()

        # Create cells from the board
        self.board = self.sudoku_generator.get_board()
        self.cells = [[Cell(self.board[row][col], row, col, screen) for col in range(9)] for row in range(9)]
        self.selected_cell = None
        self.original_board = [[cell.value for cell in row] for row in self.cells]

    def draw(self):
        # Draw all cells
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

        # Draw grid lines
        for i in range(10):
            thickness = 5 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 60), (540, i * 60), thickness)  # Horizontal
            pygame.draw.line(self.screen, (0, 0, 0), (i * 60, 0), (i * 60, 540), thickness)  # Vertical

    def select(self, row, col):
        # Highlight a cell
        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def sketch(self, value):
        # Add a temporary value to a cell
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        # Set a value in a cell
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.set_cell_value(value)
            self.selected_cell.sketched_value = None
            self.update_board()

    def reset_to_original(self):
        # Reset the board to the start
        for row in range(9):
            for col in range(9):
                self.cells[row][col].value = self.original_board[row][col]
                self.cells[row][col].sketched_value = None

    def is_full(self):
        # Check if the board is complete
        return all(cell.value != 0 for row in self.cells for cell in row)

    def check_board(self):
        # Check if the board is correct
        for row in range(9):  # Check rows
            if len(set(cell.value for cell in self.cells[row])) != 9:
                return False

        for col in range(9):  # Check columns
            if len(set(self.cells[row][col].value for row in range(9))) != 9:
                return False

        for box_row in range(0, 9, 3):  # Check 3x3 boxes
            for box_col in range(0, 9, 3):
                box = [self.cells[row][col].value for row in range(box_row, box_row + 3) for col in range(box_col, box_col + 3)]
                if len(set(box)) != 9:
                    return False

        return True

    def update_board(self):
        # Update the board with cell values
        self.board = [[cell.value for cell in row] for row in self.cells]
