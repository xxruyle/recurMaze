import recurMaze
import sys 
sys.setrecursionlimit(10000)

def main(): 
    g1 = recurMaze.Genmaze(150,150)
    g1.generate(1,1)
    m1 = recurMaze.MazeSearch(g1.visited) 
    m1.solve_maze(1,1) 

if __name__ == "__main__": 
    main()

    