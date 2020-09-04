from queue import PriorityQueue

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pq = PriorityQueue()
        stack = []
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append((i, c))
            elif c == ")":
                if stack:
                    (_, p) = stack[-1]
                    if p == "(":
                        pq.put(stack.pop())
                        pq.put((i, c))
                    else:
                        stack.append((i, c))    
                else:
                    stack.append((i, c))
            
            else:
                pq.put((i, c))
        res = []
        while not pq.empty():
            (_, c) = pq.get()
            print("INSIDE LOOP", c)
            res.append(c)
        
        return ''.join(res)


s = Solution()
print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
