import pygame
import time
import random
 
pygame.init()

#colores

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
darkblue = (0,0,255)

#Colores para bordes
color_arriba = darkblue
color_abajo = darkblue
color_derecha = darkblue
color_izquierda = darkblue

 
#pantalla
pantalla_ancho = 800
pantalla_largo = 600

 
pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_largo))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()
 
#snake
snake_block = 10
snake_speed = 15

snake2_block = 10
snake2_speed = 15
 
font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("arial", 35)
 
score = 0 

def puntuacion(score):
    value = score_font.render("Tu puntuación: " + str(score), True, yellow)
    pantalla.blit(value, [270, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(pantalla, black, [x[0], x[1], snake_block, snake_block])
        
def our_snake2(snake2_block, snake2_list):
    for x in snake2_list:
        pygame.draw.rect(pantalla, white, [x[0], x[1], snake2_block, snake2_block])
        
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    pantalla.blit(mesg, [200, 150])

#bordes
arriba= 0
abajo = pantalla_largo
derecha = pantalla_ancho
izquierda = 0
borde_arriba = 0
 
 #Bucle del juego
def gameLoop(arriba,abajo,izquierda, derecha):
    game_over = False
    game_close = False
 
    x1 = 400
    y1 = 300
 
    x1_change = 0
    y1_change = 0
 
    snake_cola = []
    snake_longitud = 1
 
    comidax = round(random.randrange(izquierda, derecha - snake_block) / 10.0) * 10.0
    comiday = round(random.randrange(arriba, abajo - snake_block) / 10.0) * 10.0

    comidaa = round(random.randrange(izquierda, derecha - snake_block) / 10.0) * 10.0
    comidab = round(random.randrange(arriba, abajo - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            pantalla.fill(blue)
            message("Perdiste! Pulsa C para jugar o Q para salir", red)
            puntuacion(snake_longitud - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= pantalla_ancho or x1 < 0 or y1 >= pantalla_largo or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        if y1 >= abajo:
            y1 = arriba
        if y1 < arriba:
            y1 = abajo - snake_block
        if x1 >= derecha:
            x1 = izquierda
        if x1 < izquierda:
            x1 = derecha - snake_block

        pantalla.fill(blue)
        pygame.draw.rect(pantalla, green, [comidax, comiday, snake_block, snake_block])
        pygame.draw.rect(pantalla, red, [comidaa, comidab, snake_block, snake_block])
        pygame.draw.rect(pantalla, color_arriba, [izquierda,arriba,derecha-izquierda,snake_block]) # borde de arriba
        pygame.draw.rect(pantalla, color_abajo, [izquierda,abajo-snake_block,derecha-izquierda,snake_block]) # borde de abajo
        pygame.draw.rect(pantalla, color_izquierda, [izquierda,arriba,snake_block,abajo-arriba]) # borde de la izquierda
        pygame.draw.rect(pantalla, color_derecha, [derecha-snake_block,arriba,snake_block,abajo-arriba]) # borde de la derecha
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_cola.append(snake_Head)
        if len(snake_cola) > snake_longitud:
            del snake_cola[0]
 
        for x in snake_cola[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_cola)
        puntuacion(snake_longitud -1)
 
        pygame.display.update()
 
        if x1 + snake_block >= comidaa and x1 < comidaa + snake_block and y1 + snake_block >= comidab and y1 < comidab + snake_block:
            comidaa = round(random.randrange(izquierda, derecha - snake_block) / 10.0) * 10.0
            comidab = round(random.randrange(arriba, abajo - snake_block) / 10.0) * 10.0
            snake_longitud += 24
            arriba += 24
            izquierda += 24
            abajo -= 24
            derecha -= 24
            
        if x1 + snake_block >= comidax and x1 < comidax + snake_block and y1 + snake_block >= comiday and y1 < comiday + snake_block:
            comidax = round(random.randrange(izquierda, derecha - snake_block) / 10.0) * 10.0
            comiday = round(random.randrange(arriba, abajo - snake_block) / 10.0) * 10.0
            snake_longitud += 1

 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop(arriba,abajo,izquierda,derecha)