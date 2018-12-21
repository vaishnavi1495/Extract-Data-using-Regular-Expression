import re
import os

names = ""
roles = ""
emails = ""
contacts = ""
i = 0

if os.path.exists("output.txt"):
    os.remove("output.txt")

def wr(text):
    file = open("output.txt", "a+")
    file.write("\n")
    file.write("%d" % (i+1))
    file.write("\t")
    file.write(text)

def wrt(info):
    file = open("output.txt", "a+")
    file.write("\t")
    file.write(info)

#C:/Users/bhosa/Desktop/NLP/CSfaculty.txt

file_path = input("Please, Enter A File Path : ")
input_file = open(file_path, "r")

print("Data Successfully extracted from the file and Written to Output.txt")

while True:
    file_content = input_file.readline()
    names = re.findall(r'[A-Za-z]*\s?\-?[A-Za-z]+\,\s?[A-Za-z]+\-?\.?\s?[A-Za-z]*\.?', file_content)
    roles = re.findall(r'\b([A-Z]?[a-z]*\s?[A-Z]?[a-z]*\s?[A-Z][a-z]+\s?[A-Z]?[a-z]*)<br\b', file_content)
    emails = re.findall(r'\b([A-Za-z0-9]+\.?[A-Za-z0-9]*\.?[A-Za-z0-9]*@[a-z]*\.?utdallas.edu)\s?</a\b', file_content)
    contacts = re.findall(r'\-([0-9]{4})', file_content)

    if names:
        # print("\n")
        # print("%d" % (i+1), end="\t")
        # print(names.pop(0), end="\t")
        wr(names.pop(0))
        i = i + 1
    if roles:
        # print(roles.pop(0), end="\t")
        wrt(roles.pop(0))
    if emails:
        # print(emails.pop(0), end="\t")
        wrt(emails.pop(0))
    if contacts:
        # print(contacts.pop(0), end="\t")
        wrt(contacts.pop(0))

