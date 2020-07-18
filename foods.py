my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
my_foods.append('my_test')
friend_foods.append('friend_test')
print(my_foods)
print(friend_foods)

another = ['aa', 'bb', 'cc']
copy = another
print('another: ', another)
print('copy:    ', copy)
copy.append('append')
print(another)
print(copy)

"""
If you just ust the =, you will find that if you 
change one of the val, the other will also be changed.
If you wants to copy the list, just use the cut operation.
"""
