#     def attack(self, lawannya_siapa):
#     def attacked(self, yang_nyerang_siapa, attack_yang_nyerang_berapa):
class Hero:
    def __init__(self, name, HP, atk, defense):
        self.name = name
        self.HP = HP
        self.atk = atk
        self.defense = defense
    
    def attack(self, opp_name, opp_hp, opp_atk, opp_defense):
        self.opp_name = opp_name
        self.opp_hp = opp_hp
        self.opp_atk = opp_atk
        self.opp_defense = opp_defense

        damage = self.atk/self.opp_defense
        self.HP -= damage
        
        # print(f'HP {self.name} = {self.HP}')
        return self.HP

confirm = 'y'
while confirm == 'y':
    hero1 = Hero('Saitama',5000, 5000, 300)
    hero2 = Hero('Genos', 5000, 2000, 150)
    hero3 = Hero('Atomic Samurai', 5000, 3000, 175)
    hero_available = [hero1, hero2, hero3]
    
    while True:
        user_input_1 = input('Choose your first Hero!: ')
        if user_input_1.isnumeric() == False:
            print('Input must be in Integer and No Symbols!')
            continue
        elif int(user_input_1) < 1 or int(user_input_1) > len(hero_available):
            print(f'Input must be between 1 and {len(hero_available)}!')
            continue
        else:
            break    
    # hero_input_1 = int(user_input_1) - 1
    while True:
        user_input_2 = input('Choose your second Hero!: ')
        if user_input_2 == user_input_1:
            print('First Hero and Second Hero cannot be the same!')
            continue
        if user_input_2.isnumeric() == False:
            print('Input must be in Integer and No Symbols!')
            continue
        elif int(user_input_2) < 1 or int(user_input_2) > len(hero_available):
            print(f'Input must be between 1 and {len(hero_available)}!')
            continue
        else:
            break
    hero_input_1 = int(user_input_1) - 1
    hero_input_2 = int(user_input_2) - 1

    for i in hero_available:
        hero_chosen_1_name = hero_available[hero_input_1].name
    print(f'Hello my name is {hero_chosen_1_name}. I am a {hero_available[hero_input_1].__class__.__name__}!')

    for i in hero_available:
        hero_chosen_2_name = hero_available[hero_input_2].name
    print(f'Hello my name is {hero_chosen_2_name}. I am a {hero_available[hero_input_1].__class__.__name__}!') #instance.__class__.__name__

    print(f'''
    {hero_chosen_1_name}

      VS

    {hero_chosen_2_name}
    ''')
    battle_report = {}

    i = 1
    while True:
        if i % 2 == 0:
            hero_available[hero_input_2].attack(hero_chosen_1_name, hero_available[hero_input_1].HP, hero_available[hero_input_1].atk, hero_available[hero_input_1].defense)        
            # Append isi dictionary baru ke dictionary battle_report
            battle_report[i] = {'hero1': hero_available[hero_input_1].name, 'hp1': hero_available[hero_input_1].HP, 'hero2': hero_available[hero_input_2].name, 'hp2': hero_available[hero_input_2].HP, 'Attacker':hero_available[hero_input_1].name, 'Damage':hero_available[hero_input_2].atk/hero_available[hero_input_1].defense}
            i += 1
        else:
            hero_available[hero_input_1].attack(hero_chosen_2_name, hero_available[hero_input_2].HP, hero_available[hero_input_2].atk, hero_available[hero_input_2].defense)
            # Append isi dictionary baru ke dictionary battle_report
            battle_report[i] = {'hero1': hero_available[hero_input_1].name, 'hp1': hero_available[hero_input_1].HP, 'hero2': hero_available[hero_input_2].name, 'hp2': hero_available[hero_input_2].HP, 'Attacker':hero_available[hero_input_2].name, 'Damage':hero_available[hero_input_1].atk/hero_available[hero_input_2].defense}
            i += 1
            
        if hero_available[hero_input_1].HP <= 0:
            print(f'Fight ended in {i-1} round. The winner is {hero_available[hero_input_2].name}!')
            break
        elif hero_available[hero_input_2].HP <= 0:
            print(f'Fight ended in {i-1} round. The winner is {hero_available[hero_input_1].name}!')
            break
        else:
            continue
    
    # print(battle_report)
    confirm_battle_report = 'y'
    while confirm_battle_report == 'y':
        while True:
            battle_report_ask = input('Which round battle report that you want to inspect? (Fill with integer number): ')
            if battle_report_ask.isnumeric() == False:
                print('Input must be in Integer and No Symbols!')
                continue
            elif int(battle_report_ask) < 1 or int(battle_report_ask) > i-1:
                print(f'Input must be between 1 and {i-1}')
                continue
            else:
                # print(battle_report[int(battle_report_ask)])
                key_list_chosen_battle_report = list(battle_report[int(battle_report_ask)].keys())
                value_list_chosen_battle_report = list(battle_report[int(battle_report_ask)].values())
                for j in key_list_chosen_battle_report:
                    print(f'{j}: {value_list_chosen_battle_report[key_list_chosen_battle_report.index(j)]}')
                break

        inspect_confirm = 'y'
        while inspect_confirm == 'y':
            confirm_battle_report = input('Want to inspect another battle report? (y/n): ').lower()
            if confirm_battle_report == 'y':
                confirm_battle_report == 'y'
                break
            elif confirm_battle_report == 'n':
                # confirm_battle_report == 'n'
                break
            else:
                print('Fill with y or n!')
                inspect_confirm = 'y'

    while True:
        confirm = input('Play again? (y/n): ').lower()
        if confirm == 'y':
            confirm == 'y'
            break
        elif confirm == 'n':
            print('Thank you for playing.')
            confirm == 'n'
            exit()
        else: 
            print('Fill with y or n!')