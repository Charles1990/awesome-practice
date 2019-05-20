# def a(x):
#     if x%2==0:
#         print('x is even')
#     else:
#         print('x is odd')

# def a(x,y):
#     if x==y:
#         print ('他们相等')
#     else:
#         if x<y:
#             print('X小于y')
#         else:
#             print('x大于y')

# a(3,3)

# def a(x):
#     if 0<x:
#         if x<10:
#             print('啊啊啊')

# def a(x):
#     if 0<x and x<10:
#         print('aaa')



# a(1)

# def a(n):
#     if n<=0:
#         print('Oh my god')
#     else:
#         print(n)
#         a(n-1)

# a(5)


def check_fermat(a,b,c,n):
    z=a**n+b**n-c**n
    if n<2:
        print('wrong')
    if a<0 or b<0 or c<0 or n<0:
        print("error,a,b,c must be postive integers")
        
    elif z==0:
        print("that's not work")
    else:
        print(z)

check_fermat(2,2,3,2)
    









