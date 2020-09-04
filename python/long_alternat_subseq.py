def long_alter_subs(arr):
    symbol = 0
    longest = []
    for i in range(len(arr)):
        element = arr[i]
        if symbol == 1 and element > arr[i-1]:
            longest.append(element)
            symbol = -1
        elif symbol == -1 and element < arr[i -1]:
            longest.append(element)
            symbol = 1
        elif symbol == 0 and i == 0:
            longest.append(element)
        elif symbol == 0 and i > 0:
            longest.append(element)
            symbol = 1 if arr[i] < arr[i-1] else -1
    print(longest)

if __name__=="__main__":
    long_alter_subs([1,2,3,4,5])
    long_alter_subs([1,5,3,2,4])
    long_alter_subs([5,3,4,1,2])


