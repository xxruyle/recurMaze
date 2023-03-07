import random 

class Genmaze: 
    '''Generates a maze''' 
    def __init__(self, rows, cols): 
        self.rows = rows 
        self.cols = cols  
        self.base_grid = self.grid_matrix()
        self.visited  = self.grid_matrix()  

    def pprint_matrix(self, matrix):  
        '''Prints the maze matrix in a prettier format''' 
        for row in matrix: 
            for char in row: 
                print(char, end=" ")
            print("\n")
        print("\n")

    def grid_matrix(self): 
        '''Makes a standard matrix of only walls where 0 represents walls'''
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
                valid_moves.append(row-2)
                valid_moves.append(col)
        
        # Check Right 
        if self.is_valid_move(row, col+2):
            if not self.is_visited(row, col+2): 
                valid_moves.append(row)
                valid_moves.append(col+2)
        
        # Check Down
        if self.is_valid_move(row+2, col): 
            if not self.is_visited(row+2, col): 
                valid_moves.append(row+2)
                valid_moves.append(col)

        if self.is_valid_move(row, col-2): 
            if not self.is_visited(row, col-2): 
                valid_moves.append(row)
                valid_moves.append(col-2)

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
        # Move Right 
        elif move_choice == "R": 
            make_move.append(row)
            make_move.append(col+2)
            self.mark_visited(row, col+1)
        # Move Down 
        elif move_choice == "D": 
            make_move.append(row+2)
            make_move.append(col)
            self.mark_visited(row+1, col)
        # Move Left 
        elif move_choice == "L": 
            make_move.append(row)
            make_move.append(col-2) 
            self.mark_visited(row,col-1)
        return make_move  


    def generate(self, row, col):
        '''Generates a maze at a specific row, col starting point'''
        self.mark_visited(row, col)
        self.pprint_matrix(self.visited)
        row_col_move = self.random_move(row, col) 
        if row_col_move: 
            if self.generate(row_col_move[0], row_col_move[1]): 
                return True 
            
        
        
        return False 

        




g1 = Genmaze(8,8)
g1.generate(0,0)