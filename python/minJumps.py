#minJumps(start, end) = min{minJumps(k, end)} where k is all possible reachable points
def minJumps(arr, start, end):
    # BASE CASE
    if start >= end:
        return 0

    if arr[start] == 0:
        return float('inf')

    minimumJump = float('inf')
    # ALL POSSIBLE STATES REACHABLE
    for k in range(start + 1, start + arr[start] + 1):
        jump = 1 + minJumps(arr, k, end)
        if jump < minimumJump:
            minimumJump = jump
    return minimumJump


def bottomUpMY(arr):
    n = len(arr)
    jump = [0 for i in range(n)]

    if (n == 0) or (arr[0] == 0): 
        return float('inf')
    
    jump[0] = 0
    for i in range(1, n):
        jump[i] = float('inf')
        for j in range(i):
            print(i, j)
            if (i <= j + arr[j]) and (jump[j] != float('inf')):
                jump[i] = min(jump[i], jump[j] + 1)
                break
    return jump[n - 1]

def bottomUp(arr, n): 
    jumps = [0 for i in range(n)] 
  
    if (n == 0) or (arr[0] == 0): 
        return float('inf') 
  
    jumps[0] = 0
  
    # Find the minimum number of  
    # jumps to reach arr[i] from  
    # arr[0] and assign this  
    # value to jumps[i] 
    for i in range(1, n): ## RECURVISE MOVE
        jumps[i] = float('inf') 
        for j in range(j + arr[j]): ## AVAILABLE STATES
            # if (i <= ) and (jumps[j] != float('inf')): 
            jumps[i] = min(jumps[i], jumps[j] + 1) 
            # break
    return jumps[n-1]


arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
arr1 = [1, 3, 3, 1, 0, 7, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1]
n = len(arr)

print('Minimum number of jumps to reach end is', minJumps(arr, 0, n-1))
print('Minimum number of jumps to reach end is', minJumps(arr1, 0, len(arr1)-1)) 
print('Minimum number of jumps to reach end is', bottomUpMY(arr1))