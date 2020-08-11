#this program will count the frequency of each character in a text
#no distinction between lower & uppercase
#the character's frequency is sort from the highest to lowest freq

teks = open("sample text.txt","r")
#"sample text.txt" can be changed with your file name

teks=teks.read()
teks=teks.lower()

dict_char={}

import collections
dict_char = collections.Counter(teks)

for letter,count in dict_char.most_common(len(dict_char)) :
    if letter.isalpha():
        print (letter, "->",count)
    else : continue





