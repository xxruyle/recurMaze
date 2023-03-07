import random 

class Genmaze: 
    '''
    Generates a maze
    1 = passageway 
    0 = wall 
    2 = outer walls 
    "E" = Exit 
    ''' 
    def __init__(self, rows, cols): 
        self.rows = rows 
        self.cols = cols  
        self.visited  = self.grid_matrix()  
        self.base_grid = self.grid_matrix()
        self.stored_movements = []

    def pprint_matrix(self, matrix):  
        '''Prints the maze matrix in a prettier format''' 
        for row in matrix: 
            for char in row: 
                print(char, end=" ")
            print("\n")
        print("\n")

    def grid_matrix(self): 
        '''Makes a standard matrix of only walls where 0 represents walls and chooses a random exit point'''
        matrix = []
        for i in range(self.rows): 
            row = []
            for j in range(self.cols): 
                row.append(0)

            matrix.append(row)


        return matrix

    def is_valid_move(self, row, col): 
        if (row >= 0 and row < len(self.visited)) and (col >= 0 and col < len(self.visited[row])): 
            return True 

    def is_visited(self, row, col): 
        '''Checks to see if a given row or col is visited nearby'''
        return self.visited[row][col] == 1

    def mark_visited(self, row, col): 
        self.visited[row][col] = 1 

    
    def check_surrounding(self, row, col): 
        '''Given a row and col, check surroundings to see what is valid move''' 
        valid_moves = []
        # Check Up 
        if self.is_valid_move(row-2, col): 
            if not self.is_visited(row-2,col): 
                valid_moves.append("U")
        
        # Check Right 
        if self.is_valid_move(row, col+2):
            if not self.is_visited(row, col+2): 
                valid_moves.append("R")
        
        # Check Down
        if self.is_valid_move(row+2, col): 
            if not self.is_visited(row+2, col): 
                valid_moves.append("D")

        # Check Right 
        if self.is_valid_move(row, col-2): 
            if not self.is_visited(row, col-2): 
                valid_moves.append("L")

        return valid_moves


    def random_move(self, row, col): 
        '''Returns a random move based on row col position, returns tuple of row and col movement'''
        moves = self.check_surrounding(row, col)

        # If there are no available moves
        if not moves: 
            return False 
        
        move_choice = random.choice(moves)
        make_move = []
        # Move Up 
        if move_choice == "U":
            make_move.append(row - 2) 
            make_move.append(col) 
            self.mark_visited(row-1, col)
            self.stored_movements.append((row-1, col))
        # Move Right 
        elif move_choice == "R": 
            make_move.append(row)
            make_move.append(col+2)
            self.mark_visited(row, col+1)
            self.stored_movements.append((row, col+1))
        # Move Down 
        elif move_choice == "D": 
            make_move.append(row+2)
            make_move.append(col)
            self.mark_visited(row+1, col)
            self.stored_movements.append((row+1, col))
        # Move Left 
        elif move_choice == "L": 
            make_move.append(row)
            make_move.append(col-2) 
            self.mark_visited(row,col-1)
            self.stored_movements.append((row, col-1))
        return make_move  

    def convert_matrix_to_string(self, matrix): 
        for row in matrix: 
            row_string = ""
            for element in row: 
                row_string += str(element)
            print(row_string) 


    def generate(self, row, col):
        '''Generates a maze at a specific row, col starting point'''
        self.mark_visited(row, col)
        self.stored_movements.append((row,col))
        moves = self.check_surrounding(row, col) 
        while moves: 
            row_col_move = self.random_move(row, col) 
            if row_col_move: 
                if self.generate(row_col_move[0], row_col_move[1]): 
                    return True 
                else: 
                    if row_col_move in moves: 
                        moves.remove(row_col_move) 
            else: 
                break
        
        
        return False 
    
    def make_exit(self, matrix): 
        '''Give an exit to a given maze'''
        found = False 
        while not found: 
            rand_row = random.randrange(0, len(matrix) - 1)
            rand_col = random.randrange(0, len(matrix[rand_row]) - 1) 
            if matrix[rand_row][rand_col] == 1: 
                found = True 

        matrix[rand_row][rand_col] = "E" 

        

        



