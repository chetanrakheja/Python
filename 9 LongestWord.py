# Input a sentence and display the longest word
sentence = input("enter a sentence \n")


words = sentence.split(" ")

print (words)
longestWord = ""
longestlen=0

i=0 
for j in words:
	if len(j)> longestlen:
		longestWord = j
		longestlen = len(j)
		
print("longest word is ",longestWord )
print("longest word length is ",longestlen )






