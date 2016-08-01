import decimal

decimal.getcontext().prec = 100

def polynomial(x):
	return decimal.Decimal(x)**100

def exponential(x):
	return (decimal.Decimal(11)/decimal.Decimal(10))**x

def differ(x):
	return exponential(x) - polynomial(x)

if __name__ == '__main__':
	n    = 2
	step = 1
	while differ(n) < 0:
		n    += step
		step *= 2

	lower = n - step/2
	upper = n

	while True:
		n = int((upper+lower) /2)
		if differ(n-1) * differ(n) < 0:
			break

		if differ(n) > 0:
			upper = n
		else:
			lower = n

	print "n =", n