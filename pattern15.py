# Right triangle pyramid of Stars
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

n=int(input())
for i in range(n+1):
    print(' '*(n-i)+'*'*i)