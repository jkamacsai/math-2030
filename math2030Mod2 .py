# code for math 2030 module two paper on Modeling Real Travel
# Routes Using Shortest-Path Algorithms

#define a simple road network dictionary
#each location will map to their neighbour with travel times

graph = { "A" : {"B": 5, "C": 12},
          "B" : {"A": 5, "C": 4},
          "C": {"A": 12, "B": 4}}

#Travel times with possible routes
route_1 = ["A", "B", "C"]
route_2 = ["A", "C"]

time_1 = graph["A"]["B"] + graph["B"]["C"]
time_2 = graph["A"]["C"]

#comparison of routes
if time_1 < time_2:
    shortest_path = route_1
    shortest_time = time_1

else:
    shortest_path = route_2
    shortest_time = time_2

print("Shortest Route: ", shortest_path)
print("Total Travel Time: ", shortest_time)


#create a simulation of congestion that increased travel time

graph["B"]["C"] =15

#recalculate route times

time_1 = graph["A"]["B"] + graph["B"]["C"]
time_2 = graph["A"]["C"]

#comapre routes again

if time_1 < time_2:
    shortest_path = route_1
    shortest_time = time_1

else:
    shortest_path = route_2
    shortest_time = time_2

print("Shortest Route with Congestion: ", shortest_path)
print("Total Travel Time with Congestion: ", shortest_time)






