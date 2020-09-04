class Solution:
    def cherryPickup(self, grid):
        maxres = 0
        def cherryPickUpUtil(grid, moves, source, destination, res):
            nonlocal maxres
            print("==========================", end="\n")
            print("SOURCE:", source, end="\n")
            if source == destination:
                (x, y) = source
                res += grid[x][y]
                grid[x][y] = 0
                if res > maxres:
                    maxres = res
                print("GRID:", grid, end="\n")
                return
            
            (x, y) = source
            print("GRID:", grid, end="\n")
            print("RES:", res, end="\n")
            res += grid[x][y]
            grid[x][y] = 0
            print("GRID:", grid, end="\n")
            print("RES:", res, end="\n")
            
            for move in moves:
                print("MOVE:", move, end="\n")  
                new = newSource(source, move)
                print("NEWSOURCE:", new, end="\n")
                if isValid(new, grid):
                    (x, y) = new
                    cherryPickUpUtil(grid, moves, new, destination, res)
            return maxres
        
        def newSource(source, move):
            return (source[0] + move[0], source[1] + move[1]) 
            
        def isValid(source, grid):
            (x, y) = source
            if x <0 or y < 0 or x >= len(grid) or y >= len(grid) or grid[x][y] < 0:
                return False
            return True
    
        moves = [(1, 0), (0, 1)]
        source = (0, 0)
        destination = (len(grid) -1, len(grid) -1)
        up = cherryPickUpUtil(grid, moves, source, destination, 0)
        print(up)
        
        print("**********************************************************************")
        print("**********************************************************************")
        print("**********************************************************************")
        print("**********************************************************************")
        
        maxres = 0
        moves = [(1, 0), (0, 1)]
        destination = (0, 0)
        source = (len(grid) -1, len(grid) -1)
        down = cherryPickUpUtil(grid, moves, source, destination, 0)
        print(down)
        return up+down

s = Solution()
# print(s.cherryPickup([[0,1,1,0,0],[1,1,1,1,0],[-1,1,1,1,-1],[0,1,1,1,0],[1,0,-1,0,0]]))
print(s.cherryPickup([[0,1,1,1],[0,0,0,1],[0,0,-1,1],[0,0,0,1]]))


def mid(t1, t2):
    [h1s, m1s] = t1.split(":")
    h1 = int(h1s)
    m1 = int(m1s)

    [h2s, m2s] = t2.split(":")
    h2 = int(h2s)
    m2 = int(m2s)

    if h1 >= h2:
        hourDiff = (h1 - h2)
        minuteDiff = 60 - m1 + m2
        totalDiff = hourDiff * 60 + minuteDiff

    