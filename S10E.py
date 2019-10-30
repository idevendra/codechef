for _ in range(int(input())):
	n = int(input())
	p = list(map(int,input().split()))
	ans = 1
	for i in range(1,n):
		flag = True
		for j in range(max(0,i-5),i):
			if p[j] <= p[i]: # strictly smaller!!!!!!!!!!!!!!!!!!!!!!!!!!s
				flag = False
				break
		if flag:
			ans += 1
	print(ans)