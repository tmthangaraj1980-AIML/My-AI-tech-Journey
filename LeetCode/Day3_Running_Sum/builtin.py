import itertools

def running_sum(nums):
    return list(itertools.accumulate(nums))


print(running_sum([1,2,3,4]))
