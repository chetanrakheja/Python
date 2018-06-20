#Display the Fibonacci series up to a max limit
a=0
b=1

limit = int(input("enter max limit of fibonacci series: "))


for i in range(50):
    if ((a+b)>limit):
        break
    else:
        if (i==0):
            c=a
            print(c)
        elif (i==1):
            c=b
            print(c)
        else:
            c=a+b
            print(c)
            a=b
            b=c
    
