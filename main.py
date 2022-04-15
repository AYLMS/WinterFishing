import sys
import pygame


"""Инициализация ПуГаме"""
pygame.init()
"""Окно"""
width, height = window_size = 16 * 80, 9 * 80
screen = pygame.display.set_mode(window_size)
"""Клок"""
clock = pygame.time.Clock()
"""Шрифт"""
pygame.font.init()
font_used = pygame.font.SysFont("proxima nova bold", 32)
"""Предустановка переменных"""


"""Основные функциональные классы"""


class Board:
    """Инициализация доски"""
    def __init__(self, lines_and_columns=(5, 5), cell_size=(64, 64), left_gap=0, up_gap=0, grid_color=(32, 128, 64)):
        """Основные константы и переменные"""
        # количество столбцов и строчек
        self.lines, self.columns = lines_and_columns
        # размеры клеток
        self.cell_size_x, self.cell_size_y = cell_size
        # отступы доски слева и сверху
        self.left_gap, self.up_gap = left_gap, up_gap
        # цвет сетки
        self.grid_color = grid_color
        """Матрица доски"""
        # с ней можно потом свободно взаимодействовать
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
        # если нажали на клетку
        if position:
            # действия, реакция на нажатия
            column, line = position
            print(self.board[line][column])

    def render(self, screen):
        """Отрисовка сетки и клеток у доски"""
        # перебором каждой клетки, да долго, но удобно зато)
        for line in range(self.lines):
            for column in range(self.columns):
                """Отрисовка сетки"""
                pygame.draw.rect(screen, self.grid_color, (self.left_gap + column * self.cell_size_x, self.up_gap + line * self.cell_size_y, self.cell_size_x, self.cell_size_y), 1)
                """Отрисовка клеток"""
                """if (column + line) % 2 == 1:
                    pygame.draw.rect(screen, (0, 0, 0), (self.left_gap + column * self.cell_size_x, self.up_gap + line * self.cell_size_y, self.cell_size_x, self.cell_size_y))
                else:
                    pygame.draw.rect(screen, (223, 223, 223), (self.left_gap + column * self.cell_size_x, self.up_gap + line * self.cell_size_y, self.cell_size_x, self.cell_size_y))"""
                """Отрисовка содержимого клеток"""


class Button(pygame.sprite.Sprite):
    """Инициализация кнопки"""
    def __init__(self, size=(100, 50), position=(0, 0), base_color=(0, 128, 0), pointed_color=(32, 160, 32), text=''):
        pygame.sprite.Sprite.__init__(self)
        """Основные константы и переменные"""
        # длина и высота кнопки
        self.length, self.height = size
        # основной цвет и цвет когда навелись
        self.base_color, self.pointed_color = base_color, pointed_color
        # бинд кнопки
        # текст не передан - текст на кнопке название бинда
        # шрифт текста кнопки
        self.text = font_used.render(text, True, (255, 255, 255))
        """Создание картинки или дрйгой херни"""
        self.image = pygame.Surface([self.length, self.height])
        self.rect = self.image.get_rect()
        # размещение кнопки
        self.rect.x, self.rect.y = position

    """Отрисовка кнопки"""
    def update(self):
        """Здесь пишутся функции к которым обращаются кнопки"""
        """На кнопку навели курсор"""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # some action
            self.image.fill(self.pointed_color)
        else:
            # кнопка просто есть
            self.image.fill(self.base_color)
        screen.blit(self.text, (self.rect.x + 10, self.rect.y + 10))

    """Реакция кнопки на нажатие"""
    def clicked(self):
        return bool(self.rect.collidepoint(pygame.mouse.get_pos()) and (pygame.mouse.get_pressed(3)[0] or pygame.key.get_pressed()[pygame.K_SPACE]))



"""Функции интерфейсов и игровых процессов"""


