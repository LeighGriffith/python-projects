while True:
    mario = input("Do you want to play super mario bros? ").strip().lower()

    if mario == "yes":
        print("ok lets ago!")
        break

while True:
    level_one = input("Are you ready to go to level 1? ").strip().lower()

    if level_one == "yes":
        print("lets ago!")
        break

    else:
        print("its ok il'a wait!")

print("You started to walk and you saw a goomba!")
print("optians = run away, fight")

while True:

    print("What do you choose to do? ") 
    go = input("< ").strip().lower()

    if go == "fight":
        print("You chose to fight and jumped on his " 
              "head and the goomba smushed and died.")
        break

    if go == "run away":
        print("You went to the side and got away from the goomba.")
        break

    else:
        print("please choose one of the optains")
