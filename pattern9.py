# Print reverse number from 10 to 1
# 1
# 3 2
# 6 5 4
# 10 9 8 7

n=int(input())
num=0
for i in range(n//2):
    k=num+i
    for j in range(i):
        print(k,end=' ')
        n-=1
        num+=1
    print('')