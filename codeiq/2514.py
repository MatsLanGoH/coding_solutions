# Bit count

# Get input
n, m = map(int, input().split())


def countBits(target, ones):
	count = 0
	for i in range(0,target + 1):
		if (format(i, "08b").count("1") == ones):  # convert to binary and count 1s
			count += 1
	return count

print(countBits(n,m))
