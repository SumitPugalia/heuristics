def permute(a, l, r):
    if l == r:
        print(''.join(a))
        # pass 
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

if __name__ == "__main__":
    s = "ABC"
    permute(list(s), 0, 2)

# Python program to print all permutations with 
# duplicates allowed 

def toString(List): 
	return ''.join(List) 

# # Function to print permutations of string 
# # This function takes three parameters: 
# # 1. String 
# # 2. Starting index of the string 
# # 3. Ending index of the string. 
# def permute(a, l, r): 
# 	if l==r: 
# 		print(toString(a)) 
# 	else: 
# 		for i in range(l,r+1): 
# 			a[l], a[i] = a[i], a[l] 
# 			permute(a, l+1, r) 
# 			a[l], a[i] = a[i], a[l] # backtrack 

# # Driver program to test the above function 
# string = "ABCD"
# n = len(string) 
# a = list(string) 
# permute(a, 0, n-1) 

# This code is contributed by Bhavya Jain 



[  1, 5, 3,  8,  0,   3
 1[1, 6, 9, 17, 17, 20],
 5[0, 5, 8, 16, 16, 19],
 3[0, 0, 3, 11, 11, 14],
 8[0, 0, 0, 8, 8, 11],
 0[0, 0, 0, 0, 0, 3],
 3[0, 0, 0, 0, 0, 3]
]

Using HashMap m[5] = 20, m[6] = 20, m[7] = 20 + 30 /  2
## Input = [(StartPoint, EndPoint, Speed)] 
def AvgSpeed(inputs):
	inputs.sort()
	output = [] 	//(start, end, AvgSpeed)
for item in inputs:
if not output:
output.append(item)
else:

output[-1][0] < item[0]  <  output[-1][1]:
	o = output.pop()
	e = mergeAndSplit(output, item)
		output.extend(e)
output = [(5, 7, 20), (7, 10, 25) (), ()]


def mergeAndSplit(output, item):
	
##5, 10, 20
##7, 15, 30
##5,7,10 15

## 5, 10
## 5, 7

5, 7 = 20
7, 10 = 25
10, 15 = 30

	(startO, endO, speedO) = output
	(startI, endI, speedI) = item
	

if startI < endO: 
		first = (startO, startI, speedO)
if endO < endI:	
second = (startI, endO, (speedO + speedI)/2)
third = (endO, endI, speedI)
return [second third]

elif endO > endl:
		second = (startI, endI, (speedI + speedO)/2)
third = (startI, endO, speedO)
return [first, second third]
else:
 second=  (startI, endO,  (speedI + speedO)/2)
return [first, second]
	elif startI == startO:
if endO < endI:	
second = (startI, endO, (speedO + speedI)/2)
third = (endO, endI, speedI)
return [second third]

elif endO > endl:
		second = (startI, endI, (speedI + speedO)/2)
third = (endl, endO, speedO)
return [second third]
else:
 second=  (startI, endO,  (speedI + speedO)/2)
return [first]
else:
	return [output, item]
