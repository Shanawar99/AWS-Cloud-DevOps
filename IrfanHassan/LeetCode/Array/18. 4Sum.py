#Given an array nums of n integers, return an array of all the unique quadruplets
def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    n=len(nums)
    nums.sort()
    set_=set()
    for i in range(n):
        for j in range(i+1,n):
            l,r=j+1,n-1
            while l<r:
                quadraplet=(nums[i],nums[j],nums[l],nums[r])
                if sum(quadraplet)==target and quadraplet not in set_:
                    set_.add(quadraplet)
                elif sum(quadraplet)>target:
                    r-=1
                else: 
                    l+=1
    return set_