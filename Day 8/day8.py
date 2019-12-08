f = open("input.txt","r").read().strip("\n")
f = list(map(int, f))
candidate = {0:0, 1:0, 2:0}
top_candidate = {}
fewest_zeros = 9999

for i in range(len(f)):
    if f[i] == 0:
        candidate[0] += 1
    elif f[i] == 1:
        candidate[1] += 1
    elif f[i] == 2:
        candidate[2] += 1

    if i % (25*6)-1 == 0 and i != 1:
        if candidate[0] < fewest_zeros:
            top_candidate = candidate.copy()
            fewest_zeros = candidate[0]
        candidate = {0:0, 1:0, 2:0}

print(top_candidate)
print(top_candidate[1]*top_candidate[2])
