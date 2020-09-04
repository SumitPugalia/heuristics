# Function calling 
def dictionairy():  
  
 # Declaring hash function       
 key_value ={}     
   
# Initializing the value  
 key_value['a'] = 56       
 key_value['c'] = 2
 key_value['r'] = 2
 key_value['j'] = 2
 key_value['t'] = 12 
 key_value['x'] = 24
 key_value['z'] = 18      
 key_value['p'] = 323 
   
  
 print ("Task 3:-\nKeys and Values sorted",  
   "in alphabetical order by the value") 
   
 # Note that it will sort in lexicographical order 
 # For mathematical way, change it to float 
 print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))     
   
def main(): 
    # function calling 
    dictionairy()             
    # sorted(r, key = lambda k: (r[k], -k), reverse = True)

# main function calling 
if __name__=="__main__":       
    main() 