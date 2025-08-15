import string
str=string.ascii_letters


selected_word="Thor"
current_word_state="__o_"

input_char=input("Enter char: ")

for i in range(len(selected_word)):
    
    input_char=input("Enter char: ")
    index=str.index(input_char)
    modified_word_state=""
    if current_word_state[i]=='_' and (selected_word[i]==str[26+index] or selected_word[i]==str[index-26]):
        modified_word_state+=selected_word[i]
    else:
        modified_word_state+=current_word_state[i]
    
    print(modified_word_state)
