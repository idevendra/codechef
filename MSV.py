def solve(ar, N):
	sieve = [False]*N
	ans = 0
	n = N-1
	while(n>=0):
		if sieve[n]:
			n -= 1
			continue
		else:
			temp = 0
			for i in reversed(range(n)):
				if (ar[i]%ar[n]) == 0:
					sieve[i] = True
					temp += 1
			ans = max(ans, temp)
			n -= 1
	print(ans)



for t in range(int(input())):
	n = int(input())
	ar = list(map(int,input().split()))
	solve(ar, n)