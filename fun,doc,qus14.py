def fun():
    a=int(input("enter a no"))
    i=1
    c=0
    while i<=a:
        if a%i==0:
            c+=1
        i+=1
    if c==2:
        print("prime")
    else:
        print("not prime")
fun()
        