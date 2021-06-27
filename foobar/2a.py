def solution(x, y):
	ordinate = (x * (x + 1)) / 2
	abscissa = ordinate
	y = y - 1
	abscissa = ((2 * x + (y - 1)) * y) / 2
	abscissa = abscissa + ordinate
	return str(int(abscissa))

result = solution(5, 10)
print(result)