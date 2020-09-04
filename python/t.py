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

def arrayManipulation(n, queries):
    Is = {}
    for m in range(len(queries)):
        print("------------------------------------------------")
        a,b,k = queries[m]
        print(a)
        print(b)
        print(k)
        if k == 0 :
            continue
        Is[a] = Is.get(a,0) + k
        Is[b+1] = Is.get(b+1,0) - k
        print(Is)
        
    m,v = 0,0
    for i in sorted(Is) :
        print("+++++++++++++++++++++++++++++")
        print(i)
        print(Is[i])
        print(v)
        v += Is[i]
        if v > m :
            m = v

    return m

def checkMagazine(magazine, note):
    d = dict()
    for word in magazine:
        if d.get[word]:
            d[word] += 1
        else:
            d[word] = 0
    
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

if __name__ == '__main__':
    # result = arrayManipulation(2, [[1,2, 100], [2,3,100]])
    checkMagazine(['g', 'me', 'one', 'grand', 'today', 'night'], ['give'])
    print(str(result))




