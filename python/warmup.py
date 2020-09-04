## VALLEY

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    markDown = False
    count = 0
    for i in range(n):
        if s[i] == "D":
            level -= 1
            if level < 0:
                markDown = True
        else:
            level += 1
            if level == 0  and markDown:
                count += 1
    return count            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    res = 0
    i = 0
    n = len(c)
    while i < n-1:
        if i+2<n and c[i+2] == 0:
            i = i+2
            res += 1
        else:
            i = i+1
            res += 1
    return res
    

if __name__ == '__main__':
    

    result = jumpingOnClouds([0,1,0])

    print(str(result))
### MOVEMENT FRONT


def count_inversion(lst):
    return merge_count_inversion(lst)[1]

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count
for _ in range(int(input())):
    N=int(input())
    a=list(map(int,input().split()))
    if any(a[i]-(i+1)>2 for i in range(N)):
        print("Too chaotic")
    else:
        print(count_inversion(a))

### MOVEMENT FRONT (TRICK IS THE POP)

#!/bin/python3

for _ in range(int(input())):
    input()
    q = [int(x) for x in input().split()]
    bribes = 0
    valid = True
    for i in reversed(range(len(q))):
        v = i + 1
        if q[-1] == v:
            q.pop(-1)
        elif len(q) > 1 and q[-2] == v:
            q.pop(-2)
            bribes += 1
        elif len(q) > 2 and q[-3] == v:
            q.pop(-3)
            bribes += 2
        else:
            valid = False
            break
    if valid:
        print(bribes)
    else:
        print("Too chaotic")


## MINIMUM SWAP
def minimumSwaps(arr):
    swap = 0
    for i in range (len(arr)):
        # for j in range(i, len(arr)):
        if i+1 != arr[i]:
            while arr[i] != i +1:
                temp = arr[arr[i] -1]
                arr[arr[i] -1] = arr[i]
                arr[i] = temp
                swap += 1
    return swap


## ARRAY MANIPULATION WITH RANGES

def arrayManipulation(n, queries):
    Is = {}
    for m in range(len(queries)) :
        a,b,k = queries[m]
        if k == 0 :
            continue
        Is[a] = Is.get(a,0) + k
        Is[b+1] = Is.get(b+1,0) - k
        
    m,v = 0,0
    for i in sorted(Is) :
        v += Is[i]
        if v > m :
            m = v

    return m

## HASH
def checkMagazine(magazine, note):
    d = dict()
    
    for word in magazine:
        if d.get(word):
            d[word] += 1
        else:
            d[word] = 1
    
    for word in note:
        if d.get(word):
            if d[word] == 1:
                del d[word]
            else:
                d[word] -= 1
        else:
            print("No")
            return
    
    print("Yes")
    return

## ANAGRAM
def sherlockAndAnagrams(s):
    d = dict()
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = ''.join(sorted(s[i:j+1]))
            if d.get(sub):
                d[sub] += 1
            else:
                d[sub] = 1
    
    total = 0
    for count in d.values():
        total += sum(range(count))
    
    return total

## COUNTER FREQUENCY QUERIES
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from collections import Counter 

# Complete the freqQuery function below.
def freqQuery(queries):
    freq = Counter()
    cnt = Counter()
    arr = []

    for q in queries:
        if q[0]==1:
            cnt[freq[q[1]]]-=1
            freq[q[1]]+=1
            cnt[freq[q[1]]]+=1

        elif q[0]==2:
            if freq[q[1]]>0:
                cnt[freq[q[1]]]-=1
                freq[q[1]]-=1
                cnt[freq[q[1]]]+=1

        else:
            if cnt[q[1]]>0:
                arr.append(1)
            else:
                arr.append(0)
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()


## MAXIMUM TOYS

def maximumToys(prices, k):
    count = 0
    total = 0
    for price in sorted(prices):
        if total + price <= k:
            total += price
            count += 1
    return count

## COMPARATOR

from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(a, b):
        if a.score == b.score:
            if a.name > b.name:
                return 1
            else:
                return -1
        else:
            return b.score - a.score


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)


### ACTIVITY NOTIFICATION
#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    window = []
    notify = 0
    if d > len(expenditure):
        return notify

    for i in range(d):
        bisect.insort(window, expenditure[i])
    
    for i in range(d, len(expenditure)):
        if d % 2 == 0:
            mid = d // 2
            median = (window[mid -1] + window[mid])
        else:
            mid = d // 2
            median = window[mid] + window[mid]
        
        if expenditure[i] >= median:
            notify += 1
        del window[bisect.bisect_left(window, expenditure[i-d])]
        bisect.insort(window, expenditure[i])
    return notify