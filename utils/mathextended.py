def bigSum(start, end, f): # f passed as lambda
	s=0
	if start > end:
		return s
	for i in range(start, end+1):
		s+= f(i)
	return s
def bigProduct(start, end, f):
	p = 1
	if start > end:
		return 0
	for i in range(start, end+1):
		p*= f(i)
	return p