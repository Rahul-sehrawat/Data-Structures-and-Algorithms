#Link - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [i,map[diff]]
            map[n] = i

'''
1.use dict to store the visited values
2.use enumerate to access both index and value in list
3.if the diff exist in dict , simply return the list with its indexes
'''
