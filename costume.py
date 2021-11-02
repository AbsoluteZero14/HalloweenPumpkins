import random
candy = []
trick_or_treating = False
money = 50
costume_amount = random.randint(0, 70)
costumes = ['skeleton', 'dog', 'spider-man']
print('Welcome to Pypasta, the Halloween Python simulator!')
first_choice = input('Would you like to start? ')
if first_choice == 'yes':
    #Some code here =D
    print("Let's get started!")
elif first_choice == 'no':
    print('Bwahahahaha NameError!')
    trick()
else: print('NEVER DO THIS AGAIN!')
while money == 50:
    costume_choice = input('What would you like to dress up as? (r for a random one)')
    if costume_choice == 'skeleton':
        print('Dressing up as', costume_choice)
        print('That will be', '$'+str(costume_amount))
        if costume_amount > money:
            print('You do not have enough money.')
        else:
            money = money - costume_amount
            print('You have $'+str(money), 'in your wallet.')
    if costume_choice == 'dog':
        print('Dressing up as', costume_choice)
        print('That will be', '$'+str(costume_amount))
        if costume_amount > money:
            print('You do not have enough money.')
        else:
            money = money - costume_amount
            print('You have $'+str(money), 'in your wallet.')
    if costume_choice == 'spider-man':
        print('Dressing up as', costume_choice)
        print('That will be', '$'+str(costume_amount))
        if costume_amount > money:
            print('You do not have enough money.')
        else:
            money = money - costume_amount
            print('You have $'+str(money), 'in your wallet.')
    if costume_choice == 'r':
        print('Dressing up as', random.choice(costumes))
        print('That will be', '$'+str(costume_amount))
        if costume_amount > money:
            print('You do not have enough money.')
        else:
            money = money - costume_amount
            print('You have $'+str(money), 'in your wallet.')
