def sort(nums,left,right):
    if left < right:
        p = partion(nums,left,right)
        sort(nums,left,p-1)
        sort(nums,p+1,right)

def partion(nums,left,right):
    i = left
    j = right-1
    p = nums[right]

    while i < j:
        while i < right and nums[i] < p:
            i+=1
        while j > left and nums[j] >=p:
            j-=1
        if i<j:
            nums[i],nums[j] = nums[j],nums[i]
    if nums[i] > p:
        nums[i],nums[right] = nums[right],nums[i]
    return i

nums = [20,50,30,90,70,60,40]
sort(nums,0,len(nums)-1)
print(nums)

