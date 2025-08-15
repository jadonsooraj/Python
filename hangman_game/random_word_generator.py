from random import randint

def pick_random_word():
    with open("words.txt", 'r') as words_file:
        word_list1=words_file.readlines() #list of Words from readlines() method

    word_list2=["Thor","ravan","HULK"]    
    selected_index=randint(0,len(word_list2)-1) #word is selected from the list
    return word_list2[selected_index]


