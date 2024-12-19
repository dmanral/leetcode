# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.

# Examples

# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    addAy = 'ay'
    textList = text.split(' ')
    newList = []
    for word in textList:
        wordLength = len(word)
        if wordLength <= 2:
            lastTwo = word[::-1]
            newList.append(lastTwo + word[:-2])
        else:
            lastTwo = word[-3:]
            newList.append(lastTwo + word[:-2])
        
    return newList

print(pig_it('Pig latin is cool'))       # igPay atinlay siay oolcay
# print(pig_it('Hello world !'))           # elloHay orldway !