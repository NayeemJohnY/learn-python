# Bubble Sort

def sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                temp =  nums[j]
                nums[j] = nums[j+1]
                nums[j + 1] = temp


    return nums

nums = [1,3, 4,2,67, 45,4]
print(sort(nums))

# Selection sort
def sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i,len(nums)-1):
            if nums[j] < nums[minpos]:
                minpos= j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp


    return nums

print(sort(nums))