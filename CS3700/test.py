my_file = open("project1-words.txt", "r")
project1words = my_file.read()
list_of_words = project1words.split()
print(len(list_of_words))


#Filters the list of words based on the mark
def filterword(position, mark, letter):
    #remove all the words that contain this letter in this position
    if mark == 0:
      for word in list_of_words[:]:
        if(word[position] == "z"):
            print(word)
            list_of_words.remove(word)
            print(len(list_of_words))
        
    

words = "zlice"
mark = [0,0,0,0,0]
filterword(0, mark[0], words[0])

# print(len(list_of_words))
# filterword(1, mark[1], words[1])
# print(len(list_of_words))
# filterword(2, mark[2], words[2])
# print(len(list_of_words))
# filterword(3, mark[3], words[3])
# print(len(list_of_words))
# filterword(4, mark[4], words[4])
# print(len(list_of_words))
# print(list_of_words)