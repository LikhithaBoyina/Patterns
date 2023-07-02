l=list(map(int,input().split()))
t=int(input())
for i in range(len(l)):
	p=t-l[i]
	if p in l:
		print(l.index(p),i)
	else:
		print("Not found")