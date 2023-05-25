# import pygame
# from pygame.locals import *
# import time
# import random



# pygame.init()
# red = (255,0,0)
# blue = (51,153,255)
# grey = (192,192,192)
# green = (51,102,0)
# yellow = (0,255.255)


# width = 600
# height = 400
# window = pygame.display.set_mode((width,height)) #window has been created
# # time.sleep(5)
# pygame.display.set_caption("Snake Game") #title for the window

# #game variables
# snake = 10
# snake_speed = 15

# clock = pygame.time.Clock()



# # fonts
# font_style = pygame.font.SysFont("calibri",26)
# score_font = pygame.font.SysFont("comicsansms",30)
# # fonts = pygame.font.get_fonts()
# # print(fonts)

# def user_score(score):
#     number = score_font.render("Score :",str(score),True,red)
#     window.blit(number,[0,0])


# def game_snake(snake,snake_length_list):
#     for x in snake_length_list:
#         pygame.draw.rect(window,green,[x[0],x[1],snake,snake])
    

# def message(msg):
#     msg = font_style.render(msg,True,red)
#     window.blit(msg,[width/6,height/3])


# def game_loop():
#     gameOver = False
#     gameClose = False



#     x1 = width/2
#     y1 = height/2

#     x1_change = 0
#     y1_change = 0

#     snake_length_list = []
#     snake_length = 1


#     foodx = round(random.randrange(0,width - snake)/10.0)*10.0
#     foody = round(random.randrange(0,height - snake)/10.0) * 10.0

#     while not gameOver:

#         while gameClose == True:
#             window.fill(grey)
#             message("you lost the game,Press P to play again and Q to quit")
#             user_score(snake_length-1)
#             pygame.display.update()


#             for event in pygame.event.get():
#                 if event.type ==  pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         gameOver = True
#                         gameClose = True
#                     if event.key == pygame.K_p:
#                         game_loop()

#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == K_LEFT:
#                         x1_change = -snake
#                         y1_change = 0
#                     if event.key == K_RIGHT:
#                         x1_change = snake
#                         y1_change = 0
#                     if event.key == K_UP:
#                         x1_change = 0
#                         y1_change = -snake
#                     if event.key == K_DOWN:
#                         x1_change = 0
#                         y1_change = snake
                    

#         if x1 > width or x1<0 or y1>height or y1<0:
#             gameOver = True
        
#         x1 += x1_change
#         y1 += y1_change

#         window.fill(grey)
#         pygame.draw.rect(window,red,[foodx,foody,snake,snake])
#         snake_size = []

#         snake_size.append(x1)
#         snake_size.append(y1)

#         snake_length_list.append(snake_size)

#         if len(snake_length_list)>snake_length:
#             del snake_length_list[0]


#         game_snake(snake,snake_length_list)
#         user_score(snake_length-1)


#         pygame.display.update()

#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0,width - snake)/10.0)*10.0
#             foody = round(random.randrange(0,height - snake)/10.0) * 10.0
#             snake_length += 1

#         clock.tick(snake_speed)

#     pygame.quit()
#     quit()


# game_loop()

import pygame
import time
import random

pygame.init()

# load images
# bg = pygame.image.load("snake.jpg")

black = (0,0,0)
white = (255,255,255)
green = (41,240,26)
red = (201, 18, 18)
yellow = (239,250,32)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake game")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("calibri",25)
score_font = pygame.font.SysFont("comicsans",34)
# print(pygame.font.get_fonts())

def my_score(score):
    value = score_font.render("Score: "+str(score),True,yellow)
    dis.blit(value, [0,0])

def message(msg,color):
    mssg = font_style.render(msg,True,color)
    dis.blit(mssg,[100,dis_height/3])


def my_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,green,[x[0],x[1],snake_block,snake_block])



def main_game():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    snake_list =[]
    length_snake = 1

    foodx = round(random.randrange(0,dis_width- snake_block)/10.0)*10.0
    foody = round(random.randrange(0,dis_height-snake_block)/10.0)*10.0

    while not game_over:

        # dis.blit(bg,(0,0))
        while game_close == True:
            dis.fill(white)
            message("You lost! press p to play again q to quit",red)
            my_score(length_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        main_game()

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
                    x1_change = 0
                    y1_change = -snake_block

                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        pygame.draw.rect(dis,red, [foodx,foody,snake_block,snake_block] )
        snake_size = []
        snake_size.append(x1)
        snake_size.append(y1)
        snake_list.append(snake_size)
        if len(snake_list) > length_snake:
            del snake_list[0]

        my_snake(snake_block,snake_list)
        my_score(length_snake - 1)

        pygame.display.update()


        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width-snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height-snake_block) / 10.0) * 10.0
            length_snake +=1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

main_game()













































