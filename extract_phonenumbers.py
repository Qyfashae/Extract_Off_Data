#Coded by: QyFashae

import re

print("Extract phone numbers from a txt file with the help of 'Regex' for phone numbers and delimiters.")
fileToRead = input("File to read: ")  # File to extract from
fileToWrite = input("File to write: ")  # File to write to

delimiterInFile = {
    "delimiter_one": "",
    "delimiter_two": "",
    "delimiter_three": ""
}  # The delimiters in phone numbers may vary depending on the region/country etc.

deli_one = str(input("Delimiter_one: "))
deli_two = str(input("Delimiter_two: "))
deli_three = str(input("Delimiter_three: "))

if deli_one and deli_two:
    delimiterInFile["delimiter_one"] = deli_one
    delimiterInFile["delimiter_two"] = deli_two
    delimiterInFile.pop("delimiter_three", None)
elif deli_one and deli_two and deli_three:
    delimiterInFile["delimiter_one"] = deli_one
    delimiterInFile["delimiter_two"] = deli_two
    delimiterInFile["delimiter_three"] = deli_three
else:
    print("Error. Please add at least 2 delimiters.")

def validatePhoneNumber(strPhoneNumber):
    print("Example of a regular expression for phone numbers\n^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$")
    while True:
        regex_pattern = input("Regex to use: ")
        try:
            re.compile(regex_pattern)
            return re.mathc(regex_pattern, strPhoneNumber)
        except re.error:
            print("Invalid regular expression.")

def writeFile(listData):
    with open(fileToWrite, "w+") as file:
        for item in listData:
            file.write(item + "\n")

listPhoneNumber = []
with open(fileToRead, "r") as file:
    for line in file:
        line = line.strip()
        for delimiter in delimiterInFile.values():
            line = line.replace(delimiter, " ")
        words = line.split()
        for word in words:
            if validatePhoneNumber(word):
                listPhoneNumber.append(word)

if listPhoneNumber:
    uniquePhoneNumbers = set(listPhoneNumber)
    print(len(uniquePhoneNumbers), "phone numbers collected!")
    writeFile(uniquePhoneNumbers)
else:
    print("No phone numbers found.")
