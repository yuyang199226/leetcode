

def partition(nums, l ,r):
    pivot = nums[r]
    i = l -1
    for j in range(l ,r):
        if nums[j] <= pivot:
            nums[j], nums[i+1] = nums[i+1], nums[j]
            i += 1
    nums[i+1], nums[r] = nums[r], nums[i+1]

    return i+1

def quick_sort(nums, l ,r):
    if r > l:
        mid = partition(nums, l ,r)
        quick_sort(nums, l, mid-1)
        quick_sort(nums, mid+1, r)

a = [6,8,2,7,1,5]
quick_sort(a, 0, 5)
print(a)

