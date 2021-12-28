import pygame
import os

pygame.init()
clock = pygame.time.Clock()
FPS = 60
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
screen_rect = (0, 0, 500, 500)


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
        clock.tick(FPS)


start_screen()