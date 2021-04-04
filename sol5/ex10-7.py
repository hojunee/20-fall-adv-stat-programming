def is_anagram(seq_a, seq_b):
    if sorted(seq_a) == sorted(seq_b):
        return True
    else:
        return False

print(is_anagram("rescue", "secure"))
print(is_anagram("apple", "banana"))