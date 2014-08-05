import random
count = 0
while True:
    count = count + 1
    value = random.randrange(1,1000001)
    print("{}. {}".format(count,value))
    if value == 1:
        break
