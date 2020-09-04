from collections import defaultdict

def lcs_recursion(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    
    if s1[m - 1] == s2[n - 1]:
        return 1 + lcs_recursion(s1, s2, m -1, n -1)
    else:
        return max(lcs_recursion(s1, s2, m -1, n), lcs_recursion(s1, s2, m, n-1))

def lcs(s1, s2):
    matrix = [[0] * (len(s2) + 1)] * (len(s1) + 1)
    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                matrix[i+1][j+1] = 1 + matrix[i][j]
            else:
                matrix[i+1][j+1] = max(matrix[i+1][j], matrix[i][j+1])
    print(matrix[i+1][j+1])
    print(matrix)
    # print(backtrack(matrix, s1, s2, len(s1), len(s2)))
    return "DONE"

def lcs_optimised(s1, s2):
    curr = [0]* (len(s2) + 1)
    prev = [0]* (len(s2) + 1)
    for c1 in s1:
        curr, prev = prev, curr
        for j, c2 in enumerate(s2):
            if c1 == c2:
                curr[j+1] = 1 + prev[j]
            else:
                curr[j+1] = max(prev[j+1], curr[j]) 
    return curr[-1]

def backtrack(matrix, s1, s2, i, j):
    if i == 0 or j == 0:
        return ""
    if  s1[i - 1] == s2[j -1]:
        return backtrack(matrix, s1, s2, i-1, j-1) + s1[i - 1]
    if matrix[i+1][j] > matrix[i][j+1]:
        return backtrack(matrix, s1, s2, i, j-1)
    return backtrack(matrix, s1, s2, i-1, j)

if __name__=="__main__":
    print(lcs_hashing("AGGTAB", "GXTXAYB"))
    # print(lcs_recursion("AGGTAB", "GXTXAYB", 6, 7))