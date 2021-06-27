def solution(L):
	total = sum(L)
	if (total < 3):
		return 0
	L.sort(reverse = True)
	rem = total % 3
	flag = 0
	last = len(L) - 1
	if (rem != 0):
		for i in range(last, -1, -1):
			if (L[i] % 3 == rem):
				L.remove(L[i])
				flag = 1
				break
		if (flag == 0):
			rem = 3 - rem
			count = 0
			for i in range(last, -1, -1):
				if (L[i] % 3 == rem):
					L.remove(L[i])
					count = count + 1
				if (count == 2):
						break
	if (len(L) == 0):
		return 0
	ans = L[0]
	for i in range(len(L) - 1):
		ans = ans * 10 + L[i + 1]
	return ans

result = solution([7, 1, 1, 1, 0, 0])
print(result)