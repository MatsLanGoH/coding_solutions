# 1. Read input
# 2. Convert hex input string to binary string(s)
# 3. Count horizontal pairs
# 4. Flip grid and count vertical pairs
# 5. Output


# Read input and convert to binary grid
hexin = input()
hexes = [hexin[i:i+2] for i in range(0, len(hexin), 2)]  # split hex pairs

# Convert to binary grid
grid = []
for h in hexes:
    grid.append(bin(int(h, 16))[2:].zfill(8))

binary = ''.join(grid)
output = [binary[i:i+8] for i in range(0, len(binary), 8)]


# Count sides for a line
def countSides(line):
    left = 0
    right = 0
    prev = -1
    for pos in line:
        if (pos != prev):
            if (prev == '0'):
                left += 1
            elif (prev == '1'):
                right += 1
        prev = pos
    return [left, right]


# Variables to keep track of side counts.
upTotal = 0
downTotal = 0
leftTotal = 0
rightTotal = 0

# Count sides for rows.
for line in grid:
    sides = countSides(line)
    leftTotal += sides[0]
    rightTotal += sides[1]

# Flip grid and get side count for columns
for i in range(len(grid)):
    line = ''
    for j in range(len(grid)):
        line += grid[j][i]
    sides = countSides(line)
    upTotal += sides[0]
    downTotal += sides[1]

# Output
print('{},{},{},{}'.format(upTotal, downTotal, leftTotal, rightTotal))
