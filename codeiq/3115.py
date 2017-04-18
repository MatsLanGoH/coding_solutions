try:
    while True:
        nums = sorted([int(n) for n in input()])
        if (nums[0] == 0):
            print(nums[1])
        else:
            print(nums[len(nums)-1])

except:
    pass
