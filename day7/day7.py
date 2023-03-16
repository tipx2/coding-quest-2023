import pygrille

grid = pygrille.Grid(30, (20, 20), framerate=120)


with open("C:\\Users\\avish\\Documents\\GitHub\\coding-quest-2023\\day7\\input7.txt") as f:
    lines = f.readlines()

fruits = lines[1].split(" ")
fruits = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in fruits]

moves = lines[3]

snake_parts = [(0,0)]
score = 0

new_hex = "#0575E6"
original_hex = "#021B79"

original_r = int(original_hex[1:3], 16)
original_g = int(original_hex[3:5], 16)
original_b = int(original_hex[5:7], 16)

new_r = int(new_hex[1:3], 16)
new_g = int(new_hex[3:5], 16)
new_b = int(new_hex[5:7], 16)

def get_color(i, l):
    return[int(j) for j in (i/l*(new_r - original_r)+original_r,i/l*(new_g - original_g)+original_g,i/l*(new_b - original_b)+original_b)]
   

for move in moves:
    if move == "L":
        new_head = (snake_parts[0][0]-1, snake_parts[0][1])
    elif move == "R":
        new_head = (snake_parts[0][0]+1, snake_parts[0][1])
    elif move == "D":
        new_head = (snake_parts[0][0], snake_parts[0][1]+1)
    elif move == "U":
        new_head = (snake_parts[0][0], snake_parts[0][1]-1)


    if new_head[0] > 19 or new_head[1] > 19 or new_head in snake_parts:
        print(score)
        break
    if new_head == fruits[0]:
        score += 100
        fruits = fruits[1:]
        snake_parts = [new_head] + snake_parts
    else:
        # snake translated onto new bit
        snake_parts = [new_head] + snake_parts[:-1]
    score += 1

    for x in range(20):
        for y in range(20):
            if (x, y) in snake_parts:
                grid[x][y].colour = get_color(snake_parts.index((x, y)), len(snake_parts))
            elif (x, y) == fruits[0]:
                grid[x][y].colour = "red"
            else:
                grid[x][y].colour = "black"
    grid.draw()
    grid.tick()
