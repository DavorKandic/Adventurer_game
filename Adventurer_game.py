# -*- coding: utf-8 -*-
from random import randint
import time
import sys


life = 100
mana = 100
gold = 0
damage=20
evasion=10

lifelist=[100]
manalist=[100]
goldlist=[0]
damagelist=[0,0]
evadelist=[0,0]

def dmg(lifelist,manalist,damagelist):
 dmls_length=len(damagelist)
 for i in range(dmls_length):
   damagelist.pop()
 damagelist.extend(lifelist)
 damagelist.extend(manalist)
 return damagelist

def evade(lifelist,manalist,evadelist):
 evls_length=len(evadelist)
 for i in range(evls_length):
   evadelist.pop()
 evadelist.extend(lifelist)
 evadelist.extend(manalist)
 return evadelist



def journey (life,mana,gold,damage,lifelist,manalist,goldlist):
    x=randint(1,12)
    if x == 1:
        print('You were victim of raiders attack!')
        if damage > 50:
              print('You killed them all and took their posessions, you crazy destroyer!')
              goldlist+=[15]
              return goldlist
        elif damage > 30:
              lifelist+=[-5]
              print('It was tough, but you show them who is the boss!')
              return lifelist
        else:
          lifelist+=[-20]
          if gold >= 10:
              goldlist+=[-10]
              return lifelist,goldlist
          else:
              manalist+=[-10]
              return lifelist,manalist

    elif x == 2:
        print('You passed through vampiric aura forest!')
        if mana>=20 and life >=50:
              manalist+=[-20]
              return manalist
        elif mana>=20 and life <50:
              lifelist+=[25]
              manalist+=[-20]
              return lifelist,manalist
        elif mana<20 and life >= 50:
              lifelist+=[-30]
              return lifelist

    elif x == 3:
        print('You found hidden stash that belongs to raiders.')
        goldlist+=[35]
        lifelist+=[15]
        manalist+=[10]
        return goldlist,manalist,lifelist

    elif x == 4:
        print('You found abandoned supermarket.')
        lifelist+=[35]
        manalist+=[15]
        goldlist+=[20]
        return lifelist,manalist,goldlist

    elif x == 5:
        if mana > 250:
            print('Your powerfull psyonic aura has scarred hidden Rad-Snake!\nShe has ran away, leaving one of her expensive eggs.Bingo!')
            print('But toxins from the egg damage your skin.')
            lifelist+=[-25]
            goldlist+=[15]
            return lifelist,goldlist
        else:
          print('You have been bitten by poisonous mutated Rad-Snake!')
          if life >= 150:
               lifelist+=[-125]
               return lifelist
          elif life >= 100:
               lifelist+=[-75]
               return lifelist
          else:
               lifelist+=[-50]
               return lifelist

    elif x == 6:
        print('You have found and ate some \'magic\' mushrooms. You have some unreal visions, but you feel little sick now.')
        manalist+=[15]
        lifelist+=[-20]
        return manalist,lifelist

    elif x == 7:
        print('You found members of Cyber-Scientology cult. Those strange felows share their food with you \nand give you some of coins they have. They explained to you their strange beliefs.\nThey believe that whole Universe is just computer program!\nYou find it funny, but you feel your spirituality have risen...')
        lifelist+=[5]
        manalist+=[5]
        goldlist+=[5]
        return lifelist,manalist,goldlist

    elif x == 8:
        print('You have found a bag of gold!')
        goldlist+=[25]
        return goldlist


    elif x == 9:
        print('You have found a package of meat-cans and energy-drinks!')
        lifelist+=[25]
        return lifelist

    elif x== 10:
        print('You have stepped on improvised landmine! It hurts like hell!')
        lifelist+=[-30]
        return lifelist

    elif x == 11:
        print('You have searched for gold in river. You have found a little bit of it, but blood-sucking water worms have bitten your legs!')
        goldlist+=[10]
        lifelist+=[-15]
        return goldlist,lifelist

    elif x == 12:
        print('You are suddenly feeling sick. With your Geiger-counter you discover that some\nof your gold is irradiated - you will have to throw it away!')
        if gold >= 15:
           goldlist+=[-15]
        else:
           goldlist.pop()
        lifelist+=[-10]
        return goldlist,lifelist



def status(life,mana,gold,damage,evasion):
    print('\n********\n')
    print('Your stats:\nLIFE:',life,'\nMANA:',mana,'\nGOLD:',gold,'\nDAMAGE:',damage,'\nEVASION:',evasion)
    print('\n********\n')


