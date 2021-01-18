# -*- coding: utf-8 -*-
from random import randint
import time
import sys

# Global variables

winning_amount = 300
arena_fee = 15

# Player start variables

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

def calculate_damage(lifelist,manalist,damagelist):
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

def user_input():
    try:
        return int(input('Enter number of your choice::')) 
    except ValueError:
            print('Wrong input! Please enter valid number.')


def prompt_loop(end_value: int):
    while True:
        user_choice = user_input()
        if user_choice in tuple(range(1, end_value)):
            break
    return user_choice




def journey ():
    global life, mana, gold, damage, lifelist, manalist, goldlist
    x = randint(1, 12)
    if x == 1:
        print('You were victim of raiders attack!')
        if damage > 50:
              print('You killed them all and took their posessions, you crazy destroyer!')
              goldlist+=[15]
        elif damage > 30:
              lifelist+=[-5]
              print('It was tough, but you show them who is the boss!')
        else:
          lifelist+=[-20]
          if gold >= 10:
              goldlist+=[-10]
          else:
              manalist+=[-10]
    elif x == 2:
        print('You passed through vampiric aura forest!')
        if mana >= 20 and life >= 50:
              manalist += [-20]
        elif mana >= 20 and life < 50:
              lifelist += [25]
              manalist += [-20]
        elif mana < 20 and life >= 50:
              lifelist += [-30]
    elif x == 3:
        print('You found hidden stash that belongs to raiders.')
        goldlist += [35]
        lifelist += [15]
        manalist += [10]
    elif x == 4:
        print('You found abandoned supermarket.')
        lifelist += [35]
        manalist += [15]
        goldlist += [20]
    elif x == 5:
        if mana > 250:
            print("""Your powerfull psyonic aura has scarred hidden Rad-Snake!
            She has ran away, leaving one of her expensive eggs.Bingo!
            But toxins from the egg damage your skin.""")
            lifelist += [-25]
            goldlist += [15]
        else:
            print('You have been bitten by poisonous mutated Rad-Snake!')
            if life >= 150:
                 lifelist += [-125]
            elif life >= 100:
                 lifelist += [-75]
            else:
                 lifelist += [-50]
    elif x == 6:
        print("""You have found and ate some \'magic\' mushrooms. 
        You have some unreal visions, but you feel little sick now.""")
        manalist += [15]
        lifelist += [-20]
    elif x == 7:
        print("""You found members of Cyber-Scientology cult. 
        Those strange felows share their food with you 
        and give you some of coins they have. 
        They explained to you their strange beliefs.
        They believe that whole Universe is just computer program!
        You find it funny, but you feel your spirituality have risen...""")
        lifelist += [5]
        manalist += [5]
        goldlist += [5]
    elif x == 8:
        print('You have found a bag of gold!')
        goldlist += [25]
    elif x == 9:
        print('You have found a package of meat-cans and energy-drinks!')
        lifelist += [25]
    elif x == 10:
        print('You have stepped on improvised landmine! It hurts like hell!')
        lifelist += [-30]
    elif x == 11:
        print("""You have searched for gold in river. 
        You have found a little bit of it, 
        but blood-sucking water worms have bitten your legs!""")
        goldlist += [10]
        lifelist += [-15]
    elif x == 12:
        print("""You are suddenly feeling sick. 
        With your Geiger-counter you discover that some
        of your gold is irradiated - you will have to throw it away,
        before radiation disease become serious!""")
        if gold >= 15:
           goldlist += [-15]
        else:
           goldlist.pop()
        lifelist += [-10]


def show_player_stats(life,mana,gold,damage,evasion):
    print('********')
    print('Your stats:\nLIFE:',life,'\nMANA:',mana,'\nGOLD:',gold,'\nDAMAGE:',damage,'\nEVASION:',evasion)
    print('********')


def choose_player_action():
    print('It is time to choose your path adventurer! Choose wisely:\n 1 - Go on a journey to search for gold.'
          '\n 2 - Fight in Arena to win a prize.\n 3 - Go to hospital for healing (if you have gold!).\n 4 - Gamble at casino.')
    choice = prompt_loop(5)
    if choice == 1 :
               print('You put on your hat and backpack. Time to go on a journey...')
               print('**********************************************************')
               journey()
               print('**********************************************************')
    elif choice == 2:
               print('You decided to test your luck and your skills in the Arena. Prepare for battle!')
               print('**********************************************************')
               combat(lifelist,goldlist,damagelist,evadelist,life,gold,damage,evade)
               print('**********************************************************')
    elif choice == 3:
               print('\nYou are aware that your wounds need healing. But, it will cost you some gold...\n')
               print('**********************************************************')
               hospital(lifelist,manalist,goldlist,gold)
               print('**********************************************************')
    elif choice == 4:
               print('You decided to try your luck at casino. Good luck!')
               print('**********************************************************')
               casino(gold,goldlist)
               print('**********************************************************')


def no_money_msg():
    print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
    print('\nYou do not have enough money! See you when you can afford healing.\n')
    print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')


