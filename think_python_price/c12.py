# fin=open('/Users/yezhibin/awesome-practice/think_python_price/word.txt')
# for line in fin:
#     word=line.strip()
#     if len(word)>20:
#         print(word)

# def has_no_e(word):
#     word=word.lower()
#     for letter in word:
#         if letter=='e':
#             return False
#     return  True

# print(has_no_e('test'))
# print(has_no_e('basct'))

# def avoids(word,string):
#     for letter in word:
#         if letter in string:
#             return False
#     return True

# string=str(input('Please enter啥啥啥:\n'))
# fin= open('/Users/yezhibin/awesome-practice/think_python_price/word.txt')
# count=0
# for word in fin:
#     word=word.strip()
#     if avoids(word,string):
#         count +=1
#         print(word)

# print('totale letter from "{}" is {}'.format(string,count))


# string = str(input('Please enter the string of forbidden letters:\n'))

# fin= open('/Users/yezhibin/awesome-practice/think_python_price/word.txt')
# count = 0
# for word in fin:
#     word = word.strip()
#     if avoids(word, string):
#         count += 1
#         print (word)
# print('The total number of words that donot contain any letter from "{}" is {}'.format(string, count))

def use_only(word,string):
    for letter in word:
        if letter not in string:
            return False
    return True

string='acefhlo'
fin= open('/Users/yezhibin/awesome-practice/think_python_price/word.txt')

count=0
for line in fin:
    word=line.strip()
    if word !='hoe' and word !='alfalfa':
        if use_only(word,string):
            count+=1
            print(word)

print('you have {}什么什么的东西'.format(count))
