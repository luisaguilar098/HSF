#Practice in Python

import math
a = "" 
b = ""
c = ""

def math(a,b,c):
    print("Enter the first number")
    a =int(input())
    print("Enter the second number")
    b = int(input())
    c = a + b
    ans = "{} + {} = {}".format(a,b,c)
    print(ans)

math(a,b,c)