def choose():
    print('It is time to choose your path adventurer! Choose wisely:\n 1 - Go on a journey to search for gold.'
          '\n 2 - Fight in Arena to win a prize.\n 3 - Go to hospital for healing (if you have gold!).\n 4 - Gamble at casino.')
    while True:
        try:
            choice=int(input('Enter number of your choice::'))
            break
        except ValueError:
            print('Wrong input! Please enter valid number.')

    if choice == 1 :
               print('You put on your hat and backpack. Time to go on a journey...')
               print('\n**********************************************************\n')
               journey(life,mana,gold,damage,lifelist,manalist,goldlist)
               print('\n**********************************************************\n')


    elif choice == 2:
               print('You decided to test your luck and your skills in the Arena. Prepare for battle!')
               print('\n**********************************************************\n')
               combat(lifelist,goldlist,damagelist,evadelist,life,gold,damage,evade)
               print('\n**********************************************************\n')

    elif choice == 3:
               print('\nYou are aware that your wounds need healing. But, it will cost you some gold...\n')
               print('\n**********************************************************\n')
               hospital(lifelist,manalist,goldlist,gold)
               print('\n**********************************************************\n')

    elif choice == 4:
               print('You decided to try your luck at casino. Good luck!')
               print('\n**********************************************************\n')
               casino(gold,goldlist)
               print('\n**********************************************************\n')




def hospital(lifelist,manalist,goldlist,gold):
    if gold<25:
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
        print('\nYou do not have enough money! See you when you can afford healing.\n')
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')

    else:
        while gold > 0:
            print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
            print('''\nWelcome to the City Hospital. Choose one of our services:\n1 - Small healing package (life: +15, price: 25 gold)
            \n2 - Medium healing package (life: +35, price: 50 gold)\n3 - Large healing package (life: +50, price: 75 gold)
            \n4 - Mana potion (mana: +25, price: 50 gold)\n5 - Rejuvenation potion (life: +35, mana: +35, price: 100 gold)
            \n6 - Turbo healing package (life: +125, price: 150 gold)\n7 - Not interested, thank you!''')

            while True:
                try:
                    h=int(input('\nEnter your choice::'))
                    break
                except ValueError:
                    print('Wrong input! Please enter valid number.')

            if h ==1:
                  print('You have bought Small healing package.')
                  lifelist+=[15]
                  goldlist+=[-25]
                  return lifelist,goldlist

            elif h == 2:
                if gold<50:
                  print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                  print('\nYou do not have enough money! See you when you can afford healing.\n')
                  print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                else:
                  print('You have bought Medium healing package')
                  lifelist+=[35]
                  goldlist+=[-50]
                  return lifelist,goldlist

            elif h== 3:
                if gold<75:
                  print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                  print('\nYou do not have enough money! See you when you can afford healing.\n')
                  print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                else:
                  print('You have bought Large healing package')
                  lifelist+=[50]
                  goldlist+=[-75]
                  return lifelist,goldlist

            elif h== 4:
                if gold<50:
                  print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                  print('\nYou do not have enough money! See you when you can afford healing.\n')
                  print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                else:
                  print('You have bought Mana potion')
                  manalist+=[25]
                  goldlist+=[-50]
                  return manalist,goldlist

            elif h== 5:
                if gold<100:
                  print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                  print('\nYou do not have enough money! See you when you can afford healing.\n')
                  print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                else:
                  print('You have bought Rejuvenation potion')
                  lifelist+=[35]
                  manalist+=[35]
                  goldlist+=[-100]
                  return lifelist,manalist,goldlist

            elif h== 6:
                if gold<150:
                  print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                  print('\nYou do not have enough money! See you when you can afford healing.\n')
                  print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                else:
                  print('You have bought Turbo healing package')
                  lifelist+=[125]
                  goldlist+=[-150]
                  return lifelist,goldlist

            elif h== 7:
                print('\n********************************************************************\n')
                print('\nSee you next time, good-bye!\n')
                print('\n********************************************************************\n')
                break


