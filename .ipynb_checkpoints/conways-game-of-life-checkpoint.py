import pygame
import sys
import time
import numpy as np
import algorithm # Conway's Game, matrix updating function

pygame.init()


# Screen setup
info = pygame.display.Info()
dim_x = info.current_w
dim_y = info.current_h
screen = pygame.display.set_mode((dim_x, dim_y))
pygame.display.set_caption('Conway\'s Game of Life')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Font and text
font = pygame.font.Font(None, 36)
start_text = font.render("START", True, GREEN)
stop_text = font.render("STOP", True, RED)

# Game settings
game_arr = np.zeros((100, 200)) # Initial game array
game_arr[50][100:103] = 1 # Initial alive squares
game_arr[51][101] = 1
origional_game_arr = np.copy(game_arr)


# Game state and controls
playing = False
display_boundries = (dim_x, dim_y)
timer_interval = 1000  # 1000 milliseconds = 1 second
previous_time = pygame.time.get_ticks()

# Button and text coordinates
y_ = dim_y / 30
button_top, button_bottom, button_left, button_right = y_, 3*y_, y_, 3*y_
play_button_coords = [(button_top, button_left), (button_left, button_bottom), (button_right, (button_top+button_bottom)/2)]
rect_width, rect_height = 200, 100
start_stop_coords = (button_left, button_top+button_bottom)


    
    
def draw_square(i, j, game_arr, display_boundries):
    boundry_x_len, boundry_y_len = display_boundries
    game_x_len = np.shape(game_arr)[1]
    game_y_len = np.shape(game_arr)[0]
        
    size_x = boundry_x_len / game_x_len
    size_y = boundry_y_len / game_y_len
    
    x = size_x * j
    y = size_y * i
    
    pygame.draw.rect(screen, WHITE, (x, y, size_x, size_y))
    
    
def draw_game(game_arr, display_boundries):
    for i in range(len(game_arr)):
        for j in range(len(game_arr[0])):
            if game_arr[i][j]:
                draw_square(i, j, game_arr, display_boundries)
                
def change_grid(game_arr, mouse_x, mouse_y):
    # Take mouse_x and mouse_y and scale them onto the game board
    # Update that specific coordinate to inverse of what it is currently
    
    
    return game_arr


# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_left < mouse_x < button_right and button_top < mouse_y < button_bottom:
                if not playing:
                    playing = True
                else:
                    playing = False
            else: # User has clicked on a square to be killed or alive
                game_arr = change_grid(game_arr, mouse_x, mouse_y)
            
            
    screen.fill(BLACK)

    
    
    
   
    if not playing:
        game_arr = origional_game_arr
        draw_game(game_arr, display_boundries)
        pygame.draw.polygon(screen, GREEN, play_button_coords) 
        screen.blit(start_text, start_stop_coords)
        
    if playing:
        draw_game(game_arr, display_boundries)
        
        pygame.draw.rect(screen, RED, (button_left, button_top, button_right-button_left, button_bottom-button_top)) 
        screen.blit(stop_text, start_stop_coords)
        
        
        
        
                
        # Calculate elapsed time
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - previous_time
        if elapsed_time >= timer_interval:
            # Update game array
            previous_time = current_time
            game_arr = algorithm.update_grid(game_arr)
        
        
    
    
    
    
    
    # Final updates
    pygame.display.flip() # Update the display
    pygame.time.Clock().tick(60)  # Cap at 60 frames per second
    
    

# Quit Pygame
pygame.quit()