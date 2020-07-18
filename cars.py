# sort()

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

"""
You can sort a list using sort()
Use the reverse arg to reverse the sort
Notice that if you sort a list, it can't be recover
"""

# sorted()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))
"""
After using sorted() the list will not be changed
Also, you can use the arg reverse
"""

# reverse()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
"""
The reverse() just reverse the list with it original sort
It does not contain the sort funcion
"""

# len()

cars = ['bmw', 'audi', 'toyota', 'subaru']
num = len(cars)
print(num)
"""
just get the length of the list
"""