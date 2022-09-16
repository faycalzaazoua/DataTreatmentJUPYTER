class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = [None]*target
        dic2=[None]*target
        result=[]
        c=0


        for c,i in enumerate(nums):
            value= target-i
            if dic[value] == None:
                    dic[i] = i
                    dic2[i] = c
            else:
                result.append(dic2[value])
                result.append(c)
                return result 

# Programme validé sur leetcode 
# complexité  : O(n)
# https://leetcode.com/problems/two-sum/


