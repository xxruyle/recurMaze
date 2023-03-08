import pygame 
import recurMaze
import sys 
sys.setrecursionlimit(30000)




class Maze: 
    '''Class for maze pygame'''
    def __init__(self, maze_rows=32, maze_cols=32, starting_row=1, starting_col=1, generation_algorithm="DFS", solving_algorithm="DFS", is_animated=True, draw_solve=True, shortest_path=True):  
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
        self.generated_maze = generator.visited

        solver = recurMaze.MazeSearch(generator.visited)
        self.pixel_positions = solver.make_traveled() # obtains a copy of the maze matrix, create_pixel_positions will add the corresponding pixel location to each element's index

        # Solves the maze
        solver.solve_maze(self.starting_row, self.starting_col)
        self.solved_maze = solver.traveled

    def run_maze(self): 
        pass 


class Game(Maze): 
    def __init__(self, maze_rows=32, maze_cols=32, generation_algorithm="DFS", solving_algorithm="DFS", is_animated=True, draw_solve=True, shortest_path=True): 
        super().__init__(maze_rows, maze_cols, generation_algorithm="DFS", solving_algorithm="DFS", is_animated=True, draw_solve=True, shortest_path=True)
        self.draw_scale = 32
        self.screen_width = 1000 
        self.screen_height = 1000  

        # The pixel positions corresponding to each element in the maze matrix
        self.pixel_positions = []

        self.loop = True  
        self.iteration = 0 # The iteration of each scucessive game loop increases by 1 

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    
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
        width = self.screen_width // self.draw_scale
        height = self.screen_height // self.draw_scale
        for row in maze: 
            for char in row: 
                if char == 1: 
                    color = pygame.Color(239, 238, 235)
                elif char == "E": 
                    color = pygame.Color("Green")  
                elif char == 0: 
                    color = pygame.Color(92,86,56)

                bar = pygame.Rect(x, y, width, height)
                pygame.draw.rect(self.screen, color, bar) 

                x += width
            x = 0 
            y += height

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
            self.draw_maze(self.generated_maze)

            pygame.display.flip()
            pygame.time.wait(speed)
            

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.loop = False 

maze = Maze() 
game = Game()

game.run(1)