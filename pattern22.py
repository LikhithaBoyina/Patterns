# Left triangle pascal’s pattern
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

n=int(input())
for i in range(n):
    print('  '*(n-i)+'* '*i)
for j in range(n,-1,-1):
    print('  '*(n-j)+'* '*j)