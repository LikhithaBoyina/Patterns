# Inverted Pyramid pattern with the same digit
# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5
n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print(n,end='')
    print('')