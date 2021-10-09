sentence=input("ENTER YOUR SENTENCE")
characterCount=0
wordCount=1
for character in sentence:
    characterCount=characterCount+1
    if(character==' '):
        wordCount=wordCount+1
print( "number of characters in the sentence",+characterCount)
print("number of words in the sentence",+wordCount)