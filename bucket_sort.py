def foo(nums):
    max_v = max(nums)
    bucket = [0] * (max_v +1)
    for i in nums:
        bucket[i] += 1
    print(bucket)
    res= []
    for i,v in enumerate(bucket):
        if v != 0:
            res.extend([i] * v)
    print(res)

a = [2,2,1,4,7,20,10]
print(a)
foo(a)


