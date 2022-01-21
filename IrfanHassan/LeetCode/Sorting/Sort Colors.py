class Solution:
    def sortColors(self, nums):
    
        if len(nums) <= 1:
            return
        i, j = 0, len(nums)-1
        
        while i < j:
            if nums[i] == 2:
                if nums[j] < 2:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
                j-=1
            else:
                i+=1
                
        j,i = i, 0
        
        while i < j:
            if nums[i] == 1:
                if nums[j] < 1:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
                j-=1
            else:
                i+=1
            
        return