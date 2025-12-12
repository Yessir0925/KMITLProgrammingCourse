sentence = input('Enter : ').split()
for word in sentence:
    characterDict = {}
    for char in word:
        if char in characterDict:
            characterDict[char] += 1
        else:
            characterDict[char] = 1
    print(f'{word} = {characterDict}')

if(len(sentence) > 1):
    characterDict = {}
    sentenceText = ' '.join(sentence)
    for char in sentenceText:
        if(char == ' '):
            continue
        if char in characterDict:
            characterDict[char] += 1
        else:
            characterDict[char] = 1
    print(f'{sentenceText} = {characterDict}')
max_char = max(characterDict, key=characterDict.get)
print(f'Maximum Character Count: {max_char} {characterDict[max_char]}')
print("===== End of program =====")