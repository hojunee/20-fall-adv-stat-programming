def histogram(s):
    my_dict = {}
    for elem in s:
        my_dict[elem] = my_dict.get(elem, 0) + 1  
    return my_dict

print(histogram("aaabbc"))
print(histogram("xxxxyyzzz"))