import pygame
import sys

# ракетка
class Paddle:
    def __init__(self, x):
        self.image = pygame.Surface((20, 70))  # изображение из поверхность
        self.image.fill((225, 225, 225))
        self.rect = self.image.get_rect()  # прямоугольник из изображения
        self.x = x
        self.y = 300  # TODO: поместить ракетку посередине высоты
        
# мяч
class Ball:
    pass


# счет
class Score:
    pass


# игра
class Game:
    def __init__(self):
    # подготовка
     self.player_1 = Paddle(100)


   def run(self):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Понг")

    while True:
        event = pg.event.get()  # собираем все событиям
    for event in event:  # проходим по всем событиям    
        if event.type == pg.QUIT:  # ловим событие выхода
            pg.quit()  # выгружает модули пайгейма из памяти
            sys.exit()  # выход из программы

        if event.type == pg.KEYDOWN:  # ловим нажатия клавиш
            if event.key == pg.K_ESCAPE:  # нажат эскейп
                pg.quit()
                sys.exit()


        #отрисовка
        
        screen.fill((0, 0, 0))
        # нарисовать ракетку
        pygame.display.flip()

# запуск игры
game = Game()
game.run()