def game():
    """Предустановка для Меню"""
    # частота обновления кадров
    fps = 60
    """Кнопки окна"""
    buttons = pygame.sprite.Group()
    b_back = Button(size=(4 * 80, 2 * 80), position=(10 * 80, 1 * 80), base_color=(0, 0, 0), pointed_color=(32, 32, 32), text='Назад')
    buttons.add(b_back)
    b_yes = Button(size=(4 * 80, 2 * 80), position=(10*80, 3.5*80), base_color=(64, 192, 64), pointed_color=(96, 226, 96))
    buttons.add(b_yes)
    b_no = Button(size=(4 * 80, 2 * 80), position=(10*80, 6*80), base_color=(192, 64, 64), pointed_color=(226, 96, 96))
    buttons.add(b_no)
    board = Board(lines_and_columns=(9, 16), cell_size=(80, 80), grid_color=(32, 32, 128))
    # и тут создание кнопочек
    """Основной игровой цикл окна"""
    # запуск цикла
    process_run = True
    image = pygame.image.load('data\images.jpg')
    # сам цикл игры
    while process_run:
        # заливка экрана
        screen.fill((255, 255, 255))
        # выставляем частоту кадров
        clock.tick(fps)
        """Реакция на события в окне"""
        for event in pygame.event.get():
            """Нажат крестик у приложения"""
            if event.type == pygame.QUIT:
                process_run = False
            """Нажата любая кнопка"""
            if event.type == pygame.KEYDOWN:
                # список всех кнопок, к ним просто обращаемся
                keys = pygame.key.get_pressed()
                # здесь сам бинд кнопок
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_buttons = pygame.mouse.get_pressed()
                if b_back.clicked():
                    example()
                if b_yes.clicked():
                    print('да')
                if b_no.clicked():
                    print('Нет')
        """Обновление всего что нужно в окне"""
        # здесь чисто update классов
        """Отрисовка всего что нужно в окне"""
        # отображение сетки, игрока...
        board.render(screen)
        """Отрисовка и обновление кнопочек"""
        # отрисовка кнопочек
        screen.blit(image, (10, 10))
        buttons.draw(screen)
        buttons.update()
        """Обновление экрана"""
        pygame.display.flip()
    """Основной игровой цикл окна закончился"""
    # закрываем Пугаме
    pygame.quit()
    # вырубаем программу, чтобы ошибок не было )))
    sys.exit(0)


def example():
    """Предустановка для Меню"""
    # частота обновления кадров
    fps = 60
    """Кнопки окна"""
    buttons = pygame.sprite.Group()
    b_game = Button(size=(4 * 80, 2 * 80), position=(2*80, 1*80), base_color=(0, 0, 0), pointed_color=(32, 32, 32), text='НАЧАЛО ИГРЫ')
    buttons.add(b_game)
    b_authors = Button(size=(4 * 80, 2 * 80), position=(2*80, 3.5*80), base_color=(0, 0, 0), pointed_color=(32, 32, 32), text='Авторы')
    buttons.add(b_authors)
    b_settings = Button(size=(4 * 80, 2 * 80), position=(2 * 80, 6 * 80), base_color=(0, 0, 0), pointed_color=(32, 32, 32), text='Настройки')
    buttons.add(b_settings)
    board = Board(lines_and_columns=(9, 16), cell_size=(80, 80), grid_color=(32, 128, 32))
    b_exit = Button(size=(4 * 80, 2 * 80), position=(6*80, 3.5*80), base_color=(0, 0, 0), pointed_color=(32, 32, 32), text='Вырубай')
    buttons.add(b_exit)
    # и тут создание кнопочек
    """Основной игровой цикл окна"""
    # запуск цикла
    process_run = True
    # сам цикл игры
    while process_run:
        # заливка экрана
        screen.fill((255, 255, 255))
        # выставляем частоту кадров
        clock.tick(fps)
        """Реакция на события в окне"""
        for event in pygame.event.get():
            """Нажат крестик у приложения"""
            if event.type == pygame.QUIT:
                process_run = False
            """Нажата любая кнопка"""
            if event.type == pygame.KEYDOWN:
                # список всех кнопок, к ним просто обращаемся
                keys = pygame.key.get_pressed()
                # здесь сам бинд кнопок
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_buttons = pygame.mouse.get_pressed()
                if b_game.clicked():
                    game()
                if b_exit.clicked():
                    process_run = False
        """Обновление всего что нужно в окне"""
        # здесь чисто update классов
        """Отрисовка всего что нужно в окне"""
        board.render(screen)
        # отображение сетки, игрока...
        """Отрисовка и обновление кнопочек"""
        # отрисовка кнопочек
        buttons.draw(screen)
        buttons.update()
        """Обновление экрана"""
        pygame.display.flip()
    """Основной игровой цикл окна закончился"""
    # закрываем Пугаме
    pygame.quit()
    # вырубаем программу, чтобы ошибок не было )))
    sys.exit(0)


"""Инициализация меню"""
# здесь начальный процесс
example()