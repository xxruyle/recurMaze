class ParseMaze: 
    def __init__(self, file): 
        self.file = file 

    def make_matrix(self):  
        matrix = []
        file = open(self.file, 'r')
        for line in file: 
            row = []
            for char in line.strip(): 
                row.append(char)

            matrix.append(row)

        return matrix
    
    
class MazeSearch: 
    def __init__(self, maze): 
        self.maze = maze 
        self.traveled = self.make_traveled() # Traveled maze 
        self.stored_movements = []

    def make_traveled(self):  
        '''Returns the traveled maze from the maze member variable'''
        traveled = []
        for row in self.maze: 
            zero_row = [0] * len(row) 
            traveled.append(zero_row)

        return traveled 
    
    def pprint_matrix(self, matrix):  
        '''Prints the maze matrix in a prettier format''' 
        for row in matrix: 
            for char in row: 
                print(char, end=" ")
            print("\n")
        print("\n")
        
    def valid_move(self, row, col): 
        '''Returns true if the row, col corresponding to the 2d array is in range'''
        if (row >= 0 and row < len(self.maze)) and (col >= 0 and col < len(self.maze[row])): 
            if (self.maze[row][col] == 1 or self.maze[row][col] == "E") and (self.traveled[row][col] != 1 and self.traveled[row][col] != "X") : 
                return True 
            
    def check_exit(self, row, col): 
        '''Returns true if current position is at an exit''' 
        return self.maze[row][col] == "E"

    def mark(self, row, col, val): 
        '''Changes element in the traveled matrix to val corresponding to the row and col'''
        self.traveled[row][col] = val 

    def solve_maze(self, row, col): 
        '''Uses recursive backtracking to exhaustively search the maze for an exit, returns true if exit is found, false otherwise'''
        self.stored_movements.append((row, col, False))
        self.mark(row, col, 1)

        # Check for exit
        if self.check_exit(row, col): 
            self.mark(row,col, "V")
            return True 
        
        # Check Up 
        if self.valid_move(row-1, col): 
            if self.solve_maze(row-1, col): 
                return True 
        
        # Check Right 
        if self.valid_move(row, col+1): 
            if self.solve_maze(row, col+1): 
                return True 
        
        # Check Down 
        if self.valid_move(row+1, col): 
            if self.solve_maze(row+1, col): 
                return True 
            
        # Check Left
        if self.valid_move(row, col-1):
            if self.solve_maze(row, col-1): 
                return True 

        # If no valid move is found mark the position as an X and backtrack
        self.mark(row, col, "X")     
        self.stored_movements.append((row, col, True)) 
        return False 
    
