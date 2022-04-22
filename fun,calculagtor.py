def add(a,b):
    c=a+b
    return c
def sub(x,y):
    d=x-y
    return d
def mult(e,f):
    z=f*e
    return(z)
def div(r,q):
    m=r//q
    return(m)
def main():
    print(add(20,25))
    print(sub(40,3))
    print(mult(10,4))
    print(div(40,4))
def main():
    if num3=="+":
        print(add(num1,num2))
    elif num3=="-":
        print(sub(num1,num2))
    elif num3=="*":
        print(mult(num1,num2))
    elif num3=="%":
        print(div(num1,num2))
num1=int(input("enter a num1"))
num2=int(input("enter a num2"))
num3=int(input("enter the character for specifice opertor="))
main()