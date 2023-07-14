# Another diamond pattern of star
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
rows=int(input())              
for i in range(rows+1):
    print(" " * (rows - i) + "*" + " " * ((2*i)-1) + "*" * (i != 0))
for i in range(rows-1 , -1, -1):
    print(" " * (rows - i) + "*" + " " * ((2*i)-1) + "*" * (i != 0))
