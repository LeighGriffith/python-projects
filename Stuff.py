
def prompt(area,description,actions):
	while True:
		print(area)
		print(description)
		print("optains = walk,nap")
		answer = input("What does thou chose to do?\n> ")
		 
		return answer
answer = input("What Is Your Name, Brave Adventurer?\n> ").strip()
print("Hello Brave Adventurer " + answer)
area = 'The Evil Tower'


description = ''' 
You've entered the mighty evil tower on a Tuesday 
night, you came here from a dare from your 
freinds, and you knew you could come out of here alive or
dead...
'''

actions = ["nap","walk"]
answer = prompt(area, description,actions)


if "nap" in answer:
	print("Im a little tired, im gonna get some sleep.")
	print("12 hours later...")
	import time
	for i in range(8,16):
		time.sleep(1)
		print(".....")
	print("You rose from your bed, and realized you "
		" have died from a evil "
		" monster")

if "walk" in answer:
	print("You walked slowly down the hall, you saw a chest!")

	print("optains = open the chest, keep walking")
	answer = input("Would you like to open the chest or keep walking")
if "keep walking" in answer:
	print("You decided to leave the chest alone and keep walking")
	print("You kept walking and you found the kichin")
	print("Optains: keep walking,go into kichin")
	answer = input("Would you like to go into the kichin?")
if "go into kichin" in answer:
	print("You chose to go into the kichin, you were to curious "
		" and you looked into the fridge and found a bomb and you died")
if "keep walking" in answer:
	print("You kept on walking down the hall")
	print("You heard noises so you ran as fast as you could, "
	" and then you hid behind a statue, but, the noise found you "
	" AKA monster, sliced your head in half and you died")

if "open the chest" in answer:
	print("You decided to open the chest, and you found a box")
	print("optains = yes,no")
	answer = input("Would you like to open the box")

if "yes" in answer:
 	print("You chose to open the box, it contained a bomb and it blew "
 		" up in your face")

if "no" in answer:
	print ("You chose to put the box back and you kept walking")
	print("As you were walking down the hall, you found "
	" a chest that had marks on it")
	print ("optains: yes,no")
	answer = input("Would you like to open it?")

if "no" in answer:
	print("You chose to not open the chest just in case, "
		" but as you were walking a GIANT MONSTER fell out of the cieling, he ran up and sliced your  head open and you fell "
		" down on the ground bleeding and you died")
if "yes" in answer:
 	print("As you opened it, you found a SILVER SWORD")
 	print("As you were walking, you found a GIANT MONSTER!")
 	print("optains = fight,run for it")
 	answer =input("What do you choose to do?")
if "run for it" in answer:
	print("You turned around and ran, he catched up, but you were "
 " to fast, you were at the exit, but then, all of cieling collaped on you and you bleeded to death")

if "fight" in answer:
	print("The monster tried to hit you but, you slapped his arm of "
	" and after a while, you killed him, and you found a HEALING POTION!")


	 







health = 100
strength = 1
agility = 1
intellegence = 1
stamina = 1





