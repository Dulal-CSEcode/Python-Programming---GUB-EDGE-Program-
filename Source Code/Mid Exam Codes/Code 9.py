tuples_list = [(3, 'a'), (2, 'b'), (1, 'c')]
dictionary = dict(tuples_list)
sorted_dict = dict(sorted(dictionary.items()))

print("Original dictionary:", dictionary)
print("Sorted dictionary:", sorted_dict)