# In the lecture, we described how a solution to k_clique_decision(G, k)
# can be used to solve independent_set_decision(H,s).
# Write a Python function that carries out this transformation.

# Returns a list of all the subsets of a list of size k
def k_subsets(lst, k):
	if len(lst) < k:
		return []
	if len(lst) == k:
		return [lst]
	if k == 1:
		return [[i] for i in lst]
	return k_subsets(lst[1:],k) + map(lambda x: x + [lst[0]], k_subsets(lst[1:], k-1))

# Checks if the given list of nodes forms a clique in the given graph.
def is_clique(G, nodes):
	for pair in k_subsets(nodes, 2):
		if pair[1] not in G[pair[0]]:
			return False
	return True

# Determines if there is clique of size k or greater in the given graph.
def k_clique_decision(G, k):
	nodes = G.keys()
	for i in range(k, len(nodes) + 1):
		for subset in k_subsets(nodes, i):
			if is_clique(G, subset):
				return True
	return False

def make_link(G, node1, node2):
	if node1 not in G:
		G[node1] = {}
	(G[node1])[node2] = 1
	if node2 not in G:
		G[node2] = {}
	(G[node2])[node1] = 1
	return G

def break_link(G, node1, node2):
	if node1 not in G:
		print "error: breaking link in a non-existent node"
		return
	if node2 not in G:
		print "error: breaking link in a non-existent node"
		return
	if node2 not in G[node1]:
		print "error: breaking non-existent link"
		return
	if node1 not in G[node2]:
		print "error: breaking non-existent link"
		return
	del G[node1][node2]
	del G[node2][node1]
	return G

def reform_graph(G):
	total_nodes = {}
	new_graph   = {}
	for node in G:
		total_nodes[node] = True

	for node in G:
		for x in total_nodes:
			if x != node and x not in G[node]:
				make_link(new_graph, node, x)

	return new_graph

# This function should use the k_clique_decision function
# to solve the independent set decision problem
def independent_set_decision(H, s):
	return k_clique_decision(reform_graph(H), s)

if __name__ == '__main__':
	flights = [(1,2),(1,3),(2,3),(2,6),(2,4),(2,5),(3,6),(4,5)]
	G = {}
	for (x,y) in flights:
		make_link(G,x,y)

	for node in G:
		print node, "--",
		for x in G[node]:
			print x,
		print

	print
	print "independent set:"
	for i in range(1, len(flights)):
		print i, "-" , independent_set_decision(G, i)