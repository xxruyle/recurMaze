import recurMaze

def main(): 
    g1 = recurMaze.Genmaze(32,32)
    g1.generate(1,1)
    m1 = recurMaze.MazeSearch(g1.visited) 
    m1.solve_maze(1,1) 
    print(m1.pprint_matrix(m1.traveled))
    print(m1.stored_movements)

if __name__ == "__main__": 
    main()