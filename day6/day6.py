with open("day6/input6.txt") as f:
    lines = f.readlines()

covered_spots = set()
astroids = []

for line in lines:
    xloc, yloc, xspeed, yspeed = line.strip().split(" ")
    xloc = int(xloc)
    yloc = int(yloc)

    xspeed = int(xspeed)
    yspeed = int(yspeed)

    astroids.append([xloc, yloc, xspeed, yspeed])


for x in range(3660):

    if x % 300 == 0:
        print("loopcount", x)

    for i in range(len(astroids)):
        astroids[i][0] += astroids[i][2] # xloc += hori
        astroids[i][1] += astroids[i][3] # yloc += verti

        if x >= 3600:
            covered_spots.add((astroids[i][0] , astroids[i][1]))
                        

for d in range(100):
    for j in range(100):
        if (d, j) not in covered_spots:
            print(str(d) + ":" + str(j))