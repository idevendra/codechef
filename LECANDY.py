t = int(input())
while(t > 0):
	t -= 1
	n, c = list(map(int,input().split()))
	ar = list(map(int,input().split()))
	s = sum(ar)
	if s>c:
		print('No')
	else:
		flag = True
		for i in range(n):
			if ar[i] <= c:
				c -= ar[i]
			else:
				flag = False
				break
		if flag:
			print('Yes')
		else:
			print('No')

