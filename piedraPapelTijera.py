import random

def choice(input):
    if input == 1:
        return('Piedra')
    elif input == 2:
        return('Papel')
    elif input == 3:
        return('tijeras')
    else:
        return('No elegiste nada')
    
    
def printingMessage():
    print(f'\n Has elegido la opción: {choice(optionUser)}')
    print(f'\n La máquina ha elegido: {choice(optionMachine)}')
    
    
optionUser = int(input('\n 1.Piedra \n 2.Papel \n 3.Tijera \n :'))
optionMachine = random.randint(1, 3)

if (optionUser == optionMachine):
    printingMessage()
    print('\n Empate')
    
elif ((optionUser == 1 and optionMachine == 3) or 
      (optionUser == 2 and optionMachine == 1) or 
      (optionUser == 3 and optionMachine == 2)):
    
    printingMessage()
    print('\n Ganaste')
    
elif (optionUser not in range(1,3)):
    printingMessage()
    print('\n Perdiste porque quisiste')

else:
    printingMessage()
    print('\n Perdiste mi rey')
    




