falsenameexist = False
reversetitle = False
classlist = {
    "knight", "cleric", "wizard", "warlock", "hunter", "warrior", "assassin", "noble"
    }
classlist2 = {""," "
    }
        
while True:
    name = (input("whats your name?"))
    print(name + " are you sure thats your name?")
    correctname = (input())
    correctname = correctname.lower()
    if correctname == "no":
        print()
    elif correctname =="yes":
        break
    else:
        print("that was a yes or no question.")
print("whats your age")
while True:
    age = int((input()))
    if age == str(age):
        print("thats not a number!whats your actual age?")
    elif age > 100 and age < 1000:
        print("wow your old")
        break
    elif age < 10:
        print("wow your young")
        break
    elif age >= 1000:
        print(".....suuuuure")
        break
    elif age >= 10 and age <=100:
        break

print("you are " + str(age) + " years old")

gender = (input("whats your gender?"))
if gender == "male":
    title = "sir"
    print("your a guy!")
elif gender == "female":
    title = "lady"
    print("your a girl!")
else:
    title = "thing"
    print("congrats your an it!")

fromplace = (input("where are you from?"))
print("so let me get this right you are " + title + " Gretchan of Hoboken") 
profileconfirmation = (input())

if profileconfirmation == "yes":
    falsenameexist = True
    falsename = "Gretchan"
else:
    print("no no no thats not right. Oh! I know! is it " + title + " Bennidict Cumberbatch of " + fromplace + "?")
    confirm2 = (input())
    if confirm2 == "yes":
        falsenameexist = True
        falsename = "Bennidict Cumberbatch"
    else:
        print("oh damn I really thought i had it that time. but hey I got the place right......right?")
        input("Its on the tip of my tounge this time! really I promise it is! your name is .......")
        print("noooono no no no no.... dont intererupt me while im thinking! your name...")
        print("you are")
        if gender == "male":
            print("lady " + name + " of " + fromplace)
        elif gender == "female":
            print("sir " + name + " of " + fromplace)
        elif title =="thing":
            print("shemale " + name + " of " + fromplace)
            print("so....... did i get it right this time?")
    confirm3 = (input(""))
    if confirm3 == "yes":
            reversetitle = True
    else:
        print("oh I called you by the wrong gender? are you sure I mean you definatley look like one to me but what do i kno- I mean yes yes of course I knew you were a")
        if gender == "male":
            print("guy. I was just testing your observational skills....you get +50 to...uh..observationalisticism...")
        elif gender == "female":
            print("woman I was just testing your observational skills....you get +50 to...uh..observationalisticism...")
        else:
            print(" aha ha I knew that.......-akward silence-......")
while True:
    if falsenameexist == True:    
        classquestion = (input("so " + title + " " + falsename + " what class are you?"))
    else:
        if reversetitle == True and gender == "male":
            classquestion = (input("so lady " + name + "what class are you?"))
        elif reversetitle == True and gender == "female":
            classquestion = (input("so sir " + name + "what class are you?"))
        else:
            classquestion = (input("so " + title + " " + name + " what class are you"))                           
    if classquestion not in classlist and classquestion not in classlist2:
        print("what the hell is a " + classquestion + "? oh silly me you are obviously a babling fool")
        clas = "babling fool"
        input("confirm your class, current class - " + clas)
        print("conragradulations you are now a " + clas)
        break    
    elif classquestion in classlist and classquestion not in classlist2 :
        print("conragradulations you are now a " + clas)
        break                           
    elif classquestion in classlist2 and classquestion not in classlist:
        print("SPEAK UP! I cant hear you!")

                               
    
    
