# Let the user enter any number of names with a string (e.g. as one string separated by 
# a comma or white space). Then welcome each person on the list.

user_names = input('Provide list of names separated by "," or spaces: ')
#user_names = 'john adela amelia peter, Miranda, Helmut, Bob Mery cherry Bartek'
user_names =user_names.replace(' ',',').replace(',,',',')
user_list =  user_names.split(',')

for names in user_list:
    print ('Hello, {}!'.format(names.capitalize()))
