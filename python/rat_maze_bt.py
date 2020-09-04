def solveMaze(maze, source, destination, sol):
    moves = [(1, 0), (0, 1)]
    if source == destination:
        print("I reached")
        print(sol)
        return True
    
    for i in range(len(moves)):
        if source[0] + moves[i][0] < len(maze[0]) and source[1] + moves[i][1] < len(maze):
            n = (source[0] + moves[i][0], source[1] + moves[i][1])
            print(source)
            if maze[n[0]][n[1]]:
                # maze[n[0]][n[1]] = 'x'
                sol[n[0]][n[1]] = 1
                if solveMaze(maze, n, destination, sol):
                    return True
                # maze[n[0]][n[1]] = 1
    return False

if __name__ == "__main__": 
    # Initialising the maze 
    maze = [ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [0, 1, 0, 0], 
             [1, 1, 1, 1] ] 
    sol = [[1,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    solveMaze(maze, (0, 0), (3, 3), sol) 