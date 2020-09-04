def lps(st) : 
    n = len(st) # get length of input string 
  
    # table[i][j] will be false if substring  
    # str[i..j] is not palindrome. Else  
    # table[i][j] will be true 
    table = [[0 for x in range(n)] for y 
                          in range(n)]  
      
    # All substrings of length 1 are 
    # palindromes 
    maxLength = 1
    i = 0
    while (i < n) : 
        table[i][i] = True
        i = i + 1
      
    # check for sub-string of length 2. 
    start = 0
    i = 0
    while i < n - 1 : 
        if (st[i] == st[i + 1]) : 
            table[i][i + 1] = True
            start = i 
            maxLength = 2
        i = i + 1
      
    # Check for lengths greater than 2.  
    # k is length of substring 
    k = 3
    while k <= n : 
        # Fix the starting index 
        i = 0
        while i < (n - k + 1) : 
              
            # Get the ending index of  
            # substring from starting  
            # index i and length k 
            j = i + k - 1
      
            # checking for sub-string from 
            # ith index to jth index iff  
            # st[i+1] to st[(j-1)] is a  
            # palindrome 
            if (table[i + 1][j - 1] and 
                      st[i] == st[j]) : 
                table[i][j] = True
      
                if (k > maxLength) : 
                    start = i 
                    maxLength = k 
            i = i + 1
        k = k + 1
    print (st[start: start+maxLength]) 
  
    return maxLength # return length of LP



# A O(n^2) time and O(1) space program to find the 
#longest palindromic substring 

# This function prints the longest palindrome substring (LPS) 
# of str[]. It also returns the length of the longest palindrome 
def longestPalSubstr(string): 
	maxLength = 1

	start = 0
	length = len(string) 

	low = 0
	high = 0

	# One by one consider every character as center point of 
	# even and length palindromes 
	for i in xrange(1, length): 
		# Find the longest even length palindrome with center 
	# points as i-1 and i. 
		low = i - 1
		high = i 
		while low >= 0 and high < length and string[low] == string[high]: 
			if high - low + 1 > maxLength: 
				start = low 
				maxLength = high - low + 1
			low -= 1
			high += 1

		# Find the longest odd length palindrome with center 
		# point as i 
		low = i - 1
		high = i + 1
		while low >= 0 and high < length and string[low] == string[high]: 
			if high - low + 1 > maxLength: 
				start = low 
				maxLength = high - low + 1
			low -= 1
			high += 1

	print "Longest palindrome substring is:", 
	print string[start:start + maxLength] 

	return maxLength 

# Driver program to test above functions 
string = "forgeeksskeegfor"
print "Length is: " + str(longestPalSubstr(string)) 

# This code is contributed by BHAVYA JAIN 


# Python program to implement Manacher's Algorithm 

def findLongestPalindromicString(text): 
	N = len(text) 
	if N == 0: 
		return
	N = 2*N+1 # Position count 
	L = [0] * N 
	L[0] = 0
	L[1] = 1
	C = 1	 # centerPosition 
	R = 2	 # centerRightPosition 
	i = 0 # currentRightPosition 
	iMirror = 0	 # currentLeftPosition 
	maxLPSLength = 0
	maxLPSCenterPosition = 0
	start = -1
	end = -1
	diff = -1

	# Uncomment it to print LPS Length array 
	# printf("%d %d ", L[0], L[1]); 
	for i in xrange(2,N): 
	
		# get currentLeftPosition iMirror for currentRightPosition i 
		iMirror = 2*C-i 
		L[i] = 0
		diff = R - i 
		# If currentRightPosition i is within centerRightPosition R 
		if diff > 0: 
			L[i] = min(L[iMirror], diff) 

		# Attempt to expand palindrome centered at currentRightPosition i 
		# Here for odd positions, we compare characters and 
		# if match then increment LPS Length by ONE 
		# If even position, we just increment LPS by ONE without 
		# any character comparison 
		try: 
			while ((i+L[i]) < N and (i-L[i]) > 0) and \ 
					(((i+L[i]+1) % 2 == 0) or \ 
					(text[(i+L[i]+1)/2] == text[(i-L[i]-1)/2])): 
				L[i]+=1
		except Exception as e: 
			pass

		if L[i] > maxLPSLength:	 # Track maxLPSLength 
			maxLPSLength = L[i] 
			maxLPSCenterPosition = i 

		# If palindrome centered at currentRightPosition i 
		# expand beyond centerRightPosition R, 
		# adjust centerPosition C based on expanded palindrome. 
		if i + L[i] > R: 
			C = i 
			R = i + L[i] 

	# Uncomment it to print LPS Length array 
	# printf("%d ", L[i]); 
	start = (maxLPSCenterPosition - maxLPSLength) / 2
	end = start + maxLPSLength - 1
	print "LPS of string is " + text + " : ", 
	print text[start:end+1], 
	print "\n", 

# Driver program 
text1 = "babcbabcbaccba"
findLongestPalindromicString(text1) 

text2 = "abaaba"
findLongestPalindromicString(text2) 

text3 = "abababa"
findLongestPalindromicString(text3) 

text4 = "abcbabcbabcba"
findLongestPalindromicString(text4) 

text5 = "forgeeksskeegfor"
findLongestPalindromicString(text5) 

text6 = "caba"
findLongestPalindromicString(text6) 

text7 = "abacdfgdcaba"
findLongestPalindromicString(text7) 

text8 = "abacdfgdcabba"
findLongestPalindromicString(text8) 

text9 = "abacdedcaba"
findLongestPalindromicString(text9) 

# This code is contributed by BHAVYA JAIN 


if __name__=="__main__":
    print(lps("forgeeksskeegfor"))

