# Lexographically minimal string after rotation

def lmsr(s):
    ss = s + s
    count = 0
    lowest = s
    i = 0
    while i < len(s):
        sub = ss[i:i+len(s)]
        if sub < lowest:
            lowest = sub
            count = i
        i += 1
    print(count, lowest)
    # print (lowest)

if __name__ == "__main__":
    lmsr("CDAABD")
    lmsr("GEEKSQUIZ")
    lmsr("GFG")
    lmsr("GEEKSFORGEEKS")
    # lmsr("cdab")
