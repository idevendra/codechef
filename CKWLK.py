import math
t = int(input())
while(t>0):
	t-=1
	n = int(input())
	if (n%10)!=0:
		print('No')
	else:
		c=0
		while((n%10)==0):
			n=n//10
			c+=1
		if n==1:
			print('Yes')
		else:
			if math.log(n,2)==int(math.log(n,2)):
				if c>=math.log(n,2):
					print('Yes')
				else:
					print('No')
			else:
				print('No')
