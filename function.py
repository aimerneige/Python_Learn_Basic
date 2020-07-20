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
