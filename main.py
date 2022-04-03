import random

import pygame
import time


class Helicopter(pygame.sprite.Sprite):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([72, 48])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = xy

    def coords(self):
        return self.rect.center

    def update(self):
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += 1
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= 1
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y -= 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y += 1


class Hole(pygame.sprite.Sprite):
    def __init__(self, coords=(random.randint(18, 702), random.randint(12, 468)), isbomb=False):
        self.needkill = False
        self.k = 0.5
        self.lifetime = 60 * 5
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([self.k * self.lifetime, self.k * self.lifetime])
        self.image.fill((random.randint(0, 255), 25, 125))
        self.rect = self.image.get_rect()

        self.rect.center = coords
        if isbomb and pygame.sprite.spritecollide(self, holes, False):
            self.needkill = True
            print('*плюх')
        else:
            while pygame.sprite.spritecollide(self, holes, False):
                self.rect.center = (random.randint(18, 702), random.randint(12, 468))

    def update(self):
        self.lifetime -= 1
        self.image = pygame.Surface((int(self.k * self.lifetime), int(self.k * self.lifetime)))
        self.image.fill((random.randint(0, 255), 25, 125))
        self.rect = self.image.get_rect()

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    size = width, height = 720, 480
    screen = pygame.display.set_mode(size)
    screen.fill((100, 100, 100))

    all_sprites = pygame.sprite.Group()
    hel = pygame.sprite.Group()
    helicopter = Helicopter((360, 240))
    all_sprites.add(helicopter)
    hel.add(helicopter)

    holes = pygame.sprite.Group()

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    print("space_pressed")
                    x, y = helicopter.coords()
                    hole = Hole(coords=(x, y + 48), isbomb=True)
                    holes.add(hole)
                    all_sprites.add(hole)
                    if hole.needkill:
                        hole.kill()

        screen.fill((224, 255, 255))
        all_sprites.update()
        all_sprites.draw(screen)
        hel.draw(screen)
        pygame.display.flip()
    pygame.quit()
