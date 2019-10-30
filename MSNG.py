for t in range(int(input())):
	n = int(input())
	ar = []
	for i in range(n):
		base, value = list(map(int,input().split()))
		ar.append([base, value])

	flag = False
	base = 0
	value = 0
	
	for i in range(n):
		if ar[i][0] != -1:
			flag = True
			base = ar[i][0]
			value = ar[i][1]
			break

	if flag:
		for b in range(2,37):
			
		print()
	else:
		print('45')




