# Pyramid pattern of numbers
n=int(input())
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=" ")
    print('')