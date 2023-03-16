import itertools
with open("C:\\Users\\avish\\Documents\\GitHub\\coding-quest-2023\\day8\\input8.txt") as f:
    lines = f.readlines()

distance_dict = {}
n = 1
for line in lines:
    distance_dict[n] = [int(x) for x in line.split(" ")]
    n += 1

visited = [1]
total = 0
while len(visited) < 12:
    for x in distance_dict[visited[-1]]:
        total += min(x)
        visited.appen(x.index(min(x)) +1)

