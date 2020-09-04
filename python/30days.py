# READING FROM STDIN DIFF TYPES OF VALUE 

i = 4
d = 4.0
s = 'HackerRank '

ri = int(input())
print(ri + i)

rd = float(input())
print(rd + d)

rs = input()
print(s + rs)


## OPERATORS

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    return round(tip + tax + meal_cost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    totalCost = solve(meal_cost, tip_percent, tax_percent)

    print(totalCost)

## CONDITIONALS

if __name__ == '__main__':
    N = int(input())
    if N % 2 == 0:
        if N >= 6 and N <= 20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
    

## CLASSES AND OBJECTS
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge
    
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")


## LOOPS

if __name__ == '__main__':
    n = int(input())

    for i in range (1, 11):
        print(str(n) + " x " + str(i) + " = " + str(i * n))


## REVIEW

count = int(input())
while count > 0:
    data = input()
    even = ""
    odd = ""
    for i in range(0, len(data)):
        if i % 2 == 0:
            even = even.join(data[i])
        else:
            odd = odd.join(data[i])
    print(even + " " + odd)
    count -= 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
count = int(input())
while count > 0:
    data = input()
    even = []
    odd = []
    for i in range(0, len(data)):
        if i % 2 == 0:
            even.append(data[i])
        else:
            odd.append(data[i])
    print("".join(even) + " " + "".join(odd))
    count -= 1

## REVERSE AND PRINT IN SAME LINE

    arr = list(map(int, input().rstrip().split()))

    for i in range (len(arr), 0, -1):
        print(arr[i - 1], end= " ")

>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe

>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1


## DICTIONARY
count = int(input())
phoneBook = dict()
for i in range(count):
    [key, value] = input().split()
    phoneBook[key] = value

for i in range(count):
    findMe = input()
    if findMe in phoneBook:
        print(findMe + "=" + phoneBook[findMe])
    else:
        print("Not found")


## FACTORIAL
def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()


## BIT OPERATION (BINARY)
if __name__ == '__main__':
    n = int(input())
    maxCount = 0
    count = 0
    while n > 0:
        if n & 1:
            count += 1
            n = n >> 1
        else:
            if count > maxCount:
                maxCount = count
            
            count = 0
            n = n >> 1
    if count > maxCount:
        maxCount = count
    print(maxCount)

### 2D ARRAY
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    maxCount = None
    for i in range(0, len(arr) - 2):
        for j in range(0, len(arr[0]) - 2):
            count = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if maxCount == None or count > maxCount:
                maxCount = count
    print(maxCount)

## INHERITANCE
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    
    def calculate(self):
        sum = 0
        for i in self.scores:
            sum += i
        
        avg = sum / len(self.scores)
        
        if avg >= 90 and avg <= 100:
            return 'O'
        elif avg >= 80 and avg < 90:
            return 'E'
        elif avg >= 70 and avg < 80:
            return 'A'
        elif avg >= 55 and avg < 70:
            return 'P'
        elif avg >= 40 and avg < 55:
            return 'D'
        else:
            return 'T'
        

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input()) # not needed for Python
    scores = list( map(int, input().split()) )
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())

## ABSTRACT 

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price
    
    def display(self):
        print("Title:" + " " + self.title)
        print("Author:" + " " + self.author)
        print("Price:" + " " + str(self.price))
    
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

## SCOPE

class Difference:
    def __init__(self, a):
        self.__elements = a
    
    def computeDifference(self):
        maxDifference = 0
        a = self.__elements
        # self.maximumDifference
        for i in range(0, len(a) - 1):
            for j in range(i + 1, len(a)):
                difference = abs(a[i] - a[j])
                if difference > maxDifference:
                    maxDifference = difference
        
        self.maximumDifference = maxDifference
	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

## LINKED LIST

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        node = Node(data)
        last = head 
        while last and last.next != None:
            last = last.next
        
        if head:
            last.next = node
        else:
            head = node
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 


## EXCEPTION

import sys

S = input().strip()

try:
    i = int(S)
    print(i)
except ValueError:
    print("Bad String")

## THROW EXCEPTION

#Write your code here
class Calculator():
    def __init__(self): pass
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")  
        return pow(n, p)

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   

# PALINDROME STACK AND QUEUE 

import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, ch):
        self.stack.append(ch)
    
    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.pop(0)

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    



## INTERFACE
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = 0
        i = n
        while i > 0:
            if n % i == 0:
                sum += i
            i -= 1  
        return sum

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

## BUBBLE SORT

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numSwap = 0
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            numSwap += 1

print("Array is sorted in " + str(numSwap) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))

## BST

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        if root == None:
            return -1

        return max(1 + self.getHeight(root.left), 1 + self.getHeight(root.right))

        # IF HAVE TO RETURN -1 for no node and 0 for root node

        if root is None: return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)  


## LEVEL ORDER
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        queue = []
        
        while root is not None:
            print(root.data, end = " ")
            
            if root.left is not None:
                queue.append(root.left)
            
            if root.right is not None:
                queue.append(root.right)
            
            ## TERNARY
            root = queue.pop(0) if len(queue) > 0 else None

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)



## LINKEDLIST 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        if head is None and head.next is None:
            return head

        originalHead = head
        valuesPresent = dict()
        valuesPresent[head.data] = True 
        
        while head.next:
            if valuesPresent.get(head.next.data):
                temp = head.next
                head.next = head.next.next
                temp.next = None
                del temp
            else:
                valuesPresent[head.next.data] = True
                head = head.next
        return originalHead

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 


## PRIME 
count = int(input())

for i in range(0, count):
    number = int(input())
    divisor = 2
    prime = True

    while divisor <= number**(0.5):
        if number % divisor == 0:
            prime = False
            break
        divisor += 1
    
    if number != 1 and prime:
        print("Prime")
    else:
        print("Not prime")

## TESTING

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        return []

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        # complete this function
        return [5, 10, 15, 17, 4]

    @staticmethod
    def get_expected_result():
        # complete this function
        return 4

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        # complete this function
        return [5, 10, 1, 10, 1]

    @staticmethod
    def get_expected_result():
        # complete this function
        return 2

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")



## REGEX SORTING

import math
import os
import random
import re
import sys
import bisect 



if __name__ == '__main__':
    N = int(input())
    result = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        namePattern = '^[a-z]{1,20}$'
        emailPattern = '^(?=.{1,50}$)[a-z]+[\.]?[a-z]+[\@]gmail[\.]com$'
        if re.match(emailPattern, emailID) and re.match(namePattern, firstName):
            bisect.insort(result, firstName)

    for i in range(len(result)):
        print(result[i])


## BIT AND REVERSE LOOP
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        maximum = 0
        for i in range(n, 1, -1):
            for j in range(i - 1, 0, -1):
                r = i & j
                if r > maximum and r < k:
                    maximum = r
                    if maximum == k - 1:
                        break
            if maximum == k - 1:
                break
        print(maximum)