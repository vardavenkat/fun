def list(a):
    i=0
    b=[]
    while i<len(a):
        if a[i]%2==0:
            b.append(a[i])
        i+=1
    print("even",b)
list([1,2,3,4,5,6,7,8,9])