def casino(gold,goldlist):
    if gold == 0:
        print('\nYou do not have any money, kiddo. Now, get lost!')
    else:
        print('''\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n''')
        print('\nWelcome to Casino Royal. Try your luck. Get rich or lose your gold!\n')
        print('OK,listen up! This is DIGITAL_BET.Rules are simple:\nFirst, you place your bet\nThen you choose your lucky number(1-6)\nThen it is time to see the result\n')
        print('\nAnd if you had winning number, you get 3 times of more money than you placed on bet! Got it, right?\n')

        while True:
            try:
                bet=int(input('How much money you want to place on bet?'))
                break
            except ValueError:
                print('Wrong input! Please enter valid number.')

        while gold - bet < 0:
                print('You do not have that money, kiddo. C\'mon, be serious!')
                while True:
                        try:
                            bet=int(input('How much money you want to place on bet?'))
                            break
                        except ValueError:
                            print('Wrong input! Please enter valid number.')
        else:
                goldlist+=[-bet]
                print('You put',bet,'gold on this bet.')
        if mana > 200:
            print('****!!!!!!!*****')
            print('Your psyonic aura is so strong that it has reprogramed DIGITAL_BET.\nNow you know that number wil be in range from 1 to 3!')
            lucky=int(input('Say your lucky number, kiddo. Remember, it\'s from 1 to 6!'))
            print('Your lucky number is',lucky)
            gamble=randint(1,3)
            print('DIGITAL_BET shows number',gamble)
            if gamble == lucky:
                print('Congrats! You did it, kiddo - you lucky bastard!')
                prize=bet*3
                goldlist+=[prize]
                return goldlist
            else:
                print('You lost, kiddo. Better luck next time!')
                return goldlist
        lucky=int(input('Say your lucky number, kiddo. Remember, it\'s from 1 to 6!'))
        print('Your lucky number is',lucky)
        gamble=randint(1,6)
        print('DIGITAL_BET shows number',gamble)
        if gamble == lucky:
              print('Congrats! You did it, kiddo - you lucky bastard!')
              prize=bet*3
              goldlist+=[prize]
              return goldlist
        else:
              print('You lost, kiddo. Better luck next time!')
              return goldlist


def traits(lifelist,manalist,goldlist):
    global name
    print('OK,',name,'let\'s begin! Choose your traits:')
    print('''Possibilities:
    1 - Regular guy/girl (default values: life = 100, mana = 100, gold = 0)
    ***************************************************************************
    2 - Rich kid (born in a wealthy family, have nice amount of cash,
    but growing-up in golden cradle spoiled your vitality  and spiritual powers)
    ***************************************************************************
    3 - Stalker\'s kid (your father was paid guide who led adventurers through
    forbidden zones of aliens landings. You are weak and poor, but nobody knows
    about your tremendous psyonic spiritual powers)
    ***************************************************************************
    4 - Daddy was Circus strongman (Your vitality is legendary, but your mental
    powers are below the average)
    ***************************************************************************
    ''')

    while True:
        try:
            birth=int(input('Enter number of your choice(1-4)::'))
            break
        except ValueError:
            print('Wrong input! Please enter valid number.')

    if birth == 1:
       print('********************************************************')
       print('You choose default starting stats.')
       print('********************************************************')
       goldlist+=[35]
       return lifelist,manalist,goldlist

    elif birth == 2:
         print('********************************************************')
         print('You are born with the golden spoon in your mouth.')
         print('********************************************************')
         lifelist+=[-15]
         manalist+=[-15]
         goldlist+=[85]
         return lifelist,manalist,goldlist

    elif birth == 3:
         print('********************************************************')
         print('''Other peoples sleep. You have visions of past and future.
               You are small, skiny and fragile. But dogs do not dare to
               bark at you!''')
         print('********************************************************')
         lifelist+=[-25]
         manalist+=[150]
         return lifelist,manalist,goldlist

    elif birth == 4:
         print('********************************************************')
         print('Kids in school called you Conan the Barbarian!')
         print('********************************************************')
         lifelist+=[150]
         manalist+=[-25]


