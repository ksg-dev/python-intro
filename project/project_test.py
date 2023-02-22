import inquirer

sit_down = {'light-healthy' : 'Chopped',
            'Asian' : 'Umami',
            'steaks/burgers' : 'Firebirds'}

take_out = {'light-healthy' : 'Chipotle',
            'Asian' : 'Chinese',
            'steaks/burgers' : 'Cook Out'}

fast_food = {'light-healthy' : 'Burger King',
            'Asian' : 'Surin West',
            'steaks/burgers' : 'Cook Out'}

q = [
    inquirer.List('eat_how',
                message = 'What type of restaurant are you looking for?',
                choices = ['sit_down', 'take_out', 'fast_food']
                ),
    inquirer.List('category',
                message = 'What type of food?',
                choices = ['light-healthy', 'Asian', 'steaks/burgers'])
]

answers = inquirer.prompt(q)
d = answers["eat_how"]
f = answers["category"]
if d == "sit_down":
    sit = filter(lambda s: s[f])
    print(sit_down.category)


