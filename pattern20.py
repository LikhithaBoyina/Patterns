# Print two pyramids of stars
# *  
# * *  
# * * *  
# * * * *  
# * * * * *  
# * * * * * *  
 
# * * * * * *  
# * * * * *  
# * * * *  
# * * *  
# * *  
# *  

n=int(input())
for i in range(n+1):
    print('* '*i)
print()
for j in range(n,-1,-1):
    print('* '*j)