def hospital(lifelist,manalist,goldlist,gold):
    if gold < 25:
        no_money_msg()
    else:
        while gold > 0:
            print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
            print('''\nWelcome to the City Hospital. Choose one of our services:\n1 - Small healing package (life: +15, price: 25 gold)
            \n2 - Medium healing package (life: +35, price: 50 gold)\n3 - Large healing package (life: +50, price: 75 gold)
            \n4 - Mana potion (mana: +25, price: 50 gold)\n5 - Rejuvenation potion (life: +35, mana: +35, price: 100 gold)
            \n6 - Turbo healing package (life: +125, price: 150 gold)\n7 - Not interested, thank you!''')
            hospital_choice = prompt_loop(8)
            if hospital_choice == 1:
                  print('You have bought Small healing package.')
                  lifelist += [15]
                  goldlist += [-25]
                  return lifelist,goldlist
            elif hospital_choice == 2:
                if gold<50:
                  no_money_msg()
                else:
                  print('You have bought Medium healing package')
                  lifelist += [35]
                  goldlist += [-50]
                  return lifelist,goldlist
            elif hospital_choice == 3:
                if gold < 75:
                  no_money_msg()
                else:
                  print('You have bought Large healing package')
                  lifelist += [50]
                  goldlist += [-75]
                  return lifelist,goldlist
            elif hospital_choice == 4:
                if gold<50:
                  no_money_msg()
                else:
                  print('You have bought Mana potion')
                  manalist+=[25]
                  goldlist+=[-50]
                  return manalist,goldlist

            elif hospital_choice == 5:
                if gold<100:
                  no_money_msg()
                else:
                  print('You have bought Rejuvenation potion')
                  lifelist+=[35]
                  manalist+=[35]
                  goldlist+=[-100]
                  return lifelist,manalist,goldlist

            elif hospital_choice == 6:
                if gold<150:
                  no_money_msg()
                else:
                  print('You have bought Turbo healing package')
                  lifelist+=[125]
                  goldlist+=[-150]
                  return lifelist,goldlist

            elif hospital_choice == 7:
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
        bet = prompt_loop(gold + 1)
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
            print('DIGITAL_BET shows number', gamble)
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


def choose_player_traits():
    global name, lifelist, manalist, goldlist
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
    
    birth = prompt_loop(5)
    if birth == 1:
       print('********************************************************')
       print('You choose default starting stats.')
       print('********************************************************')
       goldlist+=[35]
    elif birth == 2:
         print('********************************************************')
         print('You are born with the golden spoon in your mouth.')
         print('********************************************************')
         lifelist+=[-15]
         manalist+=[-15]
         goldlist+=[85]
    elif birth == 3:
         print('********************************************************')
         print('''Other peoples sleep. You have visions of past and future.
               You are small, skiny and fragile. But dogs do not dare to
               bark at you!''')
         print('********************************************************')
         lifelist+=[-25]
         manalist+=[150]
    elif birth == 4:
         print('********************************************************')
         print('Kids in school called you Conan the Barbarian!')
         print('********************************************************')
         lifelist+=[150]
         manalist+=[-25]


def is_any_fighter_lost(player_life, enemy_life):
    global goldlist
    if player_life > 0 and enemy_life <= 0:
        print('YOU WIN!')
        goldlist+=[250]
    elif player_life <= 0 and enemy_life > 0:
        print('YOU LOSE!')
    elif player_life <= 0 and enemy_life <= 0:
        print('IT\'S A DRAW!')


def you_lose(player_life):
    if player_life <= 0:
        end_time = round (time.time() - start_time)
        print('You are DEAD!!! GAME OVER')
        print('Time of playing this game:',end_time,'seconds.')
        time.sleep(3)
        sys.exit()


def you_won():
    print('CONGRATULATIONS! You have won in this game!')
    end_time = round (time.time() - start_time)
    print('Time of playing this game:',end_time,'seconds.')
    print('Your stats:\nLIFE:',life,'\nMANA:',mana,'\nGOLD:',gold)
    time.sleep(3)
    sys.exit()


def action_success(action_number: int, subject: str, object: str, action: str):
    action_number -= 1
    body_region = ('HEAD', 'TORSO', 'LEGS')
    if action == 'attack':
        object_action = 'block'
        print(f"{subject} {action}ed {object}'s {body_region[action_number]}!")
    elif action == 'block':
        object_action = 'attack'
        print(f"{subject} {action}ed {object}'s {object_action} to the {body_region[action_number]}!")
    print(f"{object}'s {object_action} failed!")


def show_life_after_attack(actor_life: int, actor_name: str):
    print('**********************')
    print(f'{actor_name} life: {actor_life}')
    print('**********************')


