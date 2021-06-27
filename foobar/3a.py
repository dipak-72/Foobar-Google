from fractions import Fraction as frac, gcd

def mul(A, B):
	#A and B matrix is multiplied and the result is returned

	C = [[sum(x*y for x,y in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
	return C

def identity(m):
	#Identity matrix of size m x m is returned

	I = []
	for i in range(m):
		I.append([])
		for j in range(m):
			if (i == j):
				I[i].append(1)
			else:
				I[i].append(0)
	return I

def invertMatrix(m):
	# Matrix inversion using gauss jordan elimination

	rows = len(m)
	cols = len(m[0])
	im = identity(rows)
	
	for j in range(cols):
		divisor = m[j][j]
		for k in range(cols):
			m[j][k] /= divisor
			im[j][k] /= divisor
		for i in range(rows):
			if i is j:
				continue
			else:
				x = m[i][j]
				for k in range(cols):
					m[i][k] = m[i][k] - x*m[j][k]
					im[i][k] = im[i][k] - x*im[j][k]
	return im

def lcm(lcmlist):
	#lcm of the numbers from the list 

	result = 1
	for x in lcmlist:
		result *= x // gcd(result, x)
	return result

def solution(l):
	#main-function
	
	transientState = []
	absorbingState = []
	total = []
	P = []

	for row in range(len(l)):
		t = 0
		for col in range(len(l[row])):
			t += l[row][col]
		total.append(t)
		if (t == 0):
			absorbingState.append(row)
		else:
			transientState.append(row)
	
	if 0 in absorbingState:
		output = [0] * len(absorbingState)
		output[0] = 1
		output.append(1)
		return output

	for row in range(len(l)):
		P.append([])
		for col in range(len(l[row])):
			if (total[row] != 0):
				f = frac(l[row][col], total[row])
				P[row].append(f)
			else:
				P[row].append(frac(l[row][col], 1))

	Q = []
	for row in transientState:
		temp = []
		for col in transientState:
			temp.append(P[row][col])
		Q.append(temp)

	R = []
	for row in transientState:
		temp = []
		for col in absorbingState:
			temp.append(P[row][col])
		R.append(temp)

	I = identity(len(transientState))

	M = []
	for i in range(len(Q)):
		M.append([])
		for j in range(len(Q)):
			M[i].append(I[i][j] - Q[i][j])

	F = invertMatrix(M)

	limitMatrix = mul(F, R)
	
	commonDenominator = lcm([x.denominator for x in limitMatrix[0]])
	
	output = []
	for x in limitMatrix[0]:
		temp = commonDenominator // x.denominator
		output.append(x.numerator * temp)

	output.append(commonDenominator)

	return output

pro = solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
print(pro)