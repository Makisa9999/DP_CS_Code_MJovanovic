multi_list = [["a", 2, 4], ["b", 1, 3], ["c", 0, 2]]

sorted_multi_list = sorted(multi_list, key=lambda x: x[2])

print(sorted_multi_list)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
number = lambda x : x + 10
print(number(5))