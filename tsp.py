from math import sqrt						# Github concreated.
import sys

def B(start, X, end, graph):
	
	if X == set():
		return graph[start][end]
	else:
		return min([B(start, X.difference(set([x])), x, graph) + graph[x][end] for x in X])

def TSP(num_nodes, graph):
#	print "hi im here"
	C = set(range(num_nodes))
	return min([B(0, C.difference(set([0,t])), t, graph) + graph[t][0] for t in C.difference(set([0]))])

def main():	

	with open("tsp_example_1.txt") as f:
		cities = []
		data = []
		for line in f.readlines():
			data = line.split(" ")
			data = [x.strip() for x in data]
			data = map(int, data)
			cities.append(data)	

	maxLen = len(cities)
	eucArr = [[None for i in range(maxLen)] for j in range(maxLen)]

	i = 0
	while i < len(cities):
		j = 0
		while j < len(cities):
			dx = cities[i][1] - cities[j][1]
			dy = cities[i][2] - cities[j][2]
			eucArr[i][j] = int(round(sqrt(dx**2 + dy**2)))
			j += 1
		i += 1

	maxval = TSP(maxLen, eucArr)
	print maxval


main()

#with open("tsp_example_1.txt.tour") as f:
	
