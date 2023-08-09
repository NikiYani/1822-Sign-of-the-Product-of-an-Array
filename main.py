class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        
        for i in range(0, len(nums)) :
            if nums[i] > 0 :
                continue
            elif nums[i] == 0 :
                result = 0
                break
            else :
                result *= -1
 
        return result