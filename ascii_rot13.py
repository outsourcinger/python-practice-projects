
cipher = input("What would you like to cipher? \n")

input_string = cipher

char_list = list(input_string)
# print(char_list)
newcipher = []
uncipher = []
for item in char_list:
    asciied = ord(item)
                            # print(asciied)
    ciphered = asciied + 13
                            # print(ciphered)
    chred = chr(ciphered)
    newcipher.append(chred)
    # print(chred)
    unchr = ord(chred)
    unciphered = unchr - 13
    unasciied = chr(unciphered)
    uncipher.append(unasciied)
    # print(unasciied)
print(*newcipher, sep='')
print(*uncipher, sep='')
