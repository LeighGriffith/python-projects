import random

answers = [
    'Yes. ',
    'No. ',
    'Mabye ',
    'Of Course! ',
    'Signs Point To No. ',
    'Signs Point To Yes. ',
    'It Is Certain ',
    'Ask Me Later ', 
    'Reply hazy, try again. ',
    'Without a doubt. ',
    'My sources say no. ',
    'As I see it, yes. ',
    'You may rely on it. ',
    'Concentrate and ask again. ',
    'Outlook not so good. ',
    'It is decidedly so. ',
    'Better not tell you now. ',
    'Very doubtful. ',
    'Yes - definitely. ',
    'It is certain. ',
    'Cannot predict now. ',
    'Most likely. ',
    'Ask again later. ',
    'My reply is no. ',
    'Outlook good. ',
    'Dont count on . ',
    'Yes, in due time. ',
    'My sources say no. ',
    'Definitely not. ',
    'You will have to wait. ',
    'I have my doubts. ',
    'Outlook so so. ',
    'Looks good to me! ',
    'Who knows? ',
    'Looking good! ',
    'Probably. ',
    'Are you kidding? ',
    'Go for it! ',
    'Dont bet on it. ',
    'Forget about it. ',
]
while True:
    print("Ask me a question")
    question = input('> ')
    
    if 'love' in question:
        print("NEVER TALK ABOUT LOVE!!")
    if 'poop' in question:
        print("You are so weird you dont have a life you stink")
    if 'life' in question:
        print("You have no life since your bootie is to big and your ugly")
    if 'snowman' in question:
        print("YES OF COURSE!!!")
    answer = random.choice(answers)
    print(answer)
