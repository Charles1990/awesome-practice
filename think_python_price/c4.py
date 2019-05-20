# def input_fermat():
#     a=input('baby please input a\n')
#     b=input('Now,the b\n')
#     c=input('input c\n')
#     n=input('OK,the last one n \n')
#     print(a,b,c,n)
#     #转换为整数
#     a=int(a)
#     b=int(b)
#     c=int(c)
#     n=int(n)
#     print(check_fermat(a,b,c,n))Exercise 5.4.


# def input():
#     a=input()

# def draw(t, length, n):
#     if n == 0:
#         return
#     angle = 50
#     t.fd(length*n)
#     t.lt(angle)
#     draw(t, length, n-1)
#     t.rt(2*angle)
#     draw(t, length, n-1)
#     t.lt(angle)
#     t.bk(length*n)

# draw(1,2,3)

# def ackermann(m, n):
#     if m == 0:
#         return n + 1
#     elif m > 0 and n == 0:
#         return ackermann(m - 1, 1)
#     elif m > 0 and n > 0:
#         return ackermann(m - 1, ackermann(m, n - 1))

# print (ackermann(3, 4))

# def is_power(a,b):
#     if a<b:
#         return False
#     elif a==b:
#         return True
#     else:
#         if a%b==0:
#             return is_power(a/b,b)
#         else:
#             return False

# print (is_power(16,2))
# print (is_power(15,2))



def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

#print(gcd(169,13))
print(gcd(200,17))
print(gcd(199,18))




