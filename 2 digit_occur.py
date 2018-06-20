#Find out how many times a particular digit occurs in a number

temp_num = input("enter no.")
count_num = len(temp_num)

findDigit = input("enter digit to be found.")
count_digit=temp_num.count(findDigit)

num=int(temp_num)


print(num)
print("length of num is ",count_num)
print("count of digit is ",count_digit)

