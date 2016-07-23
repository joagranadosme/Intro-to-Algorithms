import csv
import itertools
from collections import defaultdict

def read_graph(filename):
	tsv = csv.reader(open(filename), delimiter='\t')
	marvel_graph = defaultdict(list)
	for character, book in tsv:
		marvel_graph[book] += [character]

	return marvel_graph

def compute_strength(graph):
	strength_dict = defaultdict(int)
	for book in graph:
		for char_0, char_1 in itertools.combinations(graph[book], 2):
			strength_dict[max(char_0, char_1), min(char_0, char_1)] += 1

	return strength_dict

if __name__ == '__main__':
	strength_dict = compute_strength(read_graph("Marvel-Graph.tsv"))
	print max(strength_dict.items(), key=lambda x: x[1])