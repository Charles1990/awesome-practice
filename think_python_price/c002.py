# PI=3.1415926

# def f(X):
#     return X*2

# def g(a,b):
#     return a+b
# list_of_lists=['foo','abc','def']
# everything=[]
# for chunk in list_of_lists:
#     everything.extend(chunk)

# print(everything)

# by_letter={}

# for word in words:
#     letter=word[0]
#     if letter not in by_letter:
#         by_letter[letter]=[word]
#     else:
#         by_letter[letter].append(word)

# print(by_letter)


# words=['apple','bat','bar','atom','book','cup','a']

# lt=[]

# for i in words:
#     if len(i)>2:
#         lt.append(i)

# print(lt)

# all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
# lt=[]

# for names in all_data:
    
#     for name in names:
#         if names.count('e')>=2:
#             lt1.extend(names)
    


    # enough_es=[name for name in names if name.count('e')>=2]
    # lt.extend(enough_es)

# print(lt)


# string=['a','as','bata','car','dove','python']
# lt=[]

# for x in string:
#     if len(x)>2:
#         x=x.upper()
#         lt.append(x)

# # print(lt)
# all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
# lt=[]

# for names in all_data:
#     x=[name for name in names if name.count('e')>=2]
#     lt.extend(x)

# print(lt)

# for names in all_data:
#     for name in names:
#         if name.count('e')>=2:
#             lt.append(name)
# print(lt)

# a=[]
# def func():
    
#     for i in range(5):
#         a.append(i)

# print(a)

# def f():
#     a=5
#     b=6
#     c=7
#     return a,b,c
# a,b,c=f()
# print(f())

states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
  'south   carolina##', 'West virginia?']

import re
def clean_string(strings):
    result=[]
    for value in strings:
        value=value.strip()
        value=re.sub('[!#?]','',value)
        value=value.title()
        result.append(value)
    return result

print(clean_string(states))