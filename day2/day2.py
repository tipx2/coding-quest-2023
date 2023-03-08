with open("day2/input2.txt", "r") as f:
	lines = f.readlines()

saved = []
for line in lines:
	num = str(bin(int(line.strip("\n"))))[2:]
	if num.count("1") % 2 == 0:
		saved.append(num)


for n in range(len(saved)):
	saved[n] = "0" + saved[n].zfill(16)[1:]

print(round(sum([int(x, 2) for x in saved])/len(saved)))