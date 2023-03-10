import pygame 
import recurMaze
import sys 
sys.setrecursionlimit(30000)


class Maze: 
    '''Class for generating and solving a maze and storing info and settings'''
    def __init__(self, maze_rows=32, maze_cols=32, starting_row=1, starting_col=1, show_generation=True, show_solve=True, shortest_path=True, generation_algorithm="DFS", solving_algorithm="DFS"):  
        self.maze_rows = maze_rows
        self.maze_cols = maze_cols 
        self.starting_row = starting_row
        self.starting_col = starting_col
        self.show_generation = show_generation # Graphically shows the maze being generated  
        self.show_solve = show_solve  # Graphically shows the maze being solved 
        self.shortest_path = shortest_path # Graphically shows the maze's shortest path after being solved 

        self.generation_algorithm = generation_algorithm # The algorithm the program uses to generate the maze 
        self.solving_algorithm = solving_algorithm # The algorithm the program uses to solve the maze 

        self.generated_maze = None # The generated maze 
        self.solved_maze = None # The solved maze 
        self.exit_position = None 

        self.generation_history = None # the generation history of the generator 
        self.solve_history = None # The solving history of the solver 

        self.base_grid = None # The base grid with only walls 


    def generate_solve(self): 
        '''Generates and solves the maze using class properties'''
        generator = recurMaze.Genmaze(self.maze_rows, self.maze_cols)

        # Generates the maze and places exit randomly
        generator.generate(self.starting_row, self.starting_col) 
        generator.make_exit(generator.visited)
        self.exit_position = generator.exit_position

        self.generated_maze = generator.visited

        
        self.generation_history = generator.stored_movements # Getting the history of the generation process 
        self.base_grid = generator.base_grid # The base grid with no walls 

        solver = recurMaze.MazeSearch(generator.visited)
        self.pixel_positions = solver.make_traveled() # obtains a copy of the maze matrix, create_pixel_positions will add the corresponding pixel location to each element's index

        
        solver.solve_maze(self.starting_row, self.starting_col) # Solves the maze
        self.solved_maze = solver.traveled # Storing the maze 
        self.solve_history = solver.stored_movements # Getting the history of the solving process 


class Game(Maze): 
    '''Class for game graphics'''
    def __init__(self, maze_rows=32, maze_cols=32, starting_row=1, starting_col=1, generation_algorithm="DFS", solving_algorithm="DFS", show_generation=True, show_solve=True, shortest_path=True): 
        super().__init__(maze_rows=maze_rows, maze_cols=maze_cols, starting_row=starting_row, starting_col=starting_col, generation_algorithm=generation_algorithm, solving_algorithm=solving_algorithm, show_generation=show_generation, show_solve=show_solve, shortest_path=shortest_path)

        self.draw_scale = self.maze_rows
        self.screen_width = self.maze_rows * 10
        self.screen_height = self.maze_cols * 10
        
        self.pixel_positions = [] # The pixel positions corresponding to each element in the maze matrix

        self.solve_path = [] # The path of the solver up to a point 

        self.loop = True  # Game loop variable

        self.gen_iteration = 0 # The generation iteration for each successive game loop increases by 1 
        self.iteration = 0 # The iteration of each scucessive game loop increases by 1 

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
    
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
                x += self.screen_width // self.draw_scale

            x = 0 
            y += self.screen_height // self.draw_scale

    def draw_maze(self, maze): 
        '''Draw the maze''' 
        x = 0 
        y = 0 
        for row in maze: 
            for char in row: 
                if char == 1: 
                    color = pygame.Color(239, 238, 235)
                elif char == "E": 
                    color = pygame.Color("Green")  
                elif char == 0: 
                    color = pygame.Color(92,86,56)


                bar = pygame.Rect(x, y, self.screen_width // self.draw_scale, self.screen_height // self.draw_scale)
                pygame.draw.rect(self.screen, color, bar) 

                x += self.screen_width // self.draw_scale
            x = 0 
            y += self.screen_height // self.draw_scale 

    def draw_generation(self): 
        '''Draws the generation process of the maze''' 
        self.path = self.generation_history[:self.gen_iteration] 
        for tup in self.path: 
            row = tup[0]
            col = tup[1] 

            get_pixel_position = self.pixel_positions[row][col]

            x = get_pixel_position[0]
            y = get_pixel_position[1]

            color = pygame.Color("White")
            square = pygame.Rect(x,y,self.screen_width // self.draw_scale,self.screen_height // self.draw_scale)
            pygame.draw.rect(self.screen, color, square)


    def draw_solve_path(self): 
        '''Instantly draws the solving process of the solver''' 
        
        for tup in self.solve_history: 
            row = tup[0]
            col = tup[1]
            
            is_backtracking = tup[2] # If the solver has found a dead end and is backtracking
            is_post_solve = tup[3] # If the solver has found the exit and is returning home and making shortest path


            get_pixel_position = self.pixel_positions[row][col]

            x = get_pixel_position[0]
            y = get_pixel_position[1]

            if is_backtracking: 
                color = pygame.Color(84, 196, 188) # Light Blue 
            elif is_post_solve: 
                if tup[0] == self.starting_row and tup[1]  == self.starting_col: # If it is the starting position
                    color = pygame.Color("Red")
                elif tup[0] == self.exit_position[0] and tup[1] == self.exit_position[1]: # If it is the ending position
                    color = pygame.Color("#D65D0E")
                else: 
                    color = pygame.Color("#4fd626") # Green 
            else: 
                color = pygame.Color(247, 80, 12) # Orange 

            square = pygame.Rect(x,y, self.screen_width // self.draw_scale, self.screen_height // self.draw_scale) 
            pygame.draw.rect(self.screen, color, square)





    def draw_solve_history(self): 
        '''Draws the "rat" solving the maze'''
        self.path = self.solve_history[:self.iteration]
        for tup in self.path: 
            row = tup[0]
            col = tup[1]
            
            is_backtracking = tup[2] # If the solver has found a dead end and is backtracking
            is_post_solve = tup[3] # If the solver has found the exit and is returning home and making shortest path


            get_pixel_position = self.pixel_positions[row][col]

            x = get_pixel_position[0]
            y = get_pixel_position[1]

            if is_backtracking: 
                color = pygame.Color(84, 196, 188) # Light Blue 
            elif is_post_solve:
                if tup[0] == self.starting_row and tup[1]  == self.starting_col: # If it is the starting position
                    color = pygame.Color("Red")
                elif tup[0] == self.exit_position[0] and tup[1] == self.exit_position[1]: # If it is the ending position
                    color = pygame.Color("#D65D0E")
                else: 
                    color = pygame.Color("#4fd626") # Green 
            else: 
                color = pygame.Color(247, 80, 12) # Orange 

            

            square = pygame.Rect(x,y, self.screen_width // self.draw_scale, self.screen_height // self.draw_scale) 
            pygame.draw.rect(self.screen, color, square)
        


    def run(self, speed): 
        '''Runs the main game loop'''
        self.game_properties() 
        while self.loop: 
            if self.show_generation and self.gen_iteration < len(self.generation_history): 
                self.draw_maze(self.base_grid)
                self.draw_generation()
                self.gen_iteration += 1 
            else: 
                self.show_generation = False 

            if not self.show_generation and self.show_solve: # If the generation has completed or self.is_animated was false from the start
                self.draw_maze(self.generated_maze)
                self.draw_solve_history()
                self.iteration += 1 

            if not self.show_generation and not self.show_solve: 
                self.draw_maze(self.generated_maze)
                self.draw_solve_path()


            pygame.display.flip()
            pygame.time.wait(speed)


            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.loop = False 


    