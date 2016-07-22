from collections import defaultdict
import sys
import csv

def make_link(G, node1, node2):
	(G[node1])[node2] = 1
	(G[node2])[node1] = 1

def average_centrality(G, v):
	distance_from_start    = {}
	distance_from_start[v] = 0
	open_list = [v]

	while len(open_list) > 0:
		current = open_list.pop(0)
		for neighbor in G[current].keys():
			if neighbor not in distance_from_start:
				distance_from_start[neighbor] = distance_from_start[current] + 1
				open_list.append(neighbor)
	return (float(sum(distance_from_start.values())))/len(distance_from_start)

def read_graph(filename):
	actor_list = {}
	movie_graph = defaultdict(dict)

	for actor, movie, year in csv.reader(open(filename), delimiter='\t'):
		make_link(movie_graph, actor, movie+year)
		actor_list[actor] = True

	count = 0
	list_len = len(actor_list)
	centrality_dict = {}

	for actor in actor_list:
		centrality_dict[actor] = average_centrality(movie_graph, actor)
		count += 1
		sys.stdout.flush()
		sys.stdout.write("\rstatus: {:6.2f}%".format(100.0 * count / list_len))

	print
	print
	return centrality_dict

if __name__ == '__main__':
	for item in sorted(read_graph("IMDB-1.tsv").items(), key=lambda x: x[1])[:20]:
		print item