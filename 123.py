import pygame as pg
import sys
# все про экран
pg.init()  # инициализация всех модулей пайгейма
SCREEN_WIDTH = 800  # ширина экрана
SCREEN_HEIGHT = 600  # высота экрана
PLAYER_COLOR = (225, 255, 255,)  #  цвет игрока
SCREEN_COLOR = (0, 0, 0)  # цвет экрана 
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # задали размер экрана

# игрок

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
player = pg.Rect(0, 0, 50, 50)  # прямоугольник-игрок, х и у, ширина и высота
player_x = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
player_y = SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2
player = pg.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT) 

while True:  # главный цикл программы  
   
    # работа с событиями
    event = pg.event.get()  # собираем все событиям
    for event in event:  # проходим по всем событиям    
        if event.type == pg.QUIT:  # ловим событие выхода
            pg.quit()  # выгружает модули пайгейма из памяти
            sys.exit()  # выход из программы

        if event.type == pg.KEYDOWN:  # ловим нажатия клавиш
            if event.key == pg.K_ESCAPE:  # нажат эскейп
                pg.quit()
                sys.exit()


            if event.key == pg.K_RIGHT:  # игрок идет вправо
                player.x += 5

            if event.key == pg.K_LEFT:  # игрок идет влево
                player.x -= 5 

            if event.key == pg.K_UP:  # игрок идет вверх
                player.y -= 5

            if event.key == pg.K_DOWN:  # игрок идет вниз
                player.y += 5


    screen.fill(SCREEN_COLOR)  # заливаем весь экран чёрным 
    pg.draw.rect(screen, PLAYER_COLOR, player)  # рисуем игрока
    pg.display.flip()  # обновляем экран