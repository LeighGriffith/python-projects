

print('The Cell Organelle Quiz Of Doom...')
score = 0
print('Make sure you spell right...')
print('There is a tiny error in some of the questions where'
      'if you put the right answer '
      ' it will say its correct then incorrect.(you got it right)')
print('Also if you see the correct! twice, it means you got 2 points')
while True:

    print('Alright then, first question, what is the Mitochondria??')
    question = input('< ').strip().lower()

    if 'power' in question:
        print('correct!')
        score = score + 1
             
    if 'energy' in question:
        print('correct!')
        score = score + 1
             
            

    else:
        print('sorry, thats incorrect...')

    

    print('Second question, what is the Cell Membrane??')
    question = input('< ').strip().lower()

    if 'in' in question:
        print('correct!')
        score = score + 1
            
            

    if 'out' in question:
        print('correct!')
        score = score + 1
             
            
    else:
        print('sorry, thats incorrect...')


    print('Third question, what is the Cell Wall??')
    question = input('< ').strip().lower()

    if 'shape' in question:
        print('correct!')
        score = score + 1
             
            

    if 'support' in question:
        print('correct!')
        score = score + 1
            
            

    else:
        print('sorry, thats incorrect...')
        
            

    print('Fourth question, what is the Chromosone/DNA??')
    question = input('< ').strip().lower()

    if 'contains' in question:
        print('correct!')
        score = score + 1
            
           

    if 'trait' in question:
        print('correct!')
        score = score + 1
            
            

    if 'store' in question:
        print('correct!')
        score = score + 1
            
            

    else:
        print('sorry, thats incorrect...')


    print('Fifth question, what is the Cytoplasm??')
    question = input('< ').strip().lower()

    if 'inside' in question:
        print('correct!')
        score = score + 1
            
            

    if 'activities' in question:
        print('correct!')
        score = score + 1
            
            

    else:
        print('sorry, thats incorrect...')


    print('Sixth question, what is the Ribosome??')
    question = input('< ').strip().lower()

    if 'proteins' in question:
        print('correct!')
        score = score + 1

    if 'activities' in question:
        print('correct!')
        score = score + 1       

    if 'function' in question:
        print('correct!')
        score = score + 1
            
            

    else:
        print('sorry, thats incorrect...')
        
 

    print('Seventh question, what is the Nucleus??')
    question = input('< ').strip().lower()

    if 'control' in question:
        print('correct!')
        score = score + 1

    if  'leader' in question:
        print('correct!')
        score = score + 1
                
           

    if  'activities' in question:
        print('correct!')
        score = score + 1
             
            

    else:
        print('sorry, thats incorrect...')   
    

    print('Eighth question, what is the Chloroplast(Plants only)??')
    print('IF YOU CAN SPELL WHat IT CONTAINS, YOU GET 5 POINTS(has to be spelled right')
    question = input('< ').strip().lower()

    if 'chlorophyll' in question:
        print('correct!')
        score = score + 5
            
    if 'make' in question:
        print('correct!')
        score = score + 1        

    if ' trap' in question:
        print('correct!')
        score = score + 1
            
            

    else:
        print('sorry, thats incorrect...')


    print('Nineth question, what is the Smooth and rough E.R??')
    print('Worth 3 points')
    question = input('< ').strip().lower()

    if 'protein' in question:
        print('correct!')
        score = score + 3

    if 'tranport' in question:
        print('correct!')
        score = score + 3
             
    if 'stores' in question:
        print('correct!')
        score = score + 3          

    if 'ribosome' in question:
        print('correct!')
        score = score + 3
             
        

    else:
        print('sorry, thats incorrect...')       


    print('Thenth question, what is the  Golgi Body??')
    question = input('< ').strip().lower()

    if 'package' in question:
        print('correct!')
        score = score + 1
            
            

    if 'tranport' in question:
        print('correct!')
        score = score + 1
            
           

    else:
        print('sorry, thats incorrect...')



            
           



    print('Eleventh question, what is the  Lysosome??')
    question = input('< ').strip().lower()

    if 'clean' in question:
        print('correct!')
        score = score + 1
        
    if 'break down' in question:
        print('correct!')
        score = score + 1         
           

    if 'breakdown' in question:
        print('correct!')
        score = score + 1
            
          

    else:
        print('sorry, thats incorrect...')

    print('Twelth question, what is the Vacuole??')
    question = input('< ').strip().lower()

    
           

    if 'storage' in question:
        print('correct!')
        score = score + 1
            
          

    else:
        print('sorry, thats incorrect...')


    print('Congratulations!!, you scored', score , '!')
    
    print('Play agian?')
    question = input('< ')

    if 'no' in question:
        print('ok')
        break

    if 'yes'in question:
        print('sure')

            


         


    
    
