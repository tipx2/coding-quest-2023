with open("day1/input1.txt", "r") as f:
    lines = f.readlines()

items = {}

for line in lines:
    unique_id, quantity, mat_type = line.strip("\n").split(" ")
    if mat_type in items:
        items[mat_type] += int(quantity)
    else:
        items[mat_type] = int(quantity)


product = 1
for key in items.keys():
    product *= (items[key] % 100)

print(product)