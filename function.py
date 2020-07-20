def describe_pet(animal_type, pet_name):
    print('type: ', animal_type)
    print('name: ', pet_name)

describe_pet("dog", "Jack")

describe_pet(pet_name='harry', animal_type='cat')

"""
If you use the keyword to describe the parm
you can ignore the order of the parm but you
must make sure the parm name is right
"""

# default value

def describe_pet_1(pet_name, animal_type='dog'):
    print('type: ', animal_type)
    print('name: ', pet_name)

describe_pet_1('willie')

# if you don't wants the list to be changed
# give a copy but not a list

def change(some_list):
    """this function will changed list"""
    some_list[0] = 'Changed' # will change the original list

some_list = ['aaa', 'data']
change(some_list) # original list will be changed
change(some_list[:]) # original list will not be changed

def many_args(*manyargs):
    print(manyargs)
"""
when you use the * python will create a new tuple
if you do not know how many args you will get, use *
"""

many_args('aimer', 'neige', 'inory')
