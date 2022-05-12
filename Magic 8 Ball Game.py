impot random # Allow the progrram to use random numbers

while True:
    print() # prints a blank line
    
    users0uestion = input('Ask the magic 8-ball a question(press enter to quit):n')
    
        
    randomAnswer = random.randrange(0, 8)  #pick a random number
    if randomAnswer == 0:
        print('It is certain.')
        
    elif randomAnswer == 1:
        print('Absolutely!')
     
    elif randomAnswer == 2:
        print('That was a dumb question!')
        
    elif randomAnswer == 3:
        print('Answer is foggy, ask again later')
        
    elif randomAnswer == 4:
        print('Of course!')
        
    elif randomAnswer == 5:
        print('Unsure at this point, try again later')
        
    elif randomAnswer == 6:
        print('Dont bother me today')
        
    elif randomAnswer == 7:
        print('Hell NO!')
        