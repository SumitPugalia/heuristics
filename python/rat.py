def path(maze):
    source = (0, 0)
    destination = (len(maze) - 1, len(maze[0]) - 1)
    visited = {}
    sol = []
    res = []
    sol.append(source)
    return recursePath(maze, source, destination, sol, res, visited)

def recursePath(maze, source, destination, sol, res, visited):
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if source == destination:
        res.append(sol)
        print(res)
    else:
    
    
        for i in range(len(moves)):
            (valid, n) = validateMove(maze, source, moves[i], visited)
            if valid:
                visited[n] = True
                sol.append(n)
                recursePath(maze, n, destination, sol, res, visited)
                    # return res
                sol.pop()
    return False

def validateMove(maze, source, move, visited):
    n = (source[0] + move[0], source[1] + move[1])
    if n[0] < 0 or n[1] < 0 or n[0] >= len(maze) or n[1] >= len(maze[0]):
        return (False, source)
    print(n)
    if maze[n[0]][n[1]] and (n not in visited):
        return(True, n)
    
    return(False, source)

if __name__ == "__main__": 
    # Initialising the maze 
    maze = [ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [1, 1, 0, 0], 
             [0, 1, 1, 1],
             [0, 0, 0, 1] ] 
    print(path(maze))