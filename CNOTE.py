t = int(input())
while(t > 0):
	t -= 1
	x, y, k, n = list(map(int,input().split()))
	flag = False
	for i in range(n):
		p, c = list(map(int,input().split()))
		if not flag:
			if (y+p >= x) and (k>=c):
				flag = True
	if flag:
		print('LuckyChef')
	else:
		print('UnluckyChef')