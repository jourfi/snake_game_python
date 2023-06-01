import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

screen_width = 600
screen_height = 400

dis = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game by DAKAEi')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [screen_width/6, screen_height/3])

def create_gradient_surface(start_color, stop_color, width, height):
    """
    Creates a gradient surface from the start color to the stop color 
    with the specified dimensions
    """
    gradient = pygame.Surface((width, height))
    color_rect = pygame.Rect(0, 0, width, height)
    pygame.draw.rect(gradient, start_color, color_rect)
    for i in range(height):
        color_rect = pygame.Rect(0, i, width, 1)
        r = start_color[0] + (i * (stop_color[0]-start_color[0])/height)
        g = start_color[1] + (i * (stop_color[1]-start_color[1])/height)
        b = start_color[2] + (i * (stop_color[2]-start_color[2])/height)
        color = (r, g, b)
        pygame.draw.rect(gradient, color, color_rect)
    return gradient

def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0       
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
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

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        if x1 == foodx and y1 == foody:
            # Create a gradient surface object
            gradient_surface = create_gradient_surface(black, white, screen_width, screen_height)
            # Draw the gradient surface to the screen
            dis.blit(gradient_surface, (0,0))
            pygame.display.update()
            # Wait for 2 seconds
            time.sleep(2)
            dis.fill(black)
            # Update the display to show the snake's head eating the food
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            pygame.display.update()
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        dis.fill(black)
        pygame.draw.circle(dis, red, [int(foodx)+int(snake_block/2), int(foody)+int(snake_block/2)], int(snake_block/2))

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for x in range(0, len(snake_List)):
            pygame.draw.rect(dis, white, [snake_List[x][0], snake_List[x][1], snake_block, snake_block])

        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()

