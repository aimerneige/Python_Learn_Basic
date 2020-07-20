def many_args(*manyargs):
    print(manyargs)
"""
when you use the * python will create a new tuple
if you do not know how many args you will get, use *
"""

many_args('aimer', 'neige', 'inory')
many_args(['aimer', 'neige', 'inory'])


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name']  = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Aimer', 'Neige',
                            location='China',
                            field='Computer')

print(user_profile)

"""
if you wants to get key-value data and don't know
how many and what the data is use the "**"
"""
