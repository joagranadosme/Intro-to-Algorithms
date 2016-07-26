import itertools

if __name__ == '__main__':
	color = [0, 1, 2]
	A, B, C, D, E, F, G, H = next((A, B, C, D, E, F, G, H)
		for (A, B, C, D, E, F, G, H) in itertools.product(color, repeat=8)
		if not (A is B or A is C)
		if not (B is C or B is D)
		if not (C is D)
		if not (D is E or D is F)
		if not (E is G or E is F)
		if not (F is G or F is H)
		if not (G is H))

	print "D + F + C * (G-A) + H =", D + F + C * (G-A) + H