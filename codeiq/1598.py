# Read input

min_vals = [15, 15]
max_vals = [0, 0]

try:
    while True:
        vals = map(int, input().split(','))
    for idx, val in enumerate(vals):
        if val > max_vals[idx]:
            max_vals[idx] = val
    if val < min_vals[idx]:
        min_vals[idx] = val

except EOFError:
    pass


size_x, size_y = (max_vals[0] - min_vals[0])**2, (max_vals[1] - min_vals[1])**2
largest = size_x if size_x > size_y else size_y
print(largest)
