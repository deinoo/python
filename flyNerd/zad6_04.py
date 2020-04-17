'''Create a lists of male and female names. Ask user to provide name. Check if the name is male or female and display information on this topic. 
If the name is not on the list, display the message "We don't know that name." Then the user will provide information on whether the name is male or female. Add the name to the list and print list.'''

male = ['Jan', 'Stanisław', 'Andrzej', 'Józef', 'Tadeusz']
female = ['Maria', 'Krystyna', 'Anna', 'Barbara', 'Teresa', ]
name = input ('Provide name to verify:')
name = name.capitalize()
sex = None

def check_sex(name):
    if name[-1] == 'a':
        print('{} is female name'.format(name))
        sex = 0
    else:
        print('{} is male name'.format(name))
        sex = 1
    return sex

def check_on_list(name):

    def add_to_list(name, sex_user):
        if sex_user == 'M':
            male.append(name)
            print(male)
        else:
            female.append(name)
            print(female)

    if sex == 1:
        if name not in male:
            sex_user = input(
                'Ooohh.. we don\'t know that name. What sex is for {}: M(ale) or F(emale)? Suggested is M(ale)'.format(
                    name))
            add_to_list(name, sex_user)
    else:
        if name not in female:
            sex_user = input(
                'Ooohh.. we don\'t know that name. What sex is for {}: M(ale) or F(emale)? Suggested is F(emale)'.format(
                    name))
            add_to_list(name, sex_user)


sex = check_sex(name)
check_on_list(name)
