for t in range(int(input())):
	n, m, q = list(map(int,input().split()))
	rows = [0]*n
	cols = [0]*m
	while(q>0):
		q -= 1
		r, c = list(map(int,input().split()))
		r, c = r-1, c-1
		rows[r] += 1
		cols[c] += 1
	r_e, r_o, c_e, c_o = 0, 0, 0, 0
	
	for i in range(n):
		if rows[i]&1:
			r_o += 1
		else:
			r_e += 1 

	for i in range(m):
		if cols[i]&1:
			c_o += 1
		else:
			c_e += 1 

	print((r_e*c_o)+(r_o*c_e))