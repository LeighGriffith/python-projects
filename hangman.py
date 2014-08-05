word = "bighole"

print("Welcome to the amazing hangman game")
print()

while True:
    answer =input("are you ready")

    if answer == "yes":
        print("ook lets go ...") 
        break
    else:
        print('ill wait')

print("ready, begin.")

letter = input("pick a letter")

if letter == "a":
     print("wrong!")
