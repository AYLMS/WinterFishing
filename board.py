import pygame


class Board:
    """Инициализация доски"""
    def __init__(self, lines_and_columns=(5, 5), cell_size=(64, 64), left_gap=0, up_gap=0, grid_color=(32, 128, 64)):
        """Основные константы и переменные"""
        self.lines, self.columns = lines_and_columns
        self.cell_size_x, self.cell_size_y = cell_size
        self.left_gap, self.up_gap = left_gap, up_gap
        self.grid_color = grid_color
        """Матрица доски"""
        self.board = [[0] * self.columns for _ in range(self.lines)]

    def get_cell(self, mouse_pos):
        """Получение номера клетки формата (x, y)"""
        x, y = mouse_pos
        """Вне поля"""
        if x < self.left_gap or x > self.left_gap + self.columns * self.cell_size_x or y < self.up_gap or y > self.up_gap + self.lines * self.cell_size_y:
            return None
        """В поле"""
        column, line = int((x - self.left_gap) / self.cell_size_x), int((y - self.up_gap) / self.cell_size_y)
        return column, line

    def on_click(self, position):
        """События после нажатия"""
        if position != None:
            column, line = position
            self.board[line][column] = 60 * 10


    def render(self, screen):
        """Отрисовка сетки и клеток у доски"""
        for line in range(self.lines):
            for column in range(self.columns):
                """Отрисовка сетки"""
                pygame.draw.rect(screen, self.grid_color, (self.left_gap + column * self.cell_size_x, self.up_gap + line * self.cell_size_y, self.cell_size_x, self.cell_size_y), 1)
                """Отрисовка содержимого клеток"""
                lifetime = self.board[line][column]
                if lifetime > 0:
                    k = lifetime / 600
                    pygame.draw.circle(screen, (254 - int(135 * k), 254 - int(65 * k), 254 - int(53 * k)), (self.left_gap + column * self.cell_size_x + self.cell_size_x // 2, self.up_gap + line * self.cell_size_y + self.cell_size_y // 2), self.cell_size_x // 2)
                    self.board[line][column] -= 1
                elif lifetime == -1:
                    pygame.draw.rect(screen, (89, 142, 57), (self.left_gap + column * self.cell_size_x, self.up_gap + line * self.cell_size_y, self.cell_size_x, self.cell_size_y))
                    # pygame.draw.circle(screen, (164, 128, 64), (self.left_gap + column * self.cell_size_x + self.cell_size_x // 2, self.up_gap + line * self.cell_size_y + self.cell_size_y // 2), self.cell_size_x // 2)
