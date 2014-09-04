while True:

    print("How do you find the remote? ")
    find = input("< ")


    if 'couch' in find:
        print("good job you turned on the tv!")
        break

    else:
        print("you looked an it wasen't there. ")

while True:
    print("now that you have the remote, what button "
          'do you turn it on with?')
    find_one = input("< ")

    if 'power button' in find_one:
        print("good job now you can turn the tv on and watch "
              ' stuff! congrats! ')
        break
    
    else:
       print("sorry but thats not the button...")
    