def combat(lifelist,goldlist,damagelist,evadelist,life,gold,damage,evasion):
    if gold < 15:
        print('You do not have enough money to\n pay fee on entrance of Arena. Sorry!')
    else:
        print('Welcome to the Arena - home and workplace of brave warriors.\nStandard fee of 15 gold have been paid.')
        goldlist+=[15]
        print('''
              Now choose your challenge:
              1 - fight against Rad-zombie  (prize: 35 gold)
              2 - fight against Human-gladiator  (prize: 55 gold)
              3 - fight against Big-mutant-on-steroids  (prize: 75 gold)
              4 - fight against Cyborg
              5 - Let computer decide via random choice
              6 - I will skip the combat this time ...
              ''')

        while True:
            try:
                opponent=int(input('Enter number of your choice::'))
                break
            except ValueError:
                print('Wrong input! Please enter valid number.')

        if opponent == 1:
            print('You have chosen to fight against Rad-zombie.')
            radzombielife = 125
            evasion=sum(evadelist)//20
            print('**********************')
            print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion)
            print('Rad-zombie life:',radzombielife)
            print('Rad-zombie damage: 25')
            print('**********************')
            print('Rad-zombie says: - I\'M GONNA EAT YOUR BRAIN!!! AND YOUR TOES, ARRRRGH!!!')
            while radzombielife > 0 and life > 0:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print('Rad-zombie attacks!')
                print('*****************************************')
                attack=randint(1,3)

                while True:
                    try:
                        pl_block=int(input('Enter:\n1 - for HIGH BLOCK\n2 -for MIDDLE BLOCK\n3 - for LOW BLOCK\nEnter::'))
                        break
                    except ValueError:
                        print('Wrong input! Please enter valid number.')
                if attack == pl_block:
                              print('You succesfully blocked the attack!')
                else:
                              if attack == 1:
                                  print('Rad-zombie attacked your HEAD!')
                              elif attack == 2:
                                  print('Rad-zombie attacked your TORSO!')
                              elif attack == 3:
                                  print('Rad-zombie attacked your LEGS!')

                              print('You\'ve failed to block the attack!')

                              battlechance=randint(1,100)

                              num=sum(evadelist)//20

                              if battlechance >= 1 and battlechance <= num:
                                           print('You\'ve succesfully evaded the attack!')
                              else:
                                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                           print('You have been hit!')
                                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                           lifelist+=[-25]
                                           life=sum(lifelist)
                                           dmg(lifelist,manalist,damagelist)
                                           damage=sum(damagelist)//10
                                           evade(lifelist,manalist,evadelist)
                                           evasion=sum(evadelist)//20
                                           print('*****************')
                                           print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion,'\nRad-zombie life:',radzombielife)
                                           print('*****************')
                print('\nIt\'s YOUR TURN now. Choose your attack!')

                while True:
                    try:
                        pl_attack=int(input('Enter:\n1 - for HIGH ATTACK\n2 -for MIDDLE ATTACK\n3 - for LOW ATTACK\nEnter::'))
                        break
                    except ValueError:
                        print('Wrong input! Please enter valid number.')
                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                print(name,'attacks!')
                print('*****************************************')
                block=randint(1,3)
                if pl_attack == block:
                           print('Enemy has blocked your attack!')
                else:
                           print('You have hit that bastard!')
                           radzombielife-=damage
                           print('**********************')
                           print('Rad-zombie life:',radzombielife)
                           print('**********************')
            if life > 0 and radzombielife <= 0:
                print('YOU WIN!')
                goldlist+=[35]
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and radzombielife > 0:
                print('YOU LOSE!')
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and radzombielife <= 0:
                print('IT\'S A DRAW!')


        if opponent == 2:
            print('You have chosen to fight against Human-gladiator.')
            humgladlife = 175
            evasion=sum(evadelist)//20
            print('**********************')
            print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion)
            print('Human-gladiator life:',humgladlife)
            print('Human-gladiator damage: 35')
            print('**********************')
            print('Human-gladiator says: - YOU DON\'T HAVE A CHANCE AGAINST WELL-TRAINED GLADIATOR!')
            while humgladlife > 0 and life > 0:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print('Human-gladiator attacks!')
                print('*****************************************')
                attack=randint(1,3)

                while True:
                    try:
                        pl_block=int(input('Enter:\n1 - for HIGH BLOCK\n2 -for MIDDLE BLOCK\n3 - for LOW BLOCK\nEnter::'))
                        break
                    except ValueError:
                        print('Wrong input! Please enter valid number.')

                if attack == pl_block:
                              print('You succesfully blocked the attack!')
                else:
                              if attack == 1:
                                  print('Human-gladiator attacked your HEAD!')
                              elif attack == 2:
                                  print('Human-gladiator attacked your TORSO!')
                              elif attack == 3:
                                  print('Human-gladiator attacked your LEGS!')

                              print('You\'ve failed to block the attack!')

                              battlechance=randint(1,100)

                              num=sum(evadelist)//20

                              if battlechance >= 1 and battlechance <= num:
                                           print('You\'ve succesfully evaded the attack!')
                              else:
                                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                           print('You have been hit!')
                                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                           lifelist+=[-35]
                                           life=sum(lifelist)
                                           dmg(lifelist,manalist,damagelist)
                                           damage=sum(damagelist)//10
                                           evade(lifelist,manalist,evadelist)
                                           evasion=sum(evadelist)//20
                                           print('*****************')
                                           print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion,'\nHuman-gladiator life:',humgladlife)
                                           print('*****************')
                print('\nIt\'s YOUR TURN now. Choose your attack!')

                while True:
                    try:
                        pl_attack=int(input('Enter:\n1 - for HIGH ATTACK\n2 -for MIDDLE ATTACK\n3 - for LOW ATTACK\nEnter::'))
                        break
                    except ValueError:
                        print('Wrong input! Please enter valid number.')

                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                print(name,'attacks!')
                print('*****************************************')
                block=randint(1,3)
                if pl_attack == block:
                           print('Enemy has blocked your attack!')
                else:
                           print('You have hit that bastard!')
                           radzombielife-=damage
                           print('*************************')
                           print('Human-gladiator life:',humgladlife)
                           print('*************************')
            if life > 0 and humgladlife <= 0:
                print('YOU WIN!')
                goldlist+=[75]
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and humgladlife > 0:
                print('YOU LOSE!')
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and humgladlife <= 0:
                print('IT\'S A DRAW!')


        if opponent == 3:
            print('You have chosen to fight against Big-mutant-on-steroids.')
            mutantlife = 250
            evasion=sum(evadelist)//20
            print('**********************')
            print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion)
            print('Big-mutant-on-steroids life:',mutantlife)
            print('Big-mutant-on-steroids damage: 35')
            print('**********************')
            print('Big-mutant-on-steroids says: - GIT OVAH HERE, YOU LITTLE,PATHETIC WEAKLING!!!')
            while mutantlife > 0 and life > 0:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print('Big-mutant-on-steroids attacks!')
                print('*****************************************')
                attack=randint(1,3)

                while True:
                    try:
                        pl_block=int(input('Enter:\n1 - for HIGH BLOCK\n2 -for MIDDLE BLOCK\n3 - for LOW BLOCK\nEnter::'))
                        break
                    except ValueError:
                        print('Wrong input! Please enter valid number.')

                if attack == pl_block:
                              print('You succesfully blocked the attack!')
                else:
                              if attack == 1:
                                  print('Big-mutant-on-steroids attacked your HEAD!')
                              elif attack == 2:
                                  print('Big-mutant-on-steroids attacked your TORSO!')
                              elif attack == 3:
                                  print('Big-mutant-on-steroids attacked your LEGS!')

                              print('You\'ve failed to block the attack!')

                              battlechance=randint(1,100)

                              num=sum(evadelist)//20

                              if battlechance >= 1 and battlechance <= num:
                                           print('You\'ve succesfully evaded the attack!')
                              else:
                                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                           print('You have been hit!')
                                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                           lifelist+=[-50]
                                           life=sum(lifelist)
                                           dmg(lifelist,manalist,damagelist)
                                           damage=sum(damagelist)//10
                                           evade(lifelist,manalist,evadelist)
                                           evasion=sum(evadelist)//20
                                           print('*****************')
                                           print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion,'\nBig-mutant-on-steroids life:',mutantlife)
                                           print('*****************')
                print('\nIt\'s YOUR TURN now. Choose your attack!')

                while True:
                    try:
                        pl_attack=int(input('Enter:\n1 - for HIGH ATTACK\n2 -for MIDDLE ATTACK\n3 - for LOW ATTACK\nEnter::'))
                        break
                    except ValueError:
                        print('Wrong input! Please enter valid number.')

                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                print(name,'attacks!')
                print('*****************************************')
                block=randint(1,3)
                if pl_attack == block:
                           print('Enemy has blocked your attack!')
                else:
                           print('You have hit that bastard!')
                           mutantlife-=damage
                           print('*********************************')
                           print('Big-mutant-on-steroids life:',mutantlife)
                           print('*********************************')
            if life > 0 and mutantlife <= 0:
                print('YOU WIN!')
                goldlist+=[150]
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and mutantlife > 0:
                print('YOU LOSE!')
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and mutantlife <= 0:
                print('IT\'S A DRAW!')


        if opponent == 4:
            print('You have chosen to fight against Cyborg.')
            cyborglife = 300
            evasion=sum(evadelist)//20
            print('**********************')
            print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion)
            print('Cyborg life:',cyborglife)
            print('Cyborg damage: 55')
            print('**********************')
            print('Cyborg says: - ...SCANNER:ACTIVATED...TARGET:LOCKED...ALL SYSTEMS ENGAGE!!!')
            while cyborglife > 0 and life > 0:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print('Cyborg attacks!')
                print('*****************************************')
                attack=randint(1,3)

                while True:
                    try:
                        pl_block=int(input('Enter:\n1 - for HIGH BLOCK\n2 -for MIDDLE BLOCK\n3 - for LOW BLOCK\nEnter::'))
                        break
                    except ValueError:
                        print('Wrong input! Please enter valid number.')

                if attack == pl_block:
                              print('You succesfully blocked the attack!')
                else:
                              if attack == 1:
                                  print('Cyborg attacked your HEAD!')
                              elif attack == 2:
                                  print('Cyborg attacked your TORSO!')
                              elif attack == 3:
                                  print('Cyborg attacked your LEGS!')

                              print('You\'ve failed to block the attack!')

                              battlechance=randint(1,100)

                              num=sum(evadelist)//20

                              if battlechance >= 1 and battlechance <= num:
                                           print('You\'ve succesfully evaded the attack!')
                              else:
                                           critical=randint(1,6)
                                           cyborgcalc=randint(1,6)
                                           if critical == cyborgcalc:
                                               print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                               print('You have received CRITICAL hit!')
                                               print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                               lifelist+=[-100]
                                               life=sum(lifelist)
                                               dmg(lifelist,manalist,damagelist)
                                               damage=sum(damagelist)//10
                                               evade(lifelist,manalist,evadelist)
                                               evasion=sum(evadelist)//20
                                               print('*****************')
                                               print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion,'\nBig-mutant-on-steroids life:',cyborglife)
                                               print('*****************')

                                           else:
                                               print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                               print('You have been hit!')
                                               print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                               lifelist+=[-50]
                                               life=sum(lifelist)
                                               dmg(lifelist,manalist,damagelist)
                                               damage=sum(damagelist)//10
                                               evade(lifelist,manalist,evadelist)
                                               evasion=sum(evadelist)//20
                                               print('*****************')
                                               print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion,'\nCyborg life:',cyborglife)
                                               print('*****************')
                print('\nIt\'s YOUR TURN now. Choose your attack!')
                while True:
                    try:
                        pl_attack=int(input('Enter:\n1 - for HIGH ATTACK\n2 -for MIDDLE ATTACK\n3 - for LOW ATTACK\nEnter::'))
                        break
                    except ValueError:
                        print('Wrong input! Please enter valid number.')

                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                print(name,'attacks!')
                print('*****************************************')
                block=randint(1,3)
                if pl_attack == block:
                           print('Enemy has blocked your attack!')
                else:
                           print('You have hit that bastard!')
                           cyborglife-=damage
                           print('*********************************')
                           print('Cyborg life:',cyborglife)
                           print('*********************************')
            if life > 0 and cyborglife <= 0:
                print('YOU WIN!')
                goldlist+=[250]
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and cyborglife > 0:
                print('YOU LOSE!')
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and cyborglife <= 0:
                print('IT\'S A DRAW!')
                return goldlist,lifelist,damagelist,evadelist


        elif opponent == 5:
           opponent=randint(1,4)

           if opponent == 1:
            print('You have chosen to fight against Rad-zombie.')
            radzombielife = 125
            evasion=sum(evadelist)//20
            print('**********************')
            print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion)
            print('Rad-zombie life:',radzombielife)
            print('Rad-zombie damage: 25')
            print('**********************')
            print('Rad-zombie says: - I\'M GONNA EAT YOUR BRAIN!!! AND YOUR TOES, ARRRRGH!!!')
            while radzombielife > 0 and life > 0:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print('Rad-zombie attacks!')
                print('*****************************************')
                attack=randint(1,3)
                pl_block=int(input('Enter:\n1 - for HIGH BLOCK\n2 -for MIDDLE BLOCK\n3 - for LOW BLOCK\nEnter::'))
                if attack == pl_block:
                              print('You succesfully blocked the attack!')
                else:
                              if attack == 1:
                                  print('Rad-zombie attacked your HEAD!')
                              elif attack == 2:
                                  print('Rad-zombie attacked your TORSO!')
                              elif attack == 3:
                                  print('Rad-zombie attacked your LEGS!')

                              print('You\'ve failed to block the attack!')

                              battlechance=randint(1,100)

                              num=sum(evadelist)//20

                              if battlechance >= 1 and battlechance <= num:
                                           print('You\'ve succesfully evaded the attack!')
                              else:
                                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                           print('You have been hit!')
                                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                           lifelist+=[-25]
                                           life=sum(lifelist)
                                           dmg(lifelist,manalist,damagelist)
                                           damage=sum(damagelist)//10
                                           evade(lifelist,manalist,evadelist)
                                           evasion=sum(evadelist)//20
                                           print('*****************')
                                           print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion,'\nRad-zombie life:',radzombielife)
                                           print('*****************')
                print('\nIt\'s YOUR TURN now. Choose your attack!')
                pl_attack=int(input('Enter:\n1 - for HIGH ATTACK\n2 -for MIDDLE ATTACK\n3 - for LOW ATTACK\nEnter::'))
                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                print(name,'attacks!')
                print('*****************************************')
                block=randint(1,3)
                if pl_attack == block:
                           print('Enemy has blocked your attack!')
                else:
                           print('You have hit that bastard!')
                           radzombielife-=damage
                           print('**********************')
                           print('Rad-zombie life:',radzombielife)
                           print('**********************')
            if life > 0 and radzombielife <= 0:
                print('YOU WIN!')
                goldlist+=[35]
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and radzombielife > 0:
                print('YOU LOSE!')
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and radzombielife <= 0:
                print('IT\'S A DRAW!')


           if opponent == 2:
            print('You have chosen to fight against Human-gladiator.')
            humgladlife = 175
            evasion=sum(evadelist)//20
            print('**********************')
            print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion)
            print('Human-gladiator life:',humgladlife)
            print('Human-gladiator damage: 35')
            print('**********************')
            print('Human-gladiator says: - YOU DON\'T HAVE A CHANCE AGAINST WELL-TRAINED GLADIATOR!')
            while humgladlife > 0 and life > 0:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print('Human-gladiator attacks!')
                print('*****************************************')
                attack=randint(1,3)
                pl_block=int(input('Enter:\n1 - for HIGH BLOCK\n2 -for MIDDLE BLOCK\n3 - for LOW BLOCK\nEnter::'))
                if attack == pl_block:
                              print('You succesfully blocked the attack!')
                else:
                              if attack == 1:
                                  print('Human-gladiator attacked your HEAD!')
                              elif attack == 2:
                                  print('Human-gladiator attacked your TORSO!')
                              elif attack == 3:
                                  print('Human-gladiator attacked your LEGS!')

                              print('You\'ve failed to block the attack!')

                              battlechance=randint(1,100)

                              num=sum(evadelist)//20

                              if battlechance >= 1 and battlechance <= num:
                                           print('You\'ve succesfully evaded the attack!')
                              else:
                                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                           print('You have been hit!')
                                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                           lifelist+=[-35]
                                           life=sum(lifelist)
                                           dmg(lifelist,manalist,damagelist)
                                           damage=sum(damagelist)//10
                                           evade(lifelist,manalist,evadelist)
                                           evasion=sum(evadelist)//20
                                           print('*****************')
                                           print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion,'\nHuman-gladiator life:',humgladlife)
                                           print('*****************')
                print('\nIt\'s YOUR TURN now. Choose your attack!')
                pl_attack=int(input('Enter:\n1 - for HIGH ATTACK\n2 -for MIDDLE ATTACK\n3 - for LOW ATTACK\nEnter::'))
                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                print(name,'attacks!')
                print('*****************************************')
                block=randint(1,3)
                if pl_attack == block:
                           print('Enemy has blocked your attack!')
                else:
                           print('You have hit that bastard!')
                           radzombielife-=damage
                           print('*************************')
                           print('Human-gladiator life:',humgladlife)
                           print('*************************')
            if life > 0 and humgladlife <= 0:
                print('YOU WIN!')
                goldlist+=[75]
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and humgladlife > 0:
                print('YOU LOSE!')
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and humgladlife <= 0:
                print('IT\'S A DRAW!')


        if opponent == 3:
            print('You have chosen to fight against Big-mutant-on-steroids.')
            mutantlife = 250
            evasion=sum(evadelist)//20
            print('**********************')
            print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion)
            print('Big-mutant-on-steroids life:',mutantlife)
            print('Big-mutant-on-steroids damage: 35')
            print('**********************')
            print('Big-mutant-on-steroids says: - GIT OVAH HERE, YOU LITTLE,PATHETIC WEAKLING!!!')
            while mutantlife > 0 and life > 0:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print('Big-mutant-on-steroids attacks!')
                print('*****************************************')
                attack=randint(1,3)
                pl_block=int(input('Enter:\n1 - for HIGH BLOCK\n2 -for MIDDLE BLOCK\n3 - for LOW BLOCK\nEnter::'))
                if attack == pl_block:
                              print('You succesfully blocked the attack!')
                else:
                              if attack == 1:
                                  print('Big-mutant-on-steroids attacked your HEAD!')
                              elif attack == 2:
                                  print('Big-mutant-on-steroids attacked your TORSO!')
                              elif attack == 3:
                                  print('Big-mutant-on-steroids attacked your LEGS!')

                              print('You\'ve failed to block the attack!')

                              battlechance=randint(1,100)

                              num=sum(evadelist)//20

                              if battlechance >= 1 and battlechance <= num:
                                           print('You\'ve succesfully evaded the attack!')
                              else:
                                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                           print('You have been hit!')
                                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                           lifelist+=[-50]
                                           life=sum(lifelist)
                                           dmg(lifelist,manalist,damagelist)
                                           damage=sum(damagelist)//10
                                           evade(lifelist,manalist,evadelist)
                                           evasion=sum(evadelist)//20
                                           print('*****************')
                                           print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion,'\nBig-mutant-on-steroids life:',mutantlife)
                                           print('*****************')
                print('\nIt\'s YOUR TURN now. Choose your attack!')
                pl_attack=int(input('Enter:\n1 - for HIGH ATTACK\n2 -for MIDDLE ATTACK\n3 - for LOW ATTACK\nEnter::'))
                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                print(name,'attacks!')
                print('*****************************************')
                block=randint(1,3)
                if pl_attack == block:
                           print('Enemy has blocked your attack!')
                else:
                           print('You have hit that bastard!')
                           mutantlife-=damage
                           print('*********************************')
                           print('Big-mutant-on-steroids life:',mutantlife)
                           print('*********************************')
            if life > 0 and mutantlife <= 0:
                print('YOU WIN!')
                goldlist+=[150]
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and mutantlife > 0:
                print('YOU LOSE!')
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and mutantlife <= 0:
                print('IT\'S A DRAW!')


        if opponent == 4:
            print('You have chosen to fight against Cyborg.')
            cyborglife = 300
            evasion=sum(evadelist)//20
            print('**********************')
            print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion)
            print('Cyborg life:',cyborglife)
            print('Cyborg damage: 55')
            print('**********************')
            print('Cyborg says: - ...SCANNER:ACTIVATED...TARGET:LOCKED...ALL SYSTEMS ENGAGE!!!')
            while cyborglife > 0 and life > 0:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print('Cyborg attacks!')
                print('*****************************************')
                attack=randint(1,3)
                pl_block=int(input('Enter:\n1 - for HIGH BLOCK\n2 -for MIDDLE BLOCK\n3 - for LOW BLOCK\nEnter::'))
                if attack == pl_block:
                              print('You succesfully blocked the attack!')
                else:
                              if attack == 1:
                                  print('Cyborg attacked your HEAD!')
                              elif attack == 2:
                                  print('Cyborg attacked your TORSO!')
                              elif attack == 3:
                                  print('Cyborg attacked your LEGS!')

                              print('You\'ve failed to block the attack!')

                              battlechance=randint(1,100)

                              num=sum(evadelist)//20

                              if battlechance >= 1 and battlechance <= num:
                                           print('You\'ve succesfully evaded the attack!')
                              else:
                                           critical=randint(1,6)
                                           cyborgcalc=randint(1,6)
                                           if critical == cyborgcalc:
                                               print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                               print('You have received CRITICAL hit!')
                                               print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                               lifelist+=[-100]
                                               life=sum(lifelist)
                                               dmg(lifelist,manalist,damagelist)
                                               damage=sum(damagelist)//10
                                               evade(lifelist,manalist,evadelist)
                                               evasion=sum(evadelist)//20
                                               print('*****************')
                                               print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion,'\nBig-mutant-on-steroids life:',cyborglife)
                                               print('*****************')

                                           else:
                                               print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                               print('You have been hit!')
                                               print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                               lifelist+=[-50]
                                               life=sum(lifelist)
                                               dmg(lifelist,manalist,damagelist)
                                               damage=sum(damagelist)//10
                                               evade(lifelist,manalist,evadelist)
                                               evasion=sum(evadelist)//20
                                               print('*****************')
                                               print('Your life:',life,'\nYour damage:',damage,'\nYour evasion:',evasion,'\nCyborg life:',cyborglife)
                                               print('*****************')
                print('\nIt\'s YOUR TURN now. Choose your attack!')
                pl_attack=int(input('Enter:\n1 - for HIGH ATTACK\n2 -for MIDDLE ATTACK\n3 - for LOW ATTACK\nEnter::'))
                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                print(name,'attacks!')
                print('*****************************************')
                block=randint(1,3)
                if pl_attack == block:
                           print('Enemy has blocked your attack!')
                else:
                           print('You have hit that bastard!')
                           cyborglife-=damage
                           print('*********************************')
                           print('Cyborg life:',cyborglife)
                           print('*********************************')
            if life > 0 and cyborglife <= 0:
                print('YOU WIN!')
                goldlist+=[250]
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and cyborglife > 0:
                print('YOU LOSE!')
                return goldlist,lifelist,damagelist,evadelist
            elif life <= 0 and cyborglife <= 0:
                print('IT\'S A DRAW!')
                return goldlist,lifelist,damagelist,evadelist


