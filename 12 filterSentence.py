'''We wish to display only those words from the sentence that do not occur in a set of excluded words 
( like : this, and, is, not etc. ). The set of excluded words would be maintained in your code, and the 
sentence is input from the keyboard. We have to display all words that do not exist in this set, and we have
 to take care that multiple occurring words are displayed only once.
'''
#sentence = input("enter a sentence \n")
sentence="my name is chetan rakheja i study in Jims vk"

excludedWords=['this','and' ,'is','in']
sentenceList = sentence.split(" ") 
print(sentenceList)
newSentenceList=[]

for i in sentenceList :
	if i not in excludedWords:
		newSentenceList.append(i)	



print(newSentenceList)