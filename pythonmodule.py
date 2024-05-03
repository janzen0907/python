
def greet_users(names):
    '''Says hello to a list of users'''
    for name in names:
        print(name)

# Keep in mind a function gets the same reference to a list
def delete_bob(names):
    '''Don't like bob, need to remove him'''
    while 'Bob' in names:
        names.remove('Bob')
    print("The post bob list is: ", names)

def change_name(name):
    '''Changes teh name to Bob'''
    name = 'Bob'
    print(f'The name is now {name}')

# Pass in a arbritrary number of argumenst, but not in a list
# You can make an parameter a tuple with *
def display_users(*users):
    '''Prints out the users'''
    for user in users:
        print(f'User: {user}')
    print(users)


# If you mix positional with arbitrary ones, the arbitrary ones have to come last
# People will call this 'collector' arguments * args
def create_pizza(size, *toppings):
    '''Creates a pizza string'''
    pizza_string = f'{size} pizza with'
    for topping in toppings:
        pizza_string += f'\n{topping}'
    return pizza_string


# Instead of accepting a tuple you can instead set a arbitary set of key value pairs as a dict
# use ** for that 
# Often you'll see **kwargs used to collect nonspecific argumes
def create_user_profile(first, last,**user_info):
    '''Creates a user profile'''
    user_info['name'] = first + last
    return user_info

print('code in the file was run')




