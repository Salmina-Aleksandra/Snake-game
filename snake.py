import time
from os import times
import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 102)
green = (0, 255, 0)

dis_width = 500
dis_height = 500

dis=pygame.display.set_mode((dis_width, dis_height)) #playing field size
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
snake_block = 10 #standard shift amount
snake_speed = 15 #speed limit
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35) #score game

def Your_score(score): #def of count score
    value = score_font.render("Your score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color): #def message for game display
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

def gameLoop(): #all game logic
    game_over = False #game status
    game_close = False
    x1 = dis_width / 2 #x-axis initial position
    y1 = dis_height / 2 #y-axis initial position
    x1_change = 0 #x-axis change
    y1_change = 0 #y-axis change
    snake_List = [] #current snake length
    Length_of_snake = 1
    foodX = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    #food location along the x-axis
    foodY = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    #food location along the y-axis
    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You lose! Press N to exit or Y to play again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_y:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #exit the game
                game_over = True
            if event.type == pygame.KEYDOWN: #keyboard directions
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
            game_close = True #obvious out-of-bounds
        x1 += x1_change #new position
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodX, foodY, snake_block, snake_block])
        snake_Head = [] #length of the snake when moving
        snake_Head.append(x1) #adding when changing along the x-axis
        snake_Head.append(y1) #adding when changing along the y-axis
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0] #removing the first element so that it does not increase on its own
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodX and y1 == foodY:
        #if the coordinates of the head coincide with the food then the food appears in a
        #new place and the snake grows larger
            foodX = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foodY = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()