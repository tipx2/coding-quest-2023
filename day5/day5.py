import requests
import os
import time

lines = requests.get("https://codingquest.io/api/puzzledata?puzzle=22").text.split("\n")

# all pixels are off apart from these
on_coords = []

currentline = 0
for line in lines:
    currentline += 1
    left_edge, top_edge, width, height = line.split(" ")
    left_edge = int(left_edge)
    top_edge = int(top_edge)
    width = int(width)
    height = int(height)

    for x in range(left_edge, left_edge + width):
        for y in range(top_edge, top_edge + height):
            if (x, y) in on_coords:
                on_coords.remove((x,y))
            else:
                on_coords.append((x,y))

    for x in range(10):
        for y in range(50):
            if (y,x) in on_coords:
                print("#", end="")
            else:
                print(".", end="")
        print()
    
    if currentline >= 0 and currentline < len(lines)//3:
        print("\u001b[31m")
    elif currentline >= len(lines)//3 and currentline < (2* len(lines)//3):
        print("\u001b[33m")
    elif currentline > (2* len(lines)//3) and currentline <= len(lines):
        print("\u001b[32m")
    print(currentline)
    print("\u001b[0m")
    
    time.sleep(0.001)
    if currentline == len(lines):
        input()
    os.system("cls")