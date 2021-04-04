# A : 65
# a : 97 ~ z : 122

# chr : int -> char
# ord : char -> int

def rotate_word(target, offset):
    return_str = ""
    if offset % 26 == 0:
        return target
    for elem in target:
        if offset > 0:
            if (ord(elem) + offset > 122):
                current_char = chr(96 + (ord(elem) + (offset % 26) - ord('z')))
            else:
                current_char = chr(ord(elem) + offset)
        else: 
            if (ord(elem) + offset < 97):
                current_char = chr(123 - (ord(elem) + (abs(offset) % 26) - ord('a')))
            else:
                current_char = chr(ord(elem) + offset)
        return_str += current_char
    return return_str
    
        
print(rotate_word("aaa", -27))
print(rotate_word("abc", 3))
print(rotate_word("xyz", 3))
print(rotate_word("python", 100))

# 'z' + 1 = 'a'
# 'z' + 2 = 'b'
...
# 'z' + 26 = 'z' // 122 + 26