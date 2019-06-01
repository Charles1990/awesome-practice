# def build_dict():
#     dictionary={}
#     fin=open('/Users/yezhibin/awesome-practice/think_python_price/word.txt')
#     for line in fin:
#         word=line.strip()
#         dictionary[word]=len(word)
#     return dictionary

# def is_in_dictionary(string):
#     dictionary=build_dict()
#     if string in dictionary:
#         return True

# print(is_in_dictionary('banana'))

# def histogram(s):
#     d=dict()
#     for i in s:
#         d[i]=d.get(i,s.count(i))
#     return d

# def print_his(h):
#     listik=sorted(h.keys())
#     print(listik)

    # for i in listik:
    #     print(i,h[i])

# h=histogram('bajfskdakdb')
# print_his(h)


# def histogram(s):
#     d=dict()
#     for i in s:
#         d[i]=d.get(i,s.count(i))
#     return d

# def invert_dict(d):
#     invert=dict()
#     for k,v in d.items():
#         invert.setdefault(v,[]).append(k) #https://segmentfault.com/q/1010000014282676
#         # append(k)为原来d.items中的Key(p,a,o,t)，而v是原来的(1,2,)，在v=1中，添加[。。。]
#     return invert

# hist = histogram('parrot')
# print(invert_dict(hist))


# import time

# known = {0:0, 1:1}

# def fibonacci2(n):
#     if n in known:
#         return known[n]
#     res = fibonacci2(n-1) + fibonacci2(n-2)
#     known[n] = res
#     return res


# def fibonacci1(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci1(n-1) + fibonacci1(n-2)
    
# start_time = time.time()
# fibonacci1(30)
# function_time1 = time.time() - start_time

# start_time = time.time()
# fibonacci2(30)
# function_time2 = time.time() - start_time

# print(function_time1) 
# print(function_time2)

# def has_duplicates(t):
#     result = {}
#     for element in t:
#         if element in result:
#             return True
#         else:
#              result[element] = 1
#     return False

# print(has_duplicates([1,2,3,4]))
# print(has_duplicates([1,2,2,4]))
