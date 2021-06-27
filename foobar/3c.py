def solution(l):
	count = c1 = c2 = 0
	for i in range(len(l)):
		for j in range(0, i):
			if (l[i] % l[j] == 0):
				c1 += 1
		for k in range(i+1, len(l)):
			if (l[k] % l[i] == 0):
				c2 += 1
		count += c1*c2
		c1 = c2 = 0
	return count


ans = solution([1,2,3,4,5,6])
print(ans)