import array

def print_array(arr):
    for element in arr:
        print(element, end=" ")
    print ("\r")

arr = array.array('i', [1, 2, 3])
print_array(arr)

arr.append(4)
print_array(arr)

arr.pop(2)
print_array(arr)

print(len(arr))

arr.reverse()
print_array(arr)

print(arr.index(1))