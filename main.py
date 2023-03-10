import recurMaze
import game 
import sys 
sys.setrecursionlimit(10000)

def main(): 
    maze = game.Maze(32,32, 50, 50, show_generation=True, show_solve=True) 
    game = game.Game(32,32, 50, 50, show_generation=True, show_solve=True)

    game.run(0)

if __name__ == "__main__": 
    main()

    