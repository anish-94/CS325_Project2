with open("tsp_example.txt") as f:
	cities = []
	data = []
	for line in f.readlines():
		data = line.split(" ")
		data = [x.strip() for x in data]
		cities.append(data)	

print(cities[:])
