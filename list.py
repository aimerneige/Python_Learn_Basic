list_test = ['Aimer', 'Neige', 'Inory', 'aimer neige']
print(list_test)

# access with index
print(list_test[0])
print(list_test[1])
print(list_test[-1])
print(list_test[-2])
print(list_test[-1].title())
print("===")
for item in list_test:
    print(item)
print("===")


print(list_test)

# edit item
list_test[-1] = 'Sayori'
print(list_test)

# add item
## append
list_test.append('Natsuki')
list_test.append('Monika')
print(list_test)
## insert
list_test.insert(0, 'Insert')
print(list_test)
list_test.insert(1, 'Yuri')
print(list_test)

# delete item
## use del to delete with index
del list_test[1]
print(list_test)
del list_test[0]
print(list_test)
## use pop
### pop without index
popped = list_test.pop()
print(popped) # when you use pop you can still use the item deleted
print(list_test)
### pop with index
first = list_test.pop(0)
print('first:\t', first)
print(list_test)
"""
if you wants to delete a item and will not use it again just use the del
but if you wants to use it after delete it, use pop to delete it and save
it on a temp var
"""
## delete with value
list_test.remove('Inory')
print(list_test)
"""
Note that if there is not only one key with the value
the remove() will only delete the first value
"""

