import pygame

"""Инициализация ПуГаме"""
pygame.init()
"""Окно"""
width, height = window_size = 16 * 64, 9 * 64
screen = pygame.display.set_mode(window_size)
"""Клок"""
clock = pygame.time.Clock()
"""Шрифт"""
pygame.font.init()
font_used = pygame.font.SysFont("proxima nova bold", 32)
"""Предустановка переменных"""


"""Класс доски"""
class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[(255, 255, 0)] * width for _ in range(height)]

        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 64
    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def update(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, (0, 0, 0), (
                    self.left + self.cell_size * x, self.top + self.cell_size * y,
                    self.cell_size, self.cell_size), 4)
                pygame.draw.rect(screen, self.board[y][x], (
                    self.left + self.cell_size * x + 2,
                    self.top + self.cell_size * y + 2,
                    self.cell_size - 4, self.cell_size - 4))

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if x > self.cell_size * self.width + self.left or \
                x < self.left or \
                y > self.cell_size * self.height + self.top or \
                y < self.top:
            return None
        else:
            x, y = int((x - self.left) / self.cell_size), \
                   int((y - self.top) / self.cell_size)
            return x, y

    def on_click(self, cell_coords):
        if cell_coords is None:
            return
        y, x = cell_coords
        if self.board[x][y] == (255, 255, 0):
            self.board[x][y] = (0, 0, 0)
        elif self.board[x][y] == (0, 0, 0):
            self.board[x][y] = (0, 255, 0)
        elif self.board[x][y] == (0, 255, 0):
            self.board[x][y] = (255, 255, 0)


"""Основные функциональные классы"""


class Button(pygame.sprite.Sprite):
    """Инициализация кнопки"""

    def __init__(self, size=(100, 50), position=(0, 0), base_color=(0, 128, 0), pointed_color=(0, 255, 0), text=None,
                 bind=None):
        pygame.sprite.Sprite.__init__(self)
        """Основные переменные"""
        self.length, self.height = size
        self.base_color, self.pointed_color = base_color, pointed_color
        self.bind = bind
        if text == None:
            text = bind
        self.text = font_used.render(text, True, (255, 255, 255))
        """Создание картинки или дрйгой херни"""
        self.image = pygame.Surface([self.length, self.height])
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    """Что делает кнопка"""

    def update(self):
        """Здесь пишутся функции к которым обращаются кнопки"""
        self.image.fill(self.base_color)
        """На кнопку навели курсор"""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # some action
            self.image.fill(self.pointed_color)
            """На кнопку ещё и нажали"""
            if (pygame.mouse.get_pressed(3)[0] or pygame.key.get_pressed()[pygame.K_SPACE]) and self.bind != None:
                print(self.bind)
                """Бинд кнопок"""
                if self.bind == 'game':
                    game_process()
                elif self.bind == 'how2play':
                    how_to_play()
                elif self.bind == 'menu':
                    main_menu()
        screen.blit(self.text, (self.rect.x + 10, self.rect.y + 10))


"""Функции интерфейсов и игровых процессов"""


def game_process():
    """Предустановка для Меню"""
    fps = 60
    buttons = pygame.sprite.Group()
    """Создание доски"""
    board = Board(16, 9)
    """Основной игровой цикл окна"""
    process_run = True
    while process_run:
        screen.fill((255, 255, 255))
        clock.tick(fps)
        """Реакция на события в окне"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                process_run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.on_click(board.get_cell(event.pos))

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_b]:
                    button = Button(size=(250, 100), bind='menu')
                    buttons.add(button)
                if keys[pygame.K_ESCAPE]:
                    main_menu()
        """Отображение кнопок"""
        board.update(screen)
        buttons.draw(screen)

        buttons.update()
        """Отрисовка всего что нужно в окне"""
        """Обновление экрана"""
        pygame.display.flip()
    """Основной игровой цикл окна закончился"""
    pygame.quit()


def how_to_play():
    # print('Жопой об косяк')
    print("Привет, мир! Играй руками")


def main_menu():
    """Предустановка для Меню"""
    fps = 60
    """Кнопки окна"""
    buttons = pygame.sprite.Group()
    quantity_buttons = 3 + 1
    button_width, button_height = 500, height // quantity_buttons - 20

    button_game = Button(position=(int(width / 2 - button_width / 2), int(height / quantity_buttons - button_height / 2)),
                         size=(button_width, button_height), bind='game')
    button_how2play = Button(position=(int(width / 2 - button_width / 2), int(height * 2 / quantity_buttons - button_height / 2)),
                             size=(button_width, button_height), bind='how2play')
    button_authors = Button(position=(int(width / 2 - button_width / 2), int(height * 3 / quantity_buttons - button_height / 2)),
                             size=(button_width, button_height), bind='authors')
    buttons.add(button_game)
    buttons.add(button_how2play)
    buttons.add(button_authors)
    """Основной игровой цикл окна"""
    process_run = True
    while process_run:
        screen.fill((0, 0, 0))
        clock.tick(fps)
        """Реакция на события в окне"""
        for event in pygame.event.get():
            """Нажат крестик у приложения"""
            if event.type == pygame.QUIT:
                process_run = False
            """Нажата любая кнопка"""
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
        """Обновление и отрисовка всего что нужно в окне"""
        buttons.draw(screen)
        buttons.update()
        """Отрисовка всего что нужно в окне"""
        """Обновление экрана"""
        pygame.display.flip()
    """Основной игровой цикл окна закончился"""
    pygame.quit()


"""Инициализация меню"""
main_menu()
