# Right start pattern of star
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

n=int(input())
for i in range(n):
    print('* '*i)
for j in range(n,-1,-1):
    print('* '*j)