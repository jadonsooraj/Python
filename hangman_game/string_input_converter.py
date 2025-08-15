import string
str=string.ascii_letters

input_char=input("Enter character: ")
index=str.index(input_char)

if index<26:
    print(str[index],str[26+index])
else:
    print(str[index-26],str[index])
