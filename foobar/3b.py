def solution(m, f):
	m = int(m)
	f = int(f)
	count = 0
	while (m != f):
		# print(m, f)
		if (m == 1):
			count += (f - m)		  #if either of them reaches 1 first, add the difference to the count and set the other one 1
			f = 1
			break
		elif(f == 1):
			count += (m - f)
			m = 1
			break
		x = max(m, f)
		y = min(m, f)
		if (x % y == 0):			  #if they aren't co-prime at any level it is impossible to reach the initial stage 
			return "impossible"		  
		temp = x % y;
		count += (x // y)
		if (m > f):
			m = temp                  #if m is greater m is replaced with the difference between the max and the min values
		else:
			f = temp                  #if f is greater f is replaced with the difference between the max and the min values
	if (m > 1 and f > 1):             #if the loop ends at a point where m and f is not at the initial stage, the case is impossible
		return "impossible"
	else:
		return str(count)

s = solution(8, 60)
print(s)