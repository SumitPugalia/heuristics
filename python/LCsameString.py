def lcss(s1, s2):
    print(s1, s2)
    # matrix = [[0] * (len(s2)+1)] * (len(s1)+1)
    # print(matrix)
    matrix = [[0 for k in range(len(s2)+1)] for l in range(len(s1)+1)]
    # print(matrix)
    longestCount = 0
    for i,c1 in enumerate(s1):
        for j,c2 in enumerate(s2):
            if c1 == c2:
                matrix[i+1][j+1] = 1 + matrix[i][j]
                longestCount = max(matrix[i+1][j+1], longestCount)
            else:
                matrix[i+1][j+1] = 0
    return longestCount

# def lcss_recur(i, j, count) :  
      
#     if (i == 0 or j == 0) :  
#         return count  
          
#     if (X[i - 1] == Y[j - 1]) : 
#         count = lcss_recur(i - 1, j - 1, count + 1)  
      
#     count = max(count, max(lcss_recur( i, j - 1, 0),  
#                            lcss_recur( i - 1, j, 0)))  
  
#     return count 



def LCSubStr(X, Y, m, n): 
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)] 
    result = 0 
    for i in range(m + 1):
        for j in range(n + 1): 
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j])
                print(result)
            else: 
                LCSuff[i][j] = 0
    return result 
    
if __name__ == "__main__":
    print(lcss("OldSite:GeeksforGeeks.org", "NewSite:GeeksQuiz.com"))
    X = 'OldSite:GeeksforGeeks.org'
    Y = 'NewSite:GeeksQuiz.com'
    # print(lcss_recur(len(X), len(Y), 0))
    # m = len(X) 
    # n = len(Y) 
    
    # print('Length of Longest Common Substring is', 
    #                     LCSubStr(X, Y, m, n))