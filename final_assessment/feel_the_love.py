#
# Take a weighted graph representing a social network where the weight
# between two nodes is the "love" between them.  In this "feel the
# love of a path" problem, we want to find the best path from node `i`
# and node `j` where the score for a path is the maximum love of an
# edge on this path. If there is no path from `i` to `j` return
# `None`.  The returned path doesn't need to be simple, ie it can
# contain cycles or repeated vertices.
#
# Devise and implement an algorithm for this problem.
#

import heapq
from collections import defaultdict

def feel_the_love(G, i, j):
	# return a path (a list of nodes) between `i` and `j`,
	# with `i` as the first node and `j` as the last node,
	# or None if no path exists
	path = dijkstra_path(G, i)
	if not j in path:
		return None

	node_a, node_b = max_weight_edge(G, i)
	path_a = path[node_a]
	path_b = (dijkstra_path(G, node_b))[j]

	return path_a + path_b

def max_weight_edge(G, i):
	max_so_far = -float('inf')
	edge       = None
	reachable  = dijkstra_path(G, i)
	for node in G:
		for neighbor in G[node]:
			if (G[node])[neighbor] > max_so_far and node in reachable:
				max_so_far = (G[node])[neighbor]
				edge = node, neighbor

	return edge

def dijkstra_path(HG, v):
	dist_so_far = {v: 0}
	final_dist = {}
	final_path = defaultdict(list)
	heap = [(0, v)]
	while dist_so_far:
		(w, k) = heapq.heappop(heap)
		if k in final_dist or (k in dist_so_far and w > dist_so_far[k]):
			continue
		else:
			del dist_so_far[k]
			final_dist[k] = w
		for neighbor in [nb for nb in HG[k] if nb not in final_dist]:
			nw = final_dist[k]+ HG[k][neighbor]
			final_path[neighbor] = final_path[k] + [k]

			if neighbor not in dist_so_far or nw < dist_so_far[neighbor]:
				dist_so_far[neighbor] = nw
				heapq.heappush(heap, (nw, neighbor))

	for node in final_path:
		final_path[node] += [node]
	return final_path

#########
#
# Test

def score_of_path(G, path):
	max_love = -float('inf')
	for n1, n2 in zip(path[:-1], path[1:]):
		love = G[n1][n2]
		if love > max_love:
			max_love = love
	return max_love

def test():
	G = {'a':{'c':1},
		 'b':{'c':1},
		 'c':{'a':1, 'b':1, 'e':1, 'd':1},
		 'e':{'c':1, 'd':2},
		 'd':{'e':2, 'c':1},
		 'f':{}}
	path = feel_the_love(G, 'a', 'b')
	assert score_of_path(G, path) == 2

	path = feel_the_love(G, 'a', 'f')
	assert path == None

if __name__ == '__main__':
	test()
	print "Test passes"