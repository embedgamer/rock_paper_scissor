import random
com_opt = ['rock','paper','scissors']
def gaming ():
    com_poin = 0
    user_poin = 0
    user_cho = input ('>>> ')
    user_cho = user_cho.lower()
    while user_cho != 'quit':
        com_cho = random.choice(com_opt)
        a = 'You : %s ; Comp : %s' % (user_cho,com_cho)
#rock
        if user_cho == 'rock':

            if com_cho == 'paper':
                com_poin = com_poin + 1
                print (f'''{a} 
You : {user_poin} 
Comp : {com_poin}''')
            elif com_cho == 'scissors':
                user_poin = user_poin + 1
                print (f'''{a}
You : {user_poin}
Comp : {com_poin}''')
            elif com_cho == 'rock':
                print (f'''{a}
You : {user_poin}
Comp : {com_poin}''')
            user_cho = input('>>> ')
#paper
        elif user_cho == 'paper':
                if com_cho == 'scissors':
                    com_poin = com_poin + 1
                    print(f'''{a}
You : {user_poin}
Comp : {com_poin}''')
                elif com_cho == 'rock':
                    user_poin = user_poin + 1
                    print(f'''{a}
You : {user_poin}
Comp : {com_poin}''')
                elif com_cho == 'paper':
                    print(f'''{a}
You : {user_poin}
Comp : {com_poin}''')
                user_cho = input('>>> ')
#scissor
        elif user_cho == 'scissors':
                if com_cho == 'rock':
                    com_poin = com_poin + 1
                    print(f'''{a}
You : {user_poin}
Comp : {com_poin}''')
                elif com_cho == 'paper':
                    user_poin = user_poin + 1
                    print(f'''{a}
You : {user_poin}
Comp : {com_poin}''')
                elif com_cho == 'scissors':
                    print(f'''{a}
You : {user_poin}
Comp : {com_poin}''')
                user_cho = input('>>> ')
        elif user_cho not in com_opt and user_cho != 'quit':
            print (f"I don't understand {user_cho}")
            user_cho = input ('>>> ')
    if user_cho == 'quit':
        if user_poin > com_poin:
            print ('You Won 😎😉😊🍦🍩🍕✈')
        elif user_poin == com_poin:
            print ('Tie 😐 ')
        else :
            print ('You Lose 😢😐😠❌')
gaming()





