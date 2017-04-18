"""
merges Intervals
"""


def combineIntervals(old, new):
    """
    Compares two 2-element intervals.
    If intervals overlap, an extended interval covering the difference of both
    is returned.
    Otherwise the bigger interval is returned.
    If no overlap, new interval is returned (??)
    """
    # case comparisons
    # if old contains new entirely:
    if (old[0] <= new[0]) and (new[1] <= old[1]):
        return old
    # else if new contains old entirely:
    elif (new[0] <= old[0]) and (old[1] <= new[1]):
        return new
    # else if intervals do not overlap
    elif (old[1] < new[0]) or (new[1] < old[0]):
        return old, new  # TODO: do I want to return both?
    # else overlap:
    else:
        return [min(old[0], new[0]), max(old[1], new[1])]



print(combineIntervals([0, 1], [2, 4]))
print(combineIntervals([2, 4], [0, 1]))
print(combineIntervals([0, 4], [2, 3]))
print(combineIntervals([2, 3], [0, 4]))
print(combineIntervals([0, 3], [2, 4]))
print(combineIntervals([2, 4], [0, 3]))
print(combineIntervals([0, 1], [2, 3]))
