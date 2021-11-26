def sort(nums):
    for i in range(1 ,len(nums)):
        j = i
        while nums[j - 1] > nums[j] and j>0:
            nums[j - 1], nums[j] = nums[j] , nums[j-1]
            j -=1

nums = [6,8,5,7,4,3,1,2]
sort(nums)
print(nums)

