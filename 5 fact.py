# Calculate the factorial of a number n

limit = int(input("enter number to calc factorial : "))
fact=1

for i in range (1,limit+1):
    fact=i*fact

print(fact)