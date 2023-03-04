import recurMaze

def main(): 
    p1 = recurMaze.ParseMaze("recurMaze/maze.txt")
    m1 = recurMaze.MazeSearch(p1.make_matrix()) 
    m1.solve_maze(0,0) 

if __name__ == "__main__": 
    main()