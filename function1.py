from zipfile import ZIP_BZIP2


def add(a,b):
    c=a+b
    return c
def sub(x,y):
    d=x-y
    return d
def mult(e,f):
    z=f*e
    return z
def div(s,t):
    g=s//t
    return g
def main():
    if num3=="+":
        print(add(num1,num2))
    if num3=="-":
        print(sub(num1,num2))
    if num3=="*":
        print(mult(num1,num2))
    if num3=="%":
        print(div(num1,num2))
    else:
        print("nothing")
num1=int(input("enter a nuo"))
num2=int(input("enter a no"))
num3=int(input("enter a no"))
main()