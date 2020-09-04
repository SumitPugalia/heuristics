# dp[0] = max(arr[start], arr[end])
# dp[1] = max(dp[0] + arr[start], dp[0] + arr[end])
# dp[n] = max(dp[n - 1] + arr[start], )
def maxPoints(arr, k, start, end):
    if k == 0:
        return 0
    
    dp = [0 for i in range(len(arr) + 1)]

    if len(arr) < k:
        return 0
    
    dp[max(maxPoints(arr, k - 1, start + 1, end), maxPoints(arr, k - 1, start, end - 1))
        
    return dp[k]




cardPoints = [1,2,3,4,5,6,1]
k = 3
print(maxPoints(cardPoints, k, 0, len(arr) - 1))

