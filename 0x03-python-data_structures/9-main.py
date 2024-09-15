#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
second_lis = []
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
print(max_integer(second_lis))
print(max_integer([1, 3, 2, 4, 5]))  # Should print 5
print(max_integer([1, 2, 3, 4, 5]))  # Should print 5
print(max_integer([-1, -2, -3, -4, -5]))  # Should print -1, but will print 0
print(max_integer([-10]))  # Should print -10, but will print 0
print(max_integer([]))  # Should print None
print(max_integer([3]))  # Should print 3
print(max_integer([0, 0, 0]))
