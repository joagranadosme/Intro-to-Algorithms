#
# In lecture, we took the bipartite Marvel graph,
# where edges went between characters and the comics
# books they appeared in, and created a weighted graph
# with edges between characters where the weight was the
# number of comic books in which they both appeared.
#
# In this assignment, determine the weights between
# comic book characters by giving the probability
# that a randomly chosen comic book containing one of
# the characters will also contain the other
#

import itertools
from collections import defaultdict
import cPickle

marvel     = cPickle.load(open("smallG.pkl"))
characters = cPickle.load(open("smallChr.pkl"))

def create_weighted_graph(bipartiteG, characters):
	G = defaultdict(dict)
	for char_a, char_b in itertools.combinations(characters, 2):
		a_books = set(bipartiteG[char_a])
		b_books = set(bipartiteG[char_b])

		inter_book_num = float(len(a_books.intersection(b_books)))
		if inter_book_num == 0:
			continue

		prob = inter_book_num / (len(a_books)+len(b_books)-inter_book_num)
		G[char_a][char_b] = prob
		G[char_b][char_a] = prob

	return G

######
#
# Test

def test():
	bipartiteG = {'charA':{'comicB':1, 'comicC':1},
				  'charB':{'comicB':1, 'comicD':1},
				  'charC':{'comicD':1},
				  'comicB':{'charA':1, 'charB':1},
				  'comicC':{'charA':1},
				  'comicD': {'charC':1, 'charB':1}}
	G = create_weighted_graph(bipartiteG, ['charA', 'charB', 'charC'])
	# three comics contain charA or charB
	# charA and charB are together in one of them
	assert G['charA']['charB'] == 1.0 / 3
	assert G['charA'].get('charA') == None
	assert G['charA'].get('charC') == None

def test2():
	G = create_weighted_graph(marvel, characters)

if __name__ == '__main__':
	test()
	test2()
	print "Test passes"