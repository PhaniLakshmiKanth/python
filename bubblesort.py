def bubblesort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if nums[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp

nums = [5,3,9,6,4]
bubblesort(nums)
print(nums)

