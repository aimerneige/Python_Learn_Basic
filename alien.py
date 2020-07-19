alien_0 = {'color': 'green', 'points': 5}
# alien_0 = {
#     'color': 'green',
#     'points': 5
# }
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

# add a key-value
alien_0['added'] = False
print(alien_0)
print(alien_0['added'])

# create a empty dict
empty = {}
print(empty)
empty['key'] = 'value'
print(empty)

# you can also add list and dict
empty['list'] = ['a', 'b']

empty['dict'] = {
    'a': ['a', 'c'],
    'dic': {
        'test': 1,
        'li': [1, 2, 3]
    },
    'c': [
        {
            'a':False,
            'b':True
        },
        {
            'a':False,
            'b':False
        }
    ]
}
print(empty)