def duel(enemy_name: str, enemy_life: int, enemy_damage: int, enemy_says: str):
    global life, damage, evasion, lifelist, manalist, damagelist
    print(f'You have chosen to fight against {enemy_name}.')
    evasion = sum(evadelist) // 20
    print('**********************')
    print(f'Your life: {life}\nYour damage: {damage}\nYour evasion: {evasion}')
    print(f'{enemy_name} life: {enemy_life}\n{enemy_name} damage: {enemy_damage}')
    print('**********************')
    print(f'{enemy_name} says: - {enemy_says}')
    while enemy_life > 0 and life > 0:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print(f'{enemy_name} attacks!')
        print('*****************************************')
        enemy_attack = randint(1,3)
        print('Enter:\n1 - for HIGH BLOCK\n2 -for MIDDLE BLOCK\n3 - for LOW BLOCK\n')
        player_block = prompt_loop(4)
        if enemy_attack == player_block:
            action_success(player_block, name, enemy_name, 'block')
        else:
            action_success(enemy_attack, enemy_name, name, 'attack')  
            battlechance = randint(1, 100)    
            num = sum(evadelist) // 20    
            if battlechance >= 1 and battlechance <= num:
                print(f'{name} succesfully evaded the attack!')
            else:
                lifelist += [-enemy_damage]
                life = sum(lifelist)
                calculate_damage(lifelist, manalist, damagelist)
                damage = sum(damagelist) // 10
                evade(lifelist, manalist, evadelist)
                evasion = sum(evadelist) // 20
                show_life_after_attack(life, name)
                you_lose(life)
        print('\nIt\'s YOUR TURN now. Choose your attack!')
        print('Enter:\n1 - for HIGH ATTACK\n2 -for MIDDLE ATTACK\n3 - for LOW ATTACK\n')
        player_attack = prompt_loop(4)
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        print(f'{name} attacks!')
        print('*****************************************')
        enemy_block = randint(1, 3)
        if player_attack == enemy_block:
            action_success(enemy_block, enemy_name, name, 'block')
        else:
            action_success(player_attack, name, enemy_name, 'attack')
            enemy_life -= damage
            show_life_after_attack(enemy_life, enemy_name)
    is_any_fighter_lost(life, enemy_life)


def combat(lifelist, goldlist, damagelist, evadelist, life, gold, damage, evasion):
    if gold < arena_fee:
        print("""You do not have enough money to
        pay fee on entrance of Arena. Sorry!""")
    else:
        print('Welcome to the Arena - home and workplace of brave warriors.')
        print(f'Standard fee of {arena_fee} gold have been paid.')
        goldlist+=[-arena_fee]
        print('''
              Now choose your challenge:
              1 - fight against Rad-zombie  (prize: 35 gold)
              2 - fight against Human-gladiator  (prize: 55 gold)
              3 - fight against Big-mutant-on-steroids  (prize: 75 gold)
              4 - fight against Cyborg
              5 - Let computer decide via random choice
              6 - I will skip the combat this time ...
              ''')
        opponent = prompt_loop(7)
        if opponent == 5:
           opponent = randint(1,4)
        if opponent == 1:
            enemy_words = 'I\'M GONNA EAT YOUR BRAIN!!! AND YOUR TOES, ARRRRGH!!!'
            duel('Rad-Zombie', 125, 25, enemy_words)
        elif opponent == 2:
            enemy_words = 'YOU DON\'T HAVE A CHANCE AGAINST WELL-TRAINED GLADIATOR!'
            duel('Human-Gladiator', 175, 25, enemy_words)
        elif opponent == 3:
            enemy_words = 'GIT OVAH HERE, YOU LITTLE,PATHETIC WEAKLING!!!'
            duel('Big-Mutant-On-Steroids', 250, 35, enemy_words)
        elif opponent == 4:
            enemy_words = '...SCANNER:ACTIVATED...TARGET:LOCKED...ALL SYSTEMS ENGAGE!!!'
            duel('Cyborg', 300, 55, enemy_words)
        elif opponent == 6:
            print(f'Courage have left you {name}, right. See you next time cry-baby.')

### START OF GAME - LIKE 'MAIN'
start_time = time.time()
print("""Your are surviving adventurer in post-apocalyptic world.
Your goal is to earn 300 gold and not to die.
You can fight in the city Arena or go to on a journey.
Journey is scavaging expedition into the wasteland around city.""")
name = input('Enter your name::')
choose_player_traits()
calculate_damage(lifelist,manalist,damagelist)
evade(lifelist,manalist,evadelist)
life = sum(lifelist)
mana = sum(manalist)
gold = sum(goldlist)
damage = int(sum(damagelist) / 10)
evasion = int(sum(evadelist) / 20)
show_player_stats(life, mana, gold, damage, evasion)
while (gold < winning_amount):
         if life <= 0:
             you_lose(life)
         else:
             choose_player_action()
             calculate_damage(lifelist, manalist, damagelist)
             evade(lifelist, manalist, evadelist)
             life = sum(lifelist)
             mana = sum(manalist)
             gold = sum(goldlist)
             damage =int(sum(damagelist) / 10)
             evasion = int(sum(evadelist) / 20)
             show_player_stats(life, mana, gold, damage, evasion)
you_won()