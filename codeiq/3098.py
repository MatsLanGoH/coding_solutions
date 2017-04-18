# Solution for codeIQ problem 3098
# 2017/1/20 Matthias Lambrecht

"""
1. Read each instruction and store start/end coordinates per row or column.
2. Merge intervals if multiple values in the same row/column.
3. Find overlapping tiles.
4. Get sum of all row and column squares.
5. Get sum of collisions (row/column).
6. Output sum of squares - sum of collisions.
"""

# Variables
collisions = 0
columns = dict()
rows = dict()


def addIntervals(existing, current):
    """
    Adds current interval to list of existing intervals.
    If current interval overlaps with any interval of oldList,
    the intervals are merged and appended to the list.
    """
    added = []
    # Find out how current and elements in existing are related
    for interval in existing:
        # if current overlaps with interval extend it.
        if (mergeIntervals(interval, current)):
            current = mergeIntervals(interval, current)
        # otherwise append mergeIntervals as it is
        else:
            added.append(interval)
    # finally, append current
    added.append(current)
    return added


def mergeIntervals(old, new):
    """
    Returns two Intervals if they can be merged (i.e. if they overlap).
    Returns False for all other cases.
    """
    # case comparisons
    # if old contains new entirely:
    if (old[0] <= new[0]) and (new[1] <= old[1]):
        return False
    # else if new contains old entirely:
    elif (new[0] <= old[0]) and (old[1] <= new[1]):
        return False
    # else if intervals do not overlap
    elif (old[1] < new[0]) or (new[1] < old[0]):
        return False
    # else overlap: return merged Interval
    else:
        return [min(old[0], new[0]), max(old[1], new[1])]


#
# Process input and populate columns/rows
#
try:
    while True:
        instructions = input().split()

        for line in instructions:
            # Split instructions into direction and coordinates
            direction = line.split(',')[0]
            curX, curY, squares = [int(i) for i in line.split(',')[1:]]

            # TODO: could refactor the sorting algorithm
            #
            # Sort row/columns dict according to direction instruction
            if (direction == "H"):
                # If key exists, update value using the addIntervals function
                if (curY in rows.keys()):
                    rows[curY] = addIntervals(rows[curY], [curX, curX + squares - 1])
                # otherwise add key for the first time with given range
                else:
                    rows.setdefault(curY, []).append([curX, curX + squares - 1])

            elif (direction == "V"):
                # If key exists, update value using the addIntervals function
                if (curX in columns.keys()):
                    columns[curX] = addIntervals(columns[curX], [curY, curY + squares - 1])
                # otherwise add key for the first time with given range
                else:
                    columns.setdefault(curX, []).append([curY, curY + squares - 1])
        break
except:
    pass



def countOverlaps(columns, rows):
    """
    Calculates sum of overlapping tiles for two
    dictionaries containing columns/rows data
    """
    # Iterate over each row
    #  For each range in a row, see if there is a column that falls inside it.
    #  If yes, add the [x,y] (i.e. row,col) coordinates to the list.
    overlaps = []
    colXs = [x for x in columns.keys()]

    for rowY, rowXranges in rows.items():
        # Does a column cross this row?
        for rowXrange in rowXranges:
            for colX in colXs:
                # If there is a colX in this range...
                if ((rowXrange[0] <= colX) and (colX <= rowXrange[1])):
                    # ...check if any of its ranges contains colX.
                    for colXrange in columns[colX]:
                        if ((colXrange[0] <= rowY) and (rowY <= colXrange[1])):
                            # we have a collision
                            overlaps.append((colX, rowY))
    return(len(set(overlaps)))


def calculator(coordinates):
    """
    Calculate total sum from column / row data:
    """
    total = 0
    for pos, ranges in coordinates.items():
        min = 10000001
        max = 0
        tally = 0
        for range in ranges:
            # print(pos, range)
            if range[0] < min:
                min = range[0]
            if range[1] > max:
                max = range[1]
        tally += 1 + max-min
        total += tally
        # print('\n', max, min, max-min, tally)
    return total

#####
# Output result
#####
tiles_count = calculator(rows) + calculator(columns)
collisions = countOverlaps(columns, rows)
# print('rows', rows)
# print('columns', columns)
# print(tiles_count, '-', collisions, '=', tiles_count - collisions)
print(tiles_count - collisions)
