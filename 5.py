import os
import pygame
import random

size = width, height = 824, 400
screen = pygame.display.set_mode(size)
screen_rect = (0, 0, 824, 400)


def load_image(name, color_key=None):
    fullname = os.path.join(name)
    image = pygame.image.load(fullname).convert()

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def start_screen():
    intro_text = [
        "Правила игры:",
        "цель этой игры -это  собирать подарки.",
        "Подарки будут падать сверху."
        "Игрок должен собрать их,",
        "управляя ноогодним мешком,",
        "При этом если вы потеряете 5 жизней - погибните, ",
        "За каждые 2 пропущенных подарка снимается 1 жизнь."
        "",
        "Для управления направлением движения",
        "нужно нажимать на соответствующие кнопки-стрелки",
        "",
        "Для того чтобы начать игру, нажать любую клавишу"
    ]
    fon = pygame.transform.scale(load_image('start_image.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()  # выход
            elif event.type == pygame.KEYDOWN:
                return  # начало игры
        pygame.display.flip()
        clock.tick(fps)


class Gift(pygame.sprite.Sprite):
    image = load_image("1.png", -1)
    image = pygame.transform.scale(image, (70, 70))

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite
        super().__init__(group)
        self.image = Gift.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        self.rect.y += 1
        if not self.rect.colliderect(screen_rect):
            self.kill()


class Meshok(pygame.sprite.Sprite):
    image = load_image("2.png", -1)

    def __init__(self):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite
        super().__init__(player_sprites)
        self.image = Meshok.image
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 230

    def update(self, x):
        self.rect.x += x


# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()
Gift(all_sprites)

clock = pygame.time.Clock()
pygame.init()
fon = pygame.image.load('fon.jpg')
screen.blit(fon, (0, 0))
pygame.display.set_caption('Реакция на события от мыши')
running = True
x_pos = 0
v = 20  # пикселей в секунду
fps = 60
player_sprites = pygame.sprite.Group()
player = Meshok()
start_screen()
while running:
    step = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if player.rect.x - 1 >= 0:
                    step = -20
            if event.key == pygame.K_RIGHT:
                if player.rect.x + 1 <= width:
                    step = 20
    screen.fill('black')
    screen.blit(fon, (0, 0))
    all_sprites.draw(screen)
    player_sprites.draw(screen)
    player_sprites.update(step)
    all_sprites.update()
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
