# Outputs number of squares painted black
# after given a series of coordinates / directions.
#
# Idea: No need to draw a grid.
#       Keep track of painted squares as tuplets
#       Add a painted square to a set of painteds.
#       Finally count the length of this set.
#
# Pseudocode:
#       Create storage set.
#       Read input.
#       For each line in input:
#           Split input into H/V, startX, startY, numSquares
#           If H:
#               in range 0, numSquares:
#                   add (x,y) to set
#                   increase x by one
#           If V:
#               in range 0, numSquares:
#                   add (x,y) to set
#                   increase y by one
#       print the length of the storage set.

# Read and process input
from itertools import count

# Store painted squares
# painted_squares = set()
# painted_squares = []
painted_squares = {}

# Process square input
try:
    while True:
        instructions = input().split()

        for line in instructions:
            direction = line.split(',')[0]
            posX, posY, numSquares = [int(i) for i in line.split(',')[1:]]

            # Todo: refactor!
            if (direction == "H"):
                for n in count():
                    if n == numSquares:
                        break
                    painted_squares.setdefault(posX+n, set()).add(posY)

            elif (direction == "V"):
                for n in count():
                    if n == numSquares:
                        break
                    painted_squares.setdefault(posX, set()).add(posY+n)
        break
except:
    pass

# Count items in painted_squares
squares_count = 0
for v in painted_squares.values():
    squares_count += len(v)


# output number of painted squares
print(painted_squares)
print(squares_count)
