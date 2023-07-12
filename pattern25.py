# Pant style pattern of stars
#        * 
#       * * 
#      * * * 
#     * * * * 
#    * * * * * 
#   * * * * * * 
#    * * * * * 
#     * * * * 
#      * * * 
#       * * 
#        * 
n=int(input())
k=2*n-2
for i in range(n):
    print(' '*(k)+'* '*i)
    k=k-1
for j in range(n,0,-1):
    print(' '*(k)+'* '*j)
    k=k+1
