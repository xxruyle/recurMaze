import pygame 
import recurMaze
import sys 
sys.setrecursionlimit(30000)




class Maze: 
    '''Class for maze pygame'''
    def __init__(self, maze_rows, maze_cols, starting_row=1, starting_col=1, generation_algorithm="DFS", solving_algorithm="DFS", is_animated=True, draw_solve=True, shortest_path=True):  
        self.maze_rows = maze_rows
        self.maze_cols = maze_cols 
        self.starting_row = starting_row
        self.starting_col = starting_col
        self.generation_algorithm = generation_algorithm # The algorithm the program uses to generate the maze 
        self.solving_algorithm = solving_algorithm # The algorithm the program uses to solve the maze 
        self.is_animated = is_animated # Graphically shows the maze being generated  
        self.draw_solve = draw_solve  # Graphically shows the maze being solved 
        self.shortest_path = shortest_path # Graphically shows the maze's shortest path after being solved 
        self.generated_maze = None 
        self.solved_maze = None 


        self.generation_history = []
        self.solve_history = []


    def generate_solve(self): 
        '''Generates and solves the maze using class properties'''
        generator = recurMaze.Genmaze(self.maze_rows, self.maze_cols)

        # Generates the maze and places exit randomly
        generator.generate(self.starting_row, self.starting_col)
        generator.make_exit(generator.visited)
        self.generated_maze(generator.visited)

        solver = recurMaze.MazeSearch(generator.visited)
        self.pixel_positions = solver.make_traveled() # obtains a copy of the maze matrix, create_pixel_positions will add the corresponding pixel location to each element's index

        # Solves the maze
        self.solved_maze = solved.solve_maze(self.starting_row, self.starting_col)

    def run_maze(self): 
        pass 


class Game(Maze): 
    def __init__(self, maze_rows=32, maze_cols=32, generation_algorithm="DFS", solving_algorithm="DFS", is_animated=True, draw_solve=True, shortest_path=True): 
        super().__init__(maze_rows, maze_cols, generation_algorithm="DFS", solving_algorithm="DFS", is_animated=True, draw_solve=True, shortest_path=True)
        self.draw_scale = self.maze_rows 
        self.screen_width = (maze_rows * 5)  // self.draw_scale
        self.screen_height = (maze_cols * 5)  // self.draw_scale

        # The pixel positions corresponding to each element in the maze matrix
        self.pixel_positions = []

        self.loop = True  
        self.iteration = 0 # The iteration of each scucessive game loop increases by 1 

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, screen_height))
    
    def game_properties(self): 
        '''Loads the game data based on class properties'''
        # Generate and solve the matrix 
        self.generate_solve() 

        # Add the pixel positions to the obtained solved maze
        self.create_pixel_positions(self.solved_maze)

    def create_pixel_positions(self, maze): 
        '''Changes the value of each element in the maze to a corresponding pixel position'''
        x = 0 
        y = 0 
        for i, row in enumerate(maze): 
            for j, col in enumerate(row): 
                self.pixel_positions[i][j] = (x,y)
                x += self.screen_width

            x = 0 
            y += self.screen_height

    def draw_maze(self, maze): 
        '''Draw the maze''' 
        x = 0 
        y = 0 
        for i, row in enumerate(maze): 
            for j, char in enumerate(maze): 
                if char == 1: 
                    color = pygame.Color(239, 238, 235)
                elif char == "E": 
                    color = pygame.Color("Green")  
                elif char == 0: 
                    color = pygame.Color(92,86,56)

                bar = pygame.Rect(x, y, self.screen_width, self.screen_height)
                pygame.draw.rect(screen, color, bar) 

                x += self.screen_width
            x = 0 
            y += self.screen_height

    def get_solve_history(self): 
        pass 

    def get_generation_history(self): 
        pass 

    def draw_solving(self): 
        '''Draws the "rat" solving the maze'''

    def run(self, speed): 
        '''Runs the main game loop'''
        self.game_properties() 
        while self.loop: 
            draw_matrix(self.maze)

            pygame.time.wait(speed)

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.loop = False 


pygame.init()
maze_height = 100
maze_width = 100

screen_height = maze_height * 6
screen_width =  maze_width  * 6

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

            
#game_loop = True 
#
## The movement number increases each time draw_rat is called 
## The gen num increase each time draw_generation is called 
#gen_num = 0 
#gen_finished = True   
#movement_num = 0 
#while game_loop: 
#    # Draws the base grid with only the walls 
#
#    if not gen_finished: 
#        draw_generation(g1.stored_movements[gen_num][0], g1.stored_movements[gen_num][1])
#        draw_matrix(generation_stack)
#        if gen_num < len(g1.stored_movements) - 1:
#            gen_num += 1 
#        else: 
#            gen_finished = True 
#
#        
#
#    if gen_finished: 
#        draw_matrix(g1.visited)
#        draw_rat_history(rat_history)
#
#        draw_rat(m1.stored_movements[movement_num][0], m1.stored_movements[movement_num][1], m1.stored_movements[movement_num][2], m1.stored_movements[movement_num][3])
#
#        if movement_num < len(m1.stored_movements) - 1:
#            movement_num += 1 
#
#    
#
#    pygame.display.flip()
#    
#    pygame.time.wait(0)
#
#
#
#    for event in pygame.event.get(): 
#        if event.type == pygame.QUIT: 
#            game_loop = False 

