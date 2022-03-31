import pygame
import time


class Helicopter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([72, 48])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def move(self, coords):
        self.rect.center = coords

    def update(self):
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += 1
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= 1
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y -= 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y += 1


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    size = width, height = 720, 480
    screen = pygame.display.set_mode(size)
    screen.fill((100, 100, 100))
    all_sprites = pygame.sprite.Group()
    hel = pygame.sprite.Group()
    helicopter = Helicopter()
    all_sprites.add(helicopter)
    hel.add(helicopter)
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((100, 100, 100))
        all_sprites.draw(screen)
        hel.update()
        pygame.display.flip()
    pygame.quit()
