# Simple half pyramid pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

n=int(input())
for i in range(n+1):
    for j in range(i):
        print('*',end=' ')
    print(' ')