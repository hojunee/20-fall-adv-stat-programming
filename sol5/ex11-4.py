def reverse_lookup(my_dict, value):
    my_key = []
    for elem in my_dict:
        if my_dict[elem] == value:
            my_key.append(elem)
    return my_key

print(reverse_lookup({1:1, 2:1, 3:1}, 1))
print(reverse_lookup({1:1, 2:1, 3:1}, 2))
