while True:

    name = input("What is your name ").strip().lower()

    if 'j' in name:
      won = input("You won 1000 dollars!! ").strip().lower()

      if "y" in won:
          print("Just kidding...")

      else:
          print("Go down the toilot to the sewers to Canada to find your prize!")
    
    if 'b' in name:
      jail = input("Go to Bob's funland!! ").strip().lower()

      if 'n' in jail:
          print("good choice")

      else:
          print("You died.....")
    else:
        bob = input("I love u... ").strip().lower()

        if 'n' in bob:
            print("I see...")

        if 'o' in bob:
            print("Were getting married next saturday bebe...")

        if 'y' in bob:
            print("thanks... You're nice honne...")

        else:
            print("STOP BEING MEAN TO ME!!!!!")
