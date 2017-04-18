# Get matches
p_1, p_2 = (int(i) for i in input().split())
p_3, p_4 = (int(i) for i in input().split())

# Pair times to contenders
elim_times = dict(zip([i for i in range(1,5)], [int(n) for n in input().split()]))

# dict for inverse lookup.
elim_inv = {v: k for k, v in elim_times.items()}

# get player numbers after first round
fp_1 = elim_inv[min(elim_times[p_1], elim_times[p_2])]
fp_2 = elim_inv[min(elim_times[p_3], elim_times[p_4])]

# Pair finalists and times
final_times = dict(zip([int(n) for n in input().split()], sorted([fp_1, fp_2])))

# get result
first = final_times[min(sorted(final_times))]
second = final_times[max(sorted(final_times))]

# Output winning order
print(first)
print(second)
