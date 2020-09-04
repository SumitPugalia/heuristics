import heapq

def solution(S, X, Y):
    # write your code in Python 3.6
    res = dict()
    resList = []
    maxDistance = float("inf")
    distance = 0
    for index, tag in enumerate(S):
        distance = ((X[index] ** 2) + (Y[index] ** 2)) ** 0.5
        if distance < maxDistance:
            if tag in res:
                maxDistance = distance
                ## Remove all smaller
                while resList:
                    (d, t) = heapq.heappop(resList)
                    if maxDistance > d * (-1):
                        heapq.heappush(resList, (d, t))
                        break
                    res[t] = res[t] - 1
            else:
                res[tag] = 1
                heapq.heappush(resList, (distance * (-1), tag))
    return len(resList)
    


if __name__ == "__main__":
    S = "ABDCA"
    X = [2, -1, -4, -3, 3]
    Y = [2, -2, 4, 1, -3]
    print(solution(S, X, Y))
    
    S = "ABB"
    X = [1, -2, -2]
    Y = [1, -2, 2]
    print(solution(S, X, Y))

    S = "CCD"
    X = [1, -1, 2]
    Y = [1, -1, -2]
    print(solution(S, X, Y))