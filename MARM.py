'''def solve_test(n, k, ar):
	for i in range(k):
		#print('k = ',i)
		a = i%n
		b = n-a-1
		ar[a] = (ar[a]^ar[b])
		print(ar)
'''

def solve(n, k ,ar):
	l = k%(n*3)
	if( (n%2 != 0) and (k>(n//2)) ):
		ar[n//2]=0
	for i in range(l):
		a = i%n
		b = n-a-1
		ar[a] = (ar[a]^ar[b])
	print((' '.join([str(x) for x in ar])).strip())

for t in range(int(input())):
	n, k = list(map(int,input().split()))
	ar = list(map(int,input().split()))
	solve(n, k, ar)