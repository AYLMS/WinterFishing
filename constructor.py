import pygame
import sys
from board import Board
from player import Helicopter


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


class Button(pygame.sprite.Sprite):
    """Инициализация кнопки"""

    def __init__(self, size=(100, 50), position=(0, 0), base_color=(0, 128, 0), pointed_color=(0, 160, 0), text=None,
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
    board = Board(lines_and_columns=(18, 32), cell_size=(40, 40))
    for i in range(32):
        board.board[0][i] = -2
        board.board[-1][i] = -2
    print(board.board)
    for i in range(18):
        board.board[i][0] = -2
        board.board[i][-1] = -2
    print(board.board)
    """Создание игрока"""
    all_sprites = pygame.sprite.Group()
    hel_group = pygame.sprite.Group()
    helicopter = Helicopter((360, 240), screen)
    all_sprites.add(helicopter)
    hel_group.add(helicopter)
    """Основной игровой цикл окна"""
    process_run = True
    while process_run:
        screen.fill((254, 254, 254))
        x, y = helicopter.rect.center
        y += 50
        x -= 20
        clock.tick(fps)
        """Реакция на события в окне"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                process_run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(board.get_cell(pygame.mouse.get_pos()))
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_b]:
                    button = Button(size=(250, 100), bind='menu')
                    buttons.add(button)
                if keys[pygame.K_ESCAPE]:
                    main_menu()
                if keys[pygame.K_SPACE]:
                    board.on_click(board.get_cell((x, y)))
        """"Обновление игровых объектов"""
        all_sprites.update()
        """Отрисовка всего что нужно в окне"""
        board.render(screen)
        pygame.draw.rect(screen, (0, 0, 0), (x, y, 10, 10))
        hel_group.draw(screen)
        """Отображение кнопок"""
        buttons.draw(screen)
        buttons.update()
        """Обновление экрана"""
        pygame.display.flip()
    """Основной игровой цикл окна закончился"""
    pygame.quit()
    sys.exit(0)


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
    sys.exit(0)

"""Инициализация меню"""
main_menu()
