#input files and keyword
fileInput = input("Enter input file name:  ")
fileOutput = input("Enter output file name:  ")
keyword = input("Enter keyword:  ")
print("For encrypt press 'e' \nFor decrypt press 'd'")
choice = input("Choice:  ")

if not ".txt" in fileInput.lower():
    fileInput = fileInput + '.txt'

if not ".txt" in fileOutput.lower():
    fileOutput = fileOutput + '.txt'

#open input file
f = open(fileInput, "r")
inputText = f.read()


inputText = inputText.upper()
inputTextList = list(inputText)

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#transform key
key = 'MAGIC'
key = key.upper()
keyLength = len(key)
listKey = list(key)
keyMap = []
for value in listKey:
    temp = []
    num = ord(value)
    # print(num)
    for i in range(0, 26):
        temp.append(chr(num))
        num = num + 1
        if(num > 90):
            num = 65

    keyMap.append(temp)


#for encryption
if choice == 'e' or choice == 'E':
    outputTextListE = []
    s = 0
    for value in inputText:
        if ord(value) < 65 or ord(value) > 90:
            outputTextListE.append(value)
        else:
            if s < keyLength:
                index = alphabets.index(value)
                outputTextListE.append(keyMap[s][index])
                s = s + 1
            else:
                s = 0
                index = alphabets.index(value)
                outputTextListE.append(keyMap[s][index])
                s = s + 1

    encryptText = ''.join(outputTextListE)
    encryptText = encryptText.lower()
    f = open(fileOutput, "w")
    f.write(encryptText)
    f.close()

#for decryption
elif choice == 'd' or choice == 'D':
    outputTextListD = []
    s = 0
    for value in inputText.upper():
        if ord(value) < 65 or ord(value) > 90:
            outputTextListD.append(value)
        else:
            if s < keyLength:
                index = keyMap[s].index(value)
                outputTextListD.append(alphabets[index])
                s = s + 1
            else:
                s = 0
                index = keyMap[s].index(value)
                outputTextListD.append(alphabets[index])
                s = s + 1


    decryptText = ''.join(outputTextListD)
    decryptText = decryptText.lower()
    f = open(fileOutput, "w")
    f.write(decryptText)
    f.close()
