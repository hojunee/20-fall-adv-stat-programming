def most_frequent(string):
    my_dict = {}

    for elem in string:
        my_dict[elem] = my_dict.get(elem, 0) + 1  

    freq_set = [(i, my_dict[i]) for i in my_dict]
    freq_set.sort(key=lambda x : -x[1])

    print(freq_set)

most_frequent("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
most_frequent("life is short, you need python")