# import math

# def compare_square():

#     def square(a):
#         x=1.0
#         while True:
#             y=(x+a/x)/2
#             if abs(y-x)<0.0000001:
#                 break
#             x=y
#         return x

#     for i in range(1,10):
#             a=i*1.0
#             square_newton=square(a)
#             square_lib=math.sqrt(a)
#             difference=abs(square_newton-square_lib)
#             print(a,square_newton,square_lib,difference)


# compare_square()

def compare_square():
   def square(a):
        x=1.0
        a=2.0
        while True:
            y=(x+a/x)/2
            if abs(y-x)<0.0000001:
                break
            x=y
        return x
        print(x)

compare_square()