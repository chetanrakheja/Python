#Display all the words that are contained in a sentence. Words that come multiple times should be displayed only once.


#sentence = input("enter a sentence \n")
sentence = "tic tac toe is named as tic tac toe when it was made"

words = sentence.split(" ")
b =[]
for i in words :
	if i not in b:
		b.append(i)	
c= str(b)




print (words)

print("b",b)
print("c",c)






