import bisect 

def lis(arr):
    n = len(arr) 
    lis = [1]*n
    maximum = 0
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                if lis[i] > maximum:
                    maximum = lis[i]
    return maximum

# def lis_nlogn(arr):
#     if len(arr) == 0:
#         return 0
        
#     l = [arr[0]]
#     for element in arr[1:]:
#         pos = bisect.bisect(l, element)
#         if pos == len(l):
#             if element > l[pos - 1]:
#                 l.append(element)
#         else:
#             if element != l[pos - 1]:
#                 l[pos] = element
#     return len(l)

    # if len(arr) == 0:
    #     return 0
    # l = [arr[0]]
  
    # for element in arr[1:]:
    #     pos = bisect.bisect(l, element)
    #     if pos == len(l):      
    #         if element > l[pos - 1]:
    #             l.append(element)
    #     else:
    #         if element != l[pos - 1]:
    #             l[pos] = element
    #     return len(l)

def lis_nlogn(arr):
    l = [[arr[0]]]
    for element in arr[1:]:
        pos = bisect.bisect(l[-1], element)
        print(pos, element, l)
        if pos == len(l):
            if element > l[pos -1][pos - 1]:
                l.append(l[pos -1] + [element])
        elif pos == 0:
            l[pos][pos] = element
        else:
            if element != l[pos -1][pos -1]:
                l[pos][pos] = element
    return l[-1]

    # n = len(arr) 
    # lis = [1]*n 
    # for i in range (1, n): 
    #     for j in range(0, i): 
    #         if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
    #             lis[i] = lis[j]+1
    # maximum = 0
    # for i in range(n): 
    #     maximum = max(maximum, lis[i]) 
  
    # return maximum 


if __name__ == "__main__":
    # print(lis([1, 4, 6, 7, 2, 3, 5, 10]))
    print(lis_nlogn([10, 12, 9, 13, 21, 50, 41, 65, 85]))
    print(lis_nlogn([1, 2, 3, 10, 5, 6]))
    print(lis_nlogn([2, 2]))
    print(lis_nlogn([4,10,4,3,8,9]))


# import bisect
# class Solution:
#     def lengthOfLIS(self, arr: List[int]) -> int:
#         if len(arr) == 0:
#             return 0
        
#         l = [arr[0]]
#         for element in arr:
#             pos = bisect.bisect(l, element)
#             if pos == len(l):
#                 if element > l[pos - 1]:
#                     l.append(element)
#             else:
#                 if element != l[pos - 1]:
#                     l[pos] = element

#         return len(l)