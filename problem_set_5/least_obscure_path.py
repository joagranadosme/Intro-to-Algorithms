# -*- coding: utf-8 -*-
#
# Another way of thinking of a path in the Kevin Bacon game
# is not about finding *short* paths, but by finding paths
# that don’t use obscure movies.  We will give you a
# list of movies along with their obscureness score.
#
# For this assignment, we'll approximate obscurity
# based on the multiplicative inverse of the amount of
# money the movie made. Though, its not really important where
# the obscurity score came from.
#
# Use the the imdb-1.tsv and imdb-weights.tsv files to find
# the obscurity of the “least obscure”
# path from a given actor to another.
# The obscurity of a path is the maximum obscurity of
# any of the movies used along the path.
#
# You will have to do the processing in your local environment
# and then copy in your answer.
#
# Hint: A variation of amended_Dijkstra can be used to solve this problem.
#

# Change the `None` values in this dictionary to be the obscurity score
# of the least obscure path between the two actors

answer = {(u'Boone Junior, Mark', u'Del Toro, Benicio'): None,
		  (u'Braine, Richard', u'Coogan, Will'): None,
		  (u'Byrne, Michael (I)', u'Quinn, Al (I)'): None,
		  (u'Cartwright, Veronica', u'Edelstein, Lisa'): None,
		  (u'Curry, Jon (II)', u'Wise, Ray (I)'): None,
		  (u'Di Benedetto, John', u'Hallgrey, Johnathan'): None,
		  (u'Hochendoner, Jeff', u'Cross, Kendall'): None,
		  (u'Izquierdo, Ty', u'Kimball, Donna'): None,
		  (u'Jace, Michael', u'Snell, Don'): None,
		  (u'James, Charity', u'Tuerpe, Paul'): None,
		  (u'Kay, Dominic Scott', u'Cathey, Reg E.'): None,
		  (u'McCabe, Richard', u'Washington, Denzel'): None,
		  (u'Reid, Kevin (I)', u'Affleck, Rab'): None,
		  (u'Reid, R.D.', u'Boston, David (IV)'): None,
		  (u'Restivo, Steve', u'Preston, Carrie (I)'): None,
		  (u'Rodriguez, Ramon (II)', u'Mulrooney, Kelsey'): None,
		  (u'Rooker, Michael (I)', u'Grady, Kevin (I)'): None,
		  (u'Ruscoe, Alan', u'Thornton, Cooper'): None,
		  (u'Sloan, Tina', u'Dever, James D.'): None,
		  (u'Wasserman, Jerry', u'Sizemore, Tom'): None}

# Here are some test cases.
# For example, the obscurity score of the least obscure path
# between 'Ali, Tony' and 'Allen, Woody' is 0.5657
test = {
		#(u'Ali, Tony', u'Allen, Woody'): 0.5657,
		(u'Auberjonois, Rene', u'MacInnes, Angus'): 0.0814,
		(u'Avery, Shondrella', u'Dorsey, Kimberly (I)'): 0.7837,
		(u'Bollo, Lou', u'Jeremy, Ron'): 0.4763,
		(u'Byrne, P.J.', u'Clarke, Larry'): 0.109,
		(u'Couturier, Sandra-Jessica', u'Jean-Louis, Jimmy'): 0.3649,
		#(u'Crawford, Eve (I)', u'Cutler, Tom'): 0.2052,
		(u'Flemyng, Jason', u'Newman, Laraine'): 0.139,
		(u'French, Dawn', u'Smallwood, Tucker'): 0.2979,
		(u'Gunton, Bob', u'Nagra, Joti'): 0.2136,
		(u'Hoffman, Jake (I)', u'Shook, Carol'): 0.6073,
		#(u'Kamiki, Ry\xfbnosuke', u'Thor, Cameron'): 0.3644,
		(u'Roache, Linus', u'Dreyfuss, Richard'): 0.6731,
		(u'Sanchez, Phillip (I)', u'Wiest, Dianne'): 0.5083,
		(u'Sheppard, William Morgan', u'Crook, Mackenzie'): 0.0849,
		(u'Stan, Sebastian', u'Malahide, Patrick'): 0.2857,
		(u'Tessiero, Michael A.', u'Molen, Gerald R.'): 0.2056,
		(u'Thomas, Ken (I)', u'Bell, Jamie (I)'): 0.3941,
		(u'Thompson, Sophie (I)', u'Foley, Dave (I)'): 0.1095,
		(u'Tzur, Mira', u'Heston, Charlton'): 0.3642}

import csv
from collections import defaultdict
import itertools
import heapq


def read_obscurity(filename):
	tsv = csv.reader(open(filename), delimiter='\t')
	movie_obscurity = {}
	for movie, year, obscurity in tsv:
		movie_obscurity[movie+"-"+year] = obscurity

	return movie_obscurity

def make_link(G, x, y, val):
	G[x][y] = val
	G[y][x] = val

def read_graph(filename):
	tsv = csv.reader(open(filename), delimiter='\t')
	G = defaultdict(dict)

	for actor, movie, year in tsv:
		make_link(G, actor, movie+"-"+year, True)
	return G

def make_hop_graph(G, obscurities):
	HG = defaultdict(dict)
	for movie in obscurities:
		if movie not in G: continue
		for actors in itertools.combinations(G[movie], 2):
			make_link(HG, actors[0], actors[1], obscurities[movie])
	return HG

def amended_dijkstra(HG, v):
	dist_so_far = {v: 0}
	final_dist = {}
	heap = [(0, v)]
	while dist_so_far:
		(w, k) = heapq.heappop(heap)
		if k in final_dist or (k in dist_so_far and w > dist_so_far[k]):
			continue
		else:
			del dist_so_far[k]
			final_dist[k] = w
		for neighbor in [nb for nb in HG[k] if nb not in final_dist]:
			nw = max(final_dist[k], HG[k][neighbor])
			if neighbor not in dist_so_far or nw < dist_so_far[neighbor]:
				dist_so_far[neighbor] = nw
				heapq.heappush(heap, (nw, neighbor))
	return final_dist

def solve(graph, actor_0, actor_1):

	return amended_dijkstra(graph, actor_0)[actor_1]

if __name__ == '__main__':
	total_graph = read_graph("imdb-1.tsv")
	movie_obscurity = read_obscurity("imdb-weights.tsv")

	HG = make_hop_graph(total_graph, movie_obscurity)

	print "answer = {"
	for ch1, ch2 in answer:
		#ch1, ch2 = t[0], t[1]
		#routes = amended_dijkstra(HG, ch1)
		answer[ch1, ch2] = solve(HG, ch1, ch2)

		print '\t(\"' + ch1 + '\", \"'+ ch2 +'\"):', answer[ch1, ch2], ","
	print "}"