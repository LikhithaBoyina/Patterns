# Another inverted half pyramid pattern with number
# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1        


n=int(input())
for i in range(n,0,-1):
    for j in range(i,-1,-1):
        print(i-j,end=' ')
    print('')
