import pygame 
import recurMaze
from random import randrange

pygame.init()


screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width,screen_height))

p1 = recurMaze.ParseMaze("recurMaze/maze.txt")
m1 = recurMaze.MazeSearch(p1.make_matrix()) 
pixel_positions = m1.make_traveled()

draw_scale = len(m1.maze[0]) # Draw scale is based on the length of the maze row 
# Screen scale is fit perfectly when the matrix is a square n x n matrix 

# Calling the solve_maze function and getting the path history 
solved = m1.solve_maze(2,2)

def draw_matrix(matrix): 
    x = 0 
    y = 0 
    width = screen_width // draw_scale 
    height = screen_height // draw_scale  
    for i, row in enumerate(matrix): 
        for j, char in enumerate(row): 
            if char == "P": 
                color = pygame.Color("White")
            elif char == "E": 
                color = pygame.Color("Green")  
            elif char == "W": 
                color = pygame.Color("Gray")

            bar = pygame.Rect(x, y, width, height)
            pygame.draw.rect(screen, color, bar, 0, 2) 
            pixel_positions[i][j] = (x,y)

            x += width
        x = 0 
        y += height

# History of the rat movements 
rat_history = []
def draw_rat(row, col): 
    
    get_pixel_position = pixel_positions[row][col]
    x = get_pixel_position[0] + (screen_width // draw_scale) // 4
    y = get_pixel_position[1] + (screen_height // draw_scale) // 4 
    rat_history.append((x,y))
    width = (screen_width // draw_scale) // 2
    height = (screen_height // draw_scale) // 2 



    color = pygame.Color("Black")

    bar = pygame.Rect(x, y, width, height) 
    pygame.draw.rect(screen, color, bar)


def draw_rat_history(history): 
    '''Marks the places the rat has visited'''
    color_vals = [0,0,0,255]
    for i, tup in enumerate(history): 
        x = tup[0] + (screen_height // draw_scale) // 6
        y = tup[1] + (screen_height // draw_scale) // 6 
        width = (screen_width // draw_scale) // 4
        height = (screen_height // draw_scale) // 4
    
        color = pygame.Color(color_vals)
        path = pygame.Rect(x,y, width, height)
        pygame.draw.rect(screen, color, path)

        # Just messing around with the color values 
        rand_index = randrange(0,4)
        color_vals[rand_index] = 255 
        for i in range(len(color_vals)): 
            if i != rand_index: 
                color_vals[i] = 0 

            
game_loop = True 

# The movement number increases each time draw_rat is called 
movement_num = 0 
while game_loop: 
    #color = pygame.Color("Red") 

    #bar = pygame.Rect(200, 300, 50, 100)
    #pygame.draw.rect(screen, color, bar)
    draw_matrix(p1.make_matrix())
    draw_rat(m1.stored_movements[movement_num][0], m1.stored_movements[movement_num][1])
    draw_rat_history(rat_history)

    pygame.display.flip()
    
    pygame.time.wait(100)
    if movement_num < len(m1.stored_movements) - 1:
        movement_num += 1 


    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            game_loop = False 

