import pygame


class Helicopter(pygame.sprite.Sprite):
    def __init__(self, xy, screen):
        pygame.sprite.Sprite.__init__(self)
        """
        self.image = pygame.Surface([72, 48])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        """
        self.cooldown = 120
        self.skin = 1
        self.image = pygame.image.load(f"data/helicopters/{1}.gif")
        self.image.set_colorkey((0, 254, 0))
        self.image = pygame.transform.scale(self.image, (120, 80))
        self.rect = self.image.get_rect(center=(0, 0))

        self.rect.center = xy

    def coords(self):
        return self.rect.center

    def update(self):
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.rect.right < 32 * 40:
            self.rect.x += 10
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.rect.left > 20:
            self.rect.x -= 10
        if pygame.key.get_pressed()[pygame.K_UP] and self.rect.top > -40:
            self.rect.y -= 6
        if pygame.key.get_pressed()[pygame.K_DOWN] and self.rect.bottom < 16 * 40:
            self.rect.y += 6
        if pygame.key.get_pressed()[pygame.K_f] and self.cooldown > 0:
            self.cooldown -= 1
            print(self.cooldown)
        elif not pygame.key.get_pressed()[pygame.K_f] and self.cooldown != 0:
            self.cooldown = 120
        elif self.cooldown == 0:
            self.cooldown = 120
