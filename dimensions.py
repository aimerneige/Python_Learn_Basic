dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
"""
Different from the list, the tuple's value is can't be changed.
"""
# dimensions[0] = 250
# This operation is not allowed!!!
# You can't changed the value of the tuple.
"""
Traceback (most recent call last):
  File "/home/aimerneige/Code/Python/Python_Learn/dimensions.py", line 7, in <module>
    dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment
"""

# You can also traversal the tuple like the list
for dimension in dimensions:
    print(dimension)

# If you wants to edit the value, you can only redefine the tuple
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)