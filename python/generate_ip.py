#Your Function should return a list containing all possible IP address
#No need to worry about order
def is_valid(ip): 
  
    # Splitting by "." 
    ip = ip.split(".") 
      
    # Checking for the corner cases 
    for i in ip: 
        if len(i) > 3 or int(i) < 0 or int(i) > 255: 
            return False
        if len(i) > 1 and int(i) < 10: 
            return False
        # if len(i) > 1 and int(i) != 0 and i[0] == '0': 
        #     return False
    return True
  
# Function converts string to IP address 
def genIp(s): 
    sz = len(s) 
  
    # Check for string size 
    if sz > 12: 
        return [] 
    snew = s 
    l = [] 

    # Generating different combinations. 
    for i in range(1, sz - 2): 
        for j in range(i + 1, sz - 1): 
            for k in range(j + 1, sz): 
                snew = snew[:k] + "." + snew[k:] 
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]
                # Check for the validity of combination 
                if is_valid(snew): 
                    l.append(snew) 
                snew = s 
    return l

if __name__ == "__main__":
    print(genIp("96385"))