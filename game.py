def wordReplace(entryWord):
    word = entryWord
    newWord = (("a","á"),("e","é"),("i","í"),("o","ó"),("u","ú"))
    for i,j in newWord:
        if word == j:
            otherWord = word.replace(word,i)
    print (otherWord)
    return otherWord


def openTxt():
    pass




def run():
    entryWord= input("Ingrese una letra: ")
    wordReplace(entryWord)


if __name__=="__main__":
    run()