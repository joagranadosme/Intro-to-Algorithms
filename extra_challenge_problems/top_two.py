#
# write a function, `top_two` that takes in a graph and a starting
# node and returns two paths, the first and second shortest paths,
# for all the other nodes in the graph.  You can assume that the
# graph is connected.
#

import heapq
from collections import defaultdict

def top_two(graph, start, topX=2):
	heap = [((0, [start]), start)]
	best = defaultdict(list)
	best[start] = [(0, [start])]
	while heap:
		((cost, path), node) = heapq.heappop(heap)
		for (other, weight) in graph[node].items():
			if other in path:
				continue

			new = (cost + weight, path + [other])
			best[other] = sorted(best[other] + [new])[:topX]
			if new in best[other]:
				heapq.heappush(heap, (new, other))

	return best

def test():
	graph = {'a':{'b':3, 'c':4, 'd':8},
			 'b':{'a':3, 'c':1, 'd':2},
			 'c':{'a':4, 'b':1, 'd':2},
			 'd':{'a':8, 'b':2, 'c':2}}
	result = top_two(graph, 'a') # this is a dictionary
	b = result['b'] # this is a list
	b_first = b[0] # this is a list
	assert b_first[0] == 3 # the cost to get to 'b'
	assert b_first[1] == ['a', 'b'] # the path to 'b'
	b_second = b[1] # this is a list
	assert b_second[0] == 5 # the cost to get to 'b'
	assert b_second[1] == ['a', 'c', 'b']

if __name__ == '__main__':
	test()
	print "Test passes"