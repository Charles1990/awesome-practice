
# def is_palindrome(word):
#     def first(word):
#         return word[0]
#     def last(word):
#         return word[-1]
    
#     def middle(word):
#         return word[1:-1]

#     if  len(word)<=1:
#         return True
#     else:
#         if first(word)==last(word):
#             return is_palindrome(middle(word))
#         else:
#             return False

# print (is_palindrome("nope nope"))


# def is_power(a,b):
#     if a<b:
#         return False
#     elif a==b:
#         return True
#     else:
#         if a%b == 0:
#             return is_power(a/b,b)
#         else:
#             return False
        

# print(is_power(15,2))

# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return (b,a/b)

# print(gcd(3,0))
# print(gcd(169,13))
# print(gcd(14,3))


# def countdown(n):
#     while n>0:
#         print(n)
#         n=n-1

#     print('hei')

# countdown(5)


# def squence(n):
#     while n!=1:
#         print(n)
#         if n%2==0:
#             n=n/2
#         else:
#             n=n*3+1

# squence(3)





