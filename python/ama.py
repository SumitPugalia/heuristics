# def solution(A):
#     # write your code in Python 3.6
#     i = 0
#     count = 0
#     small_number_count = 0
#     while i < len(A):
#         j = 0
#         small_number_count = 0
#         while j <= i:
#             if A[j] <= i + 1:
#                 small_number_count = small_number_count + 1
#             j = j + 1
        
#         print(small_number_count)
#         if A[i] <= i + 1 and small_number_count >= A[i]:
#             count = count + 1
        
#         i = i + 1
#     return count


def solution(A):
    # s = int(A, 2)
    # count = 0

    # while s > 0:
    #     if s % 2 == 0:
    #         s = s // 2
    #     else:
    #         s = s - 1 
    #     count = count + 1
    # print(count)
    i = 0
    binarian = 0
    while i < len(A):
        binarian += 2 ** A[i]
        i = i + 1
    shortest_binarian = 0
    
    while binarian:
        shortest_binarian += binarian & 1
        binarian = binarian >> 1
    
    return shortest_binarian

def main(): 
    # function calling
    print(solution([1,0,2,0,0,2]))             
    # sorted(r, key = lambda k: (r[k], -k), reverse = True)

# main function calling 
if __name__=="__main__":       
    main() 