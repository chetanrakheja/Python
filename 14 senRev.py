''' make string from an input string with words in reverse order.  "A CAT RAN" => "RAN CAT A“  '''
sentence="a cat ran"

words = sentence.split(" ")
print(words)
words=words[-1::-1]
print(words)
newSentence=" ".join(words)
print(newSentence)