# Inverted pyramid pattern of numbers
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print(n-i+1,end=' ')
    print('')
