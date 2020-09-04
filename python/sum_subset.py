def count(arr, total):
    mem = {}
    return dp(arr, total, len(arr) - 1, mem)

def dp(arr, total, i, mem):
    key = str(total) + ":" + str(i)
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    elif total < 0 or i < 0:
        return 0
    elif total < arr[i]:
        to_return  = dp(arr, total, i - 1, mem)
    else:
        to_return = dp(arr, total, i - 1, mem) + dp(arr, total - arr[i], i - 1, mem) 
    mem[key] = to_return
    return to_return
   
if __name__=="__main__":
    arr= [3, 9, 7, 6, 4, 5, 2]
    total = 9
    print(count(arr, total))