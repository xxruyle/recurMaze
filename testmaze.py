class Maze:
    '''Depth First Search Maze Path Finding'''
    def __init__(self, maze): 
        self.maze = maze 
        self.traveled = self.make_grid(maze)
        self.current = 0 

    def make_grid(self, matrix):  
        grid = []
        for row in matrix: 
            new_row = []
            for j in row: 
                if j == "P": 
                    new_row.append(" ")
                elif j == "W": 
                    new_row.append("W")
                elif j == "E": 
                    new_row.append("E")
            grid.append(new_row)

        return grid 

    def print_maze(self, matrix): 
        for i, row in enumerate(matrix): 
            for j in range(len(row)): 
                print(self.traveled[i][j], end=" ")
            print("\n")

        print("---------------------")

maze = [
    ["W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "P", "P", "P", "P", "P", "P", "W"], 
    ["W", "W", "P", "W", "P", "W", "P", "W"],
    ["W", "W", "P", "W", "P", "W", "W", "W"],
    ["W", "W", "P", "P", "P", "P", "P", "W"],
    ["P", "P", "P", "W", "P", "W", "W", "W"],
    ["E", "W", "P", "W", "P", "P", "P", "W"],
    ["W", "W", "W", "W", "W", "W", "P", "W"],
    ["W", "W", "P", "P", "P", "P", "P", "W"],
    ["W", "W", "W", "W", "W", "P", "W", "W"]
]

m1 = Maze(maze) 



def solve_maze(x,y): 
    if maze[y][x] == "E": 
        m1.traveled[y][x] = "V"
        m1.print_maze(m1.traveled)
        return True 

    m1.print_maze(m1.traveled)

    # Checking UP 
    if y-1 >= 0: 
        if (maze[y-1][x] == "P" or maze[y-1][x] == "E") and m1.traveled[y-1][x] != 1 and m1.traveled[y-1][x] != "X": 
            m1.traveled[y-1][x] = 1
            if solve_maze(x,y-1): 
                return True 
            else: 
                m1.print_maze(m1.traveled)
                print(y,x)

    # Checking RIGHT 
    if x+1 < len(maze[y]): 
        if (maze[y][x+1] == "P" or maze[y][x+1] == "E") and m1.traveled[y][x+1] != 1 and m1.traveled[y][x+1] != "X": 
            m1.traveled[y][x+1] = 1
            if solve_maze(x+1,y): 
                return True 
            else: 
                m1.print_maze(m1.traveled)
                print(y,x)
    # Checking DOWN 
    if y+1 < len(maze): 
        if (maze[y+1][x] == "P" or maze[y+1][x] == "E") and m1.traveled[y+1][x] != 1 and m1.traveled[y+1][x] != "X": 
            m1.traveled[y+1][x] = 1
            if solve_maze(x,y+1):
                return True 
            else: 
                m1.print_maze(m1.traveled)
                print(y,x)
    # Checking LEFT 
    if x-1 >= 0: 
        if (maze[y][x-1] == "P" or maze[y][x-1] == "E") and m1.traveled[y][x-1] != 1 and m1.traveled[y][x-1] != "X": 
            m1.traveled[y][x-1] = 1 
            if solve_maze(x-1,y): 
                return True 
            else: 
                m1.print_maze(m1.traveled)
                print(y,x)

    # If no correct option is found 
    m1.traveled[y][x] = "X"
    return False 

if solve_maze(0,5): 
    print("Exit was found!")
else: 
    print("No exit could be found!")


