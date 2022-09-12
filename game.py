from pickle import FALSE
import random as rnd
import sys


def wordReplace(entryWord):
    word = entryWord
    otherWord = otherWord = "".join(word)
    #print("Esta es la palabra:"+ str(word))
    newWord = (("a","á"),("e","é"),("i","í"),("o","ó"),("u","ú"))
    for i,j in newWord:
        for value in word:
            if value == j:
                #print("Esta es la unión"+str(otherWord),value,i)
                otherWord = otherWord.replace(value,i)           
    #print("Esta es la palabra final " +str(otherWord))
    return otherWord


def openTxt():
    list = []
    with open("./data.txt", "r", encoding= "utf-8") as f:
        for line in f:
            x = line.replace("\n","")
            list.append(x)
    return list


def random_word():
    list = openTxt()
    value = rnd.randint(0 , len(list))
    guessWord = list[value]
    
    return guessWord
    

def listWord():
    word = random_word()
    print(word)
    list = []
    for i in word:
        list.append(i)
    return list




def run():
    guess = []
    guess = wordReplace(listWord())
    finalList = []
    guessWord = FALSE
    life = True
    print("arrancó" +str(guess))

    for i in guess:
        finalList.append("_")
    print(finalList)

    while guessWord and life:  
        #Creación de los espacios vacios
        
        
        entryWord = [(input("Ingrese una letra: ")).lower()]
        newWord = wordReplace(entryWord)
        counter = 0 
        for i in guess:
            counter +=1
            if i == newWord:
                finalList[counter-1] = i
        print(finalList)
        word ="".join(finalList) 

        if guess == word:
            guessWord = True
            print("¡Adivinaste la palabra!")
            answer = (input("¿Quieres jugar de nuevo?" + "\nYes o No:"+ "\n")).lower
            if answer == "yes":
                run()
            else :
                print("JUEGO TERMINADO")
                sys.exit()
        
        
    
    #openTxt()
    #random_word()
    #print(listWord())
    

if __name__=="__main__":
    run()
