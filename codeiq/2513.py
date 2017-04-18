# 256 exercise
def sumOfTwoInArray(arr, target_sum):
    for val in arr:
        if ((target_sum - val) in arr) and ((target_sum - val) != val):
            return "yes"
    return "no"

array_length = input()
vals = [int(i) for i in input().split()]

print(sumOfTwoInArray(vals, 256))
