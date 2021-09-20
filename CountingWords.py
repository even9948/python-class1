introString= input("Enter You Introduction:") 
characterCount = 0
wordCount=1
for i in introString:
    characterCount+=1
    if(i==' '):
        wordCount=wordCount+1
print("Number of words in the string: ")
print(wordCount)
print("Number of characters in the string")
print(characterCount)