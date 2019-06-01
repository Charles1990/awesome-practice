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

def histogram(s):
    d=dict()
    for i in s:
        d[i]=d.get(i,s.count(i))
    return d

def print_his(h):
    listik=sorted(h.keys())
    print(listik)

    # for i in listik:
    #     print(i,h[i])

h=histogram('bajfskdakdb')
print_his(h)

