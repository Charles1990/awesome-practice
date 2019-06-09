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

words=['apple','bat','bar','atom','book','cup']
by_letter={}

for word in words:
    letter=word[0]
    if letter not in by_letter:
        by_letter[letter]=[word]
    else:
        by_letter[letter].append(word)

print(by_letter)