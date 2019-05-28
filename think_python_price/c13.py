
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

    
def middle(ele):
    res=ele[1:len(ele)-1]
    print(res)
    return

print(middle([1,2,3,4,5]))


    