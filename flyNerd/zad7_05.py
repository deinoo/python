'''Display the Christmas tree from triangles (made of #) in such a way 
that each level of the Christmas tree is 1 row longer than the previous Christmas tree

#
##
#
##
###
#
##
###
####
'''

size = int(input('How many rows should be in first tree?: '))
counter = int(input('How many multiplication of tree is expected?: '))

for repeat in range (counter):
    None
    for tree in range(1,size+1):
        print ('#'*tree)
    size +=1
