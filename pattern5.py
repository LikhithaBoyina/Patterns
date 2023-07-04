# Alternate numbers pattern using while loop
# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(i+i+1,end=' ')
    print('')