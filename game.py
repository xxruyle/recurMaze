import pygame 
import recurMaze
import sys 
sys.setrecursionlimit(30000)


pygame.init()
maze_height = 32
maze_width = 32

screen_height = maze_height * 15
screen_width =  maze_width * 15 

screen = pygame.display.set_mode((screen_width,screen_height))

g1 = recurMaze.Genmaze(maze_height,maze_width)

g1.generate(1,1)
g1.make_exit(g1.visited)


movements = g1.stored_movements
m1 = recurMaze.MazeSearch(g1.visited) 
pixel_positions = m1.make_traveled()

draw_scale = len(m1.maze[0]) # Draw scale is based on the length of the maze row 
# Screen scale is fit perfectly when the matrix is a square n x n matrix 

# Calling the solve_maze function and getting the path history 
solved = m1.solve_maze(1,1)
def create_pixel_positions(matrix): 
    x = 0
    y = 0
    width = screen_width // draw_scale 
    height = screen_height // draw_scale   
    for i, row in enumerate(matrix): 
        for j, char in enumerate(row): 
            pixel_positions[i][j] = (x,y)
            x += width

        x = 0 
        y += height

# Getting pixel positions 
create_pixel_positions(g1.visited)

def draw_matrix(matrix): 
    x = 0 
    y = 0 
    width = screen_width // draw_scale 
    height = screen_height // draw_scale  
    for i, row in enumerate(matrix): 
        for j, char in enumerate(row): 
            if char == 1: 
                color = pygame.Color(239, 238, 235)
            elif char == "E": 
                color = pygame.Color("Green")  
            elif char == 0: 
                color = pygame.Color(92,86,56)

            bar = pygame.Rect(x, y, width, height)
            pygame.draw.rect(screen, color, bar) 
            #pixel_positions[i][j] = (x,y)

            x += width
        x = 0 
        y += height




# History of the rat movements 
rat_history = []
def draw_rat(row, col, back_track, is_returning_home): 
    
    get_pixel_position = pixel_positions[row][col]
    x = get_pixel_position[0] #+ (screen_width // draw_scale) // 4
    y = get_pixel_position[1] #+ (screen_height // draw_scale) // 4
    rat_history.append((x,y, back_track, is_returning_home))
    width = (screen_width // draw_scale) #// 2
    height = (screen_height // draw_scale) #// 2 


    
    color = pygame.Color("RED")

    bar = pygame.Rect(x, y, width, height) 
    pygame.draw.rect(screen, color, bar)

generation_stack = g1.base_grid
def draw_generation(row, col): 
    g1.base_grid[row][col] = 1 


def draw_rat_history(history): 
    '''Marks the places the rat has visited'''
    for tup in history: 
        x = tup[0] #+ (screen_height // draw_scale) // 6
        y = tup[1] #+ (screen_height // draw_scale) // 6 
        back_track = tup[2]
        is_returning_home = tup[3]
        width = (screen_width // draw_scale) 
        height = (screen_height // draw_scale) 

        # If the movement is a backtrack move or not 
        if back_track: 
            color = pygame.Color(84, 196, 188) # Blue 
        elif is_returning_home: 
            color = pygame.Color("#4fd626")
        else: 
            color = pygame.Color(247, 80, 12) # Orange 
        path = pygame.Rect(x,y, width, height)
        pygame.draw.rect(screen, color, path)

        # Just messing around with the color values 
        #rand_index = randrange(0,4)
        #color_vals[rand_index] = 255 
        #for i in range(len(color_vals)): 
        #    if i != rand_index: 
        #        color_vals[i] = 0 

            
game_loop = True 

# The movement number increases each time draw_rat is called 
# The gen num increase each time draw_generation is called 
gen_num = 0 
gen_finished = False   
movement_num = 0 
while game_loop: 
    # Draws the base grid with only the walls 

    if not gen_finished: 
        draw_generation(g1.stored_movements[gen_num][0], g1.stored_movements[gen_num][1])
        draw_matrix(generation_stack)
        if gen_num < len(g1.stored_movements) - 1:
            gen_num += 1 
        else: 
            gen_finished = True 

        

    if gen_finished: 
        draw_matrix(g1.visited)
        draw_rat_history(rat_history)

        draw_rat(m1.stored_movements[movement_num][0], m1.stored_movements[movement_num][1], m1.stored_movements[movement_num][2], m1.stored_movements[movement_num][3])

        if movement_num < len(m1.stored_movements) - 1:
            movement_num += 1 

    

    pygame.display.flip()
    
    pygame.time.wait(10)



    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            game_loop = False 

