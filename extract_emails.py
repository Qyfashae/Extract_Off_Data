#Coded by: QyFashae

import re

print("extract emails from a txt file with the help of 'Regex' for emails")
fileToRead = input("file to read: ")  # File to extract from
fileToWrite = input("file to write: ")  # File to write to
delimiterInFile = [
    ",",
    ";",
]  # Change here whether it is for example email@email.com;nextemail@nextemail.com or ';'


def validateEmail(strEmail):
    if re.match(
        "[a-zA-Z0-9.!#$%&'+-/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:.[a-zA-Z0-9-]+)", strEmail
    ):
        return True
    return False


def writeFile(listData):
    file = open(fileToWrite, "w+")
    strData = ""
    for item in listData:
        strData = strData + item + "\n"
    file.write(strData)


listEmail = []
file = open(fileToRead, "r")
listLine = file.readlines()
for itemLine in listLine:
    item = str(itemLine)
    for delimeter in delimiterInFile:
        item = item.replace(str(delimeter), " ")
    wordList = item.split()
    for word in wordList:
        if validateEmail(word):
            listEmail.append(word)
if listEmail:
    uniqEmail = set(listEmail)
    print(len(uniqEmail), "emails collected!")
    writeFile(uniqEmail)
else:
    print("No email found.")
