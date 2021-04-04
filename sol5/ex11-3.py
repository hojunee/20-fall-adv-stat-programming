def print_hist(my_dict):
    key_set = sorted(my_dict.keys())
    for x in key_set:
        print(x, my_dict[x])

print_hist({'a':1, 'b':2, 'f':3, 'c':4})
print_hist({"apple":3, "banana":2, "carrot":1})
