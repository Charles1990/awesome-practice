# import math

# def eval_loop():
#     s=''
#     add=input('> ')
#     while True:
#         if add =='done':
#             break
#         else:
#             s+=add
#             add=input('>')
#     print(eval(s))
# eval_loop()


import math
def eval_loop():
    s=''
    add=input('>')
    while add!='done':
        s=add+s
        add=input('>')

    print(eval(s))
eval_loop()