
def can_be_made_of_letters(word, letters):
    n = len(word)
    i = 0
    for i in range(n):
       if letters.count(word[i])>=word.count(word[i]):
           i +=1
       else:
           return(False)
    return(True)

def possible_words(wordlist, letters):
    wordlist == []
    viable_words = []
    i = 0
    n = len(wordlist)
    for i in range(n):
       word = wordlist[i]
       if can_be_made_of_letters(word, letters) == True:
           viable_words.append(wordlist[i])
           i += 1
    return(viable_words)


