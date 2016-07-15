# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):

	def _next_node(edge, current):
		return edge[0] if current == edge[1] else edge[1]

	def _remove_edge(raw_list, discard):
		return [item for item in raw_list if item != discard]

	search = [[[], graph[0][0], graph]]
	while search:
		path, node, unexplore = search.pop()
		path += [node]

		if not unexplore:
			return path

		for edge in unexplore:
			if node in edge:
				search += [[path, _next_node(edge, node), _remove_edge(unexplore, edge)]]

if __name__ == '__main__':
	graph = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 3)]
	print find_eulerian_tour(graph)