start_time = time.time()
print('Your are surviving adventurer in post-apocalyptic world. \nYour goal is to earn 300 gold and not to die.\nYou can fight in the city Arena or go to on a journey.\n Journey is scavaging expedition into the wasteland around city.')
status(life,mana,gold,damage,evasion)
name=input('Enter your name::')

traits(lifelist,manalist,goldlist)
dmg(lifelist,manalist,damagelist)
evade(lifelist,manalist,evadelist)
life = sum(lifelist)
mana = sum(manalist)
gold = sum(goldlist)
damage = int(sum(damagelist)/10)
evasion = int(sum(evadelist)/20)


status(life,mana,gold,damage,evasion)

while gold<300:
         if life<=0:
             end_time =round (time.time() - start_time)
             print('You are DEAD!!! GAME OVER')
             print('Time of playing this game:',end_time,'seconds.')
             time.sleep(3)
             sys.exit()

         else:

             choose()
             dmg(lifelist,manalist,damagelist)
             evade(lifelist,manalist,evadelist)
             life = sum(lifelist)
             mana = sum(manalist)
             gold = sum(goldlist)
             damage =int(sum(damagelist)/10)
             evasion = int(sum(evadelist)/20)
             status(life,mana,gold,damage,evasion)
print('CONGRATULATIONS! You have won in this game!')
end_time = round (time.time() - start_time)
print('Time of playing this game:',end_time,'seconds.')
print('Your stats:\nLIFE:',life,'\nMANA:',mana,'\nGOLD:',gold)
time.sleep(3)
sys.exit()



