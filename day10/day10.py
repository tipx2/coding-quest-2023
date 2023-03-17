import requests
import heapq

with open("day10/input10.txt") as f:
    lines = f.read()


# this is a chatgpt solution, my original one got the same answer however I didn't realise that I had to take away 600 at the end
def shortest_travel_time(beacon_data):
    # Create graph with beacons as nodes and travel times as edges
    graph = {}
    for line in beacon_data.split("\n"):
        if line == "":
            continue
        beacon1, connections = line.split(" => ")
        graph[beacon1] = {}
        for connection in connections.split(" "):
            beacon2, travel_time = connection.split(":")
            graph[beacon1][beacon2] = int(travel_time)

    # Initialize distances to infinity for all nodes except TYC
    distances = {beacon: float("inf") for beacon in graph}
    distances["TYC"] = 0

    # Use priority queue to visit nodes in order of their distance from TYC
    queue = [(0, "TYC")]
    while queue:
        curr_distance, curr_node = heapq.heappop(queue)
        # If we've reached EAR, return the shortest travel time
        if curr_node == "EAR":
            return curr_distance
        # Otherwise, examine all neighboring nodes
        for neighbor, weight in graph[curr_node].items():
            distance = curr_distance + weight + 600 # Add 600 seconds for stopping time
            # If this distance is less than the current distance for the neighbor, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    # If we've visited all nodes and still haven't reached EAR, there is no path
    return None

print(shortest_travel_time(lines)-600)