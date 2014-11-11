
import random

print('The Cell Organelle Quiz Of Doom...')
score = 0
print('Make sure you spell right...')

print('Also if you see the correct! twice, it means you got 2 points')






def mitochondria():
    global score
    
    print('what is the Mitochondria??')
    answer = input('< ').strip().lower()

    if 'power' in answer or 'energy' in answer:
        print('correct!')
        score = score + 1
        print('You have', score , 'points ')
        
    else:
        print('sorry, thats incorrect...')
        print('You have', score , 'points ')

    
def cell_membrane():
    global score

    print('what is the Cell Membrane??')
    answer = input('< ').strip().lower()

    if 'in' in answer or 'out' in answer:
        print('correct!')
        score = score + 1
        print('You have', score , 'points ')
            
    else:
        print('sorry, thats incorrect...')
        print('You have', score , 'points ')

def cell_wall():
    global score
    
    print(' what is the Cell Wall??')
    answer = input('< ').strip().lower()

    if 'shape' in answer or 'support' in answer:
        print('correct!')
        score = score + 1
        print('You have', score , 'points ')

    else:
        print('sorry, thats incorrect...')
        print('You have', score , 'points ')
        
            
def chromosome():
    global score
    
    print(' what is the Chromosone/DNA??')
    answer = input('< ').strip().lower()

    if 'contains' in answer or 'trait' in answer or 'store' in answer:
        print('correct!')
        score = score + 1
        print('You have', score , 'points ')
        
            
    else:
        print('sorry, thats incorrect...')
        print('You have', score , 'points ')

def cytoplasm():
    global score
    
    print(' what is the Cytoplasm??')
    answer = input('< ').strip().lower()

    if 'inside' in answer or 'activities' in answer:
        print('correct!')
        score = score + 1
        print('You have', score , 'points ')
            
    else:
        print('sorry, thats incorrect...')
        print('You have', score , 'points ')

def ribosome():
    global score

    print(' what is the Ribosome??')
    answer = input('< ').strip().lower()

    if 'proteins' in answer or 'activities' in answer or 'function' in answer:
        print('correct!')
        score = score + 1
        print('You have', score , 'points ')
    else:
        print('sorry, thats incorrect...')
        print('You have', score , 'points ')
        
 
def nucleus():
    global score
    
    print(' what is the Nucleus??')
    answer = input('< ').strip().lower()

    if 'control' in answer or 'leader' in answer or 'activities' in answer:
        print('correct!')
        score = score + 1
        print('You have', score , 'points ')

    else:
        print('sorry, thats incorrect...')
        print('You have', score , 'points ')
    
def chloroplast():
    global score
    
    print(' what is the Chloroplast(Plants only)??')
    print('IF YOU CAN SPELL WHat IT CONTAINS, YOU GET 5 POINTS(has to be spelled right')
    answer = input('< ').strip().lower()

    if 'chlorophyll' in answer:
        print('you spelled it correct!')
        score = score + 5
        print('You have', score , 'points ')

    else:
        print('sorry, thats incorrect')
        print('You have', score , 'points ')
        
            
    if 'make' in answer or 'trap' in answer:
        print('correct!')
        score = score + 1
        print('You have', score , 'points ') 

    else:
        print('sorry, thats incorrect...')
        print('You have', score , 'points ')
        
def smooth_rough_ER():
    global score
    
    print(' what is the Smooth and rough E.R??')
    print('Worth 3 points')
    answer = input('< ').strip().lower()

    if 'protein' in answer or 'transport' in answer or 'store' in answer or 'ribosomes' in answer:
        print('correct!')
        score = score + 3
        print('You have', score , 'points ')
    else:
        print('sorry, thats incorrect...')
        print('You have', score , 'points ')

def golgi_body():
    global score
    
    print('what is the  Golgi Body??')
    answer = input('< ').strip().lower()

    if 'package' in answer or 'transport' in answer:
        print('correct!')
        score = score + 1
        print('You have', score , 'points ')
            

    else:
        print('sorry, thats incorrect...')
        print('You have', score , 'points ')



            
           

def lysosome():
    global score

    print('what is the  Lysosome??')
    answer = input('< ').strip().lower()

    if 'clean' in answer or 'break down' in answer or 'breakdown' in answer:
        print('correct!')
        score = score + 1
        print('You have', score , 'points ')

    else:
        print('sorry, thats incorrect...')
        print('You have', score , 'points ')

def vacuole():
    global score
    print(' what is the Vacuole??')
    answer = input('< ').strip().lower()

    if 'storage' in answer:
        print('correct!')
        score = score + 1
        print('You have', score , 'points ')
            
          

    else:
        print('sorry, thats incorrect...')
        print('You have', score , 'points ')

        
questions = [
    mitochondria,
    cell_membrane,
    chromosome,
    cell_wall,
    cytoplasm,
    nucleus,
    ribosome,
    chloroplast,
    smooth_rough_ER,
    golgi_body,
    lysosome,
    vacuole
]

while True:
    current = random.choice(questions)
    current()
    
