#Display first n numbers of a Fibonacci series
a=0
b=1

limit = int(input("enter limit of fibonacci series"))

for i in range(limit):
    if (i==0): print(a)
    elif (i==1): print(b)
    else:
        c=a+b
        print(c)
        a=b
        b=c

