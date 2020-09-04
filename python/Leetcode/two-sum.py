# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# RELATED TOPICS: ARRAY, HASHMAP

# APPROACH: Since we need to search the numbers we can use map in some way to solve the problem.
# Lets explore the elements in the list and try to find if we have the remaining number visited if yes return that.

class Solution:
    def twoSum(self, nums, target):
        visited = dict()
        for index, num in enumerate(nums):
            findMe = target - num
            if  findMe in visited:
                return [visited[findMe], index]
            
            visited[num] = index
        return []

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))