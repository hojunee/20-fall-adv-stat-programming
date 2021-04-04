import random

def sort_by_random(words):
    t = []
    for word in words:
       t.append((len(word), word))

    t.sort(key=lambda x: (-x[0], random.random()))

    res = []
    for _, word in t:
        res.append(word)
    return res

print(sort_by_random(("time", "series", "data")))
print(sort_by_random(("time", "series", "data")))
print(sort_by_random(("time", "series", "data")))
print(sort_by_random(("apple", "banana", "carrot")))
print(sort_by_random(("apple", "banana", "carrot")))
print(sort_by_random(("apple", "banana", "carrot")))