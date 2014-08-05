print("Hello world")

name = input("Whats your name ").strip().title()

print("Hi " + name)

age = input("How old are you? ").strip().title()
print("You are " + age + " years old")

if int(age) < 0:
    print("i think ur lying please type in agian")
    age = input("now how old r you really? ")
    age = age.strip()
    age = int(age)


if int(age) > 123:
    print("i think ur lying please type in agian")
    age = input("now how old r you really? ")
    age = age.strip()
    age = int(age)

if int(age) == 123:
    print("hey there carmello hows bolivea these days?")
    name = "Carmello"
    



money = input("Whats your allowance money a week? ")
weeks_in_year = 52
allowance_in_week = int(money)
allowance_per_year = allowance_in_week * weeks_in_year
age_in_weeks = weeks_in_year * int(age)


print("So a year you get " + str(allowance_per_year)  + " a year.")
string = "So {} you are {} years old and {} weeks old."
formatted_string = string.format(name,age,age_in_weeks)
print(formatted_string)

 
    

 

    
 



     




