
# def nested_sum(x):
#     total=0
#     for y in x:
#         if type(y) is list:
#             y=nested_sum(y)
#         total += y

#     return total

# print(nested_sum([1,2,3,[4,5],[10]]))
# print(nested_sum([1,2,3,[4,5],[10]]))
# print(nested_sum([]))
# print(nested_sum([[1],[2],[3],[4],[5],[10]]))
# print(nested_sum([1,2,3,[-4,-5],[10]]))
# print(nested_sum([1,2,3,[[-4,[-5]],[10]]]))
# def nested_sum(listik):
#     total = 0
#     for i in listik:
#         if type(i) is list:
#            i = nested_sum(i)  
#         total += i
#     return total

# print(nested_sum([1,2,3,[4,5],[10]]))


# def cap_nested(listik):
#     caped=[]
#     for i in listik:
#         if type(i) is list:
#             i=cap_nested(i)
#         else:
#             i=i.capitalize()
#         caped.append(i)
#     return caped

# print(cap_nested(['a','b','c']))
# print(cap_nested(['a','b','c',['a','a'],['a']]))
# print(cap_nested([['banana'],['apple'],['cucumber'],['orange'],['lime'],['tomato']]))

# def nested_sum(listik):
#     total=0
#     res=[]
#     for i in listik:
#         total+=i
#         res.append(total)
#     return res

# print(nested_sum([1,2,3]))

# def middle(ele):
#     res=ele[1:len(ele)-1]
#     return res

# print(middle([1,2,3,4,5]))

    
# def middle(ele):
#     res=ele[1:len(ele)-1]
#     print(res)
#     return

# print(middle([1,2,3,4,5]))


# def is_sorted(ele):
#     if sorted(ele)==ele:
#         return True
#     else:
#         return False
# # print(is_sorted([1,2,2])
# # #print(is_sorted(['b','a'])
# print(is_sorted([1,2,2,]))
# print(is_sorted(['b','a']))

# def is_sorted(ele):
#     for i in range(len(ele)-1):
#         if ele[i] > ele[i+1]:
#             return False
#     return True

# print(is_sorted([1,2,2,]))
# print(is_sorted(['b','a']))

# def is_anagram(s, t):
#     s = s.lower().replace(" ", "")
#     t = t.lower().replace(" ", "")
    
#     first = list(s)
#     second = list(t)

#     first.sort()
#     second.sort()
    
#     return first == second

# print(is_anagram("Mary", "Army"))
# print(is_anagram("Jim Morrison", "Mr Mojo Risin"))
# print(is_anagram("War", "Peace"))

# def is_anagram(listik1, listik2):
#     if len(listik1) == len(listik2):
#         listik1 = list(listik1)
#         listik2 = list(listik2)
#         listik1.sort()
#         listik2.sort()
#         return listik1 == listik2
#     else:
#         return False
    
# print(is_anagram('orchestra','carthorse'))
# print(is_anagram('sport','porta'))
# print(is_anagram(' ',' ')) # is it ok or not?!


def is_anagram(ele,ele2):
    if len(ele)==len(ele2):
        ele=list(ele)
        ele2=list(ele2)
        ele.sort()
        ele2.sort()
        return ele==ele2
    else:
        return False
print(is_anagram('orchestra tvnm','carthorse mvtn'))
print(is_anagram('sport','porta'))
print(is_anagram(' ',' ')) # is it ok or not?!