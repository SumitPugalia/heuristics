def coinChange(arr, n, N):
    if N == 0:
        return 1
    if N < 0 or n < 0:
        return 0
    
    inc = coinChange(arr, n, N - arr[n])

    exc = coinChange(arr, n - 1, N)
    
    return inc + exc

if __name__ == '__main__':
	S = [1, 2, 3]
	N = 4
	print("Total number of ways to get desired change is", coinChange(S, len(S) -1, N))
