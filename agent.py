print ("Hello World")

name = input ("What's ur name? ").strip().title()
print ("Hello "+ name)
other_name =input("What is the other persons name? ").strip().title()
print("Please tell {} hello for me.".format(other_name))
first_age = input("How old are you {}? ".format(name)).strip()
other_age = input("And how old is {}? ".format(other_name)).strip()

first_age =int(first_age)
other_age =int(other_age)

years_apart = abs(first_age - other_age)
days_apart = 365.242 * years_apart

print("You are {} years apart ({} days).".format(years_apart,days_apart))
