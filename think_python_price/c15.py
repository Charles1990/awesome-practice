# def sumall(*t):
#     return sum(t)

# print(sumall(1,2,3,4,6))


import random

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), random.random(), word))
        
    t.sort(reverse=True)
    res = []
    
    for length, _, word in t:
        res.append(word)
    return res

print(sort_by_length(['banana', 'apple', 'kiwi', 'orange', 'cucumber', 'tomato', 'potato']))
print(sort_by_length(['banana', 'apple', 'kiwi', 'orange', 'cucumber', 'tomato', 'potato']))