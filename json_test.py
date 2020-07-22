import json

numbers = [1, 2, 3, 4, 5, 6, 7]

filename = 'numbers.json'
with open(filename, 'w') as file_obj:
    json.dump(numbers, file_obj)

dic_test = {
    'first': "hello",
    'list': [1, 2, 3, 4],
    'dic': {
        'list': [
            {
                'a': True,
                'b': False
            },
            {
                'c': True,
                'd': False
            },
            {
                'e': True,
                'f': False
            }
        ]
    }
}

with open('dic_test.json', 'w') as file_obj:
    json.dump(dic_test, file_obj)