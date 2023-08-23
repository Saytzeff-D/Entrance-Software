import random

def checkStatus():
    status = input('Are you a student? (y/N) ')
    if status == 'y':
        print('\nHi There!\nWelcome to SQI College of ICT, Ogbomoso')
        checkStud()
    elif status == 'N':
        print('\nKindly pass through the exit door as you are not allowed to come inside')
    else:
        print('\nInvalid Response, Try again!')

def checkStud():
    response = [
        'No valid response',
        'Your payment are up to date.\nYou may now proceed to go to your class.\nThank you!',
        'Sorry, your payment are not up to date.\nKindly go home and balance up your payment.',
        'Unfortunately, we could not find any of your records.',
    ]
    name = input('What is your name? ')
    index = random.randint(1,3)
    if name != '':         
        print(f"\nDear {name}!\n{response[index]}")
    else:
        print('\nPlease enter your name')
        checkStud()

checkStatus()