def is_sorted(seq):
    for i in range(len(seq)-1):
        if seq[i] > seq[i+1]: 
            return False
    return True

print(is_sorted([1, 2, 3]))
print(is_sorted(['b', 'a']))
print(is_sorted("statistics"))