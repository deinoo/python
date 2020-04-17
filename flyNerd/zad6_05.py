#Based on provided length a, b, c - check
#- find longest arm
#- are they the arms of the triangle
#- is the Pythagorean triangle
#- is it an Egyptian triangle

all_arms = []
a=int(input('Provide length of 1st triangle arm: '))
b=int(input('Provide length of 1st triangle arm: '))
c=int(input('Provide length of 1st triangle arm: '))

all_arms = all_arms + [a] + [b] + [c]

def find_longest_arm(all_arms, max_long):
    for number in all_arms:
        if number  > max_long:
            max_long = number
    return max_long

def check_triangle_possibility(all_arms):
    all_arms.sort()
    if all_arms[2]==max_long:
        print (all_arms[2] < all_arms[0]+all_arms[1])
        if all_arms[2] < all_arms[0]+all_arms[1]:
            return True
        else:
            return False

def pythagorean_egyptian_triangle(what_triangle):
    if all_arms[2]**2 == all_arms[0]**2 + all_arms[1]**2:
        if ((all_arms[0]%3==0) and  (all_arms[1]%4==0) and (all_arms[2]%5==0)):
            return ('egyptian_triangle')
        return ('pythagorean_triangle')
    else:
        return ('not_pythagorean_triangle')

max_long =0
max_long=find_longest_arm(all_arms, max_long)

correct_triangle = check_triangle_possibility(all_arms)
print ('Do we can made a triangle from  {} {} {}? {}'.format(a,b,c,correct_triangle))
if correct_triangle == True:
    print('Yes, we can make triangle from  {} {} {}!'.format(a,b,c))
else:
    raise SystemExit("With provided numbers we can't construct a triangle, sorry")

what_triangle = pythagorean_egyptian_triangle(all_arms)
if what_triangle == 'pythagorean_triangle':
    print ('This is pythagorean triangle!')
elif what_triangle == 'egyptian_triangle':
    print ('This is egyptian triangle!')
else:
    print ('This is NOT pythagorean nor egyptian triangle')