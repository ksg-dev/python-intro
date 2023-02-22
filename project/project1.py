import inquirer

eats = [
    {"name" : "Chipotle", "eat_how" : "take out", "category" : "light-healthy"},
    {"name" : "China Moon", "eat_how" : "take out", "category" : "Asian"},
    {"name" : "Umami", "eat_how" : "sit down", "category" : "Asian"},
    {"name" : "Firebirds", "eat_how" : "sit down", "category" : "steaks/burgers"},
    {"name" : "Burger King", "eat_how" : "fast food", "category" : "light-healthy"},
    {"name" : "Cook Out", "eat_how" : "fast food", "category" : "steaks/burgers"},
    {"name" : "Chopped", "eat_how" : "sit down", "category" : "light-healthy"},
    {"name" : "Surin West", "eat_how" : "fast food", "category" : "Asian"},
    {"name" : "FIVE", "eat_how" : "take out", "category" : "steaks/burgers"}
]

def main():
    restaurant = get_answers()
    if restaurant["eat_how"] == "sit down":
        sit = filter(lambda r: r["eat_how"] == "sit down", eats)
        for each in sorted(sit, key=lambda r: r["name"]):
            if each["category"] == restaurant["category"]:
                print(type(each["eat_how"]) + "  " + each["name"] + "  " + food(each["category"]))
    if restaurant["eat_how"] == "take out":
        take = filter(lambda r: r["eat_how"] == "take out", eats)
        for each in sorted(take, key=lambda r: r["name"]):
            if each["category"] == restaurant["category"]:
                print(type(each["eat_how"]) + "  " + each["name"] + "  " + food(each["category"]))
    if restaurant["eat_how"] == "fast food":
        fast = filter(lambda r: r["eat_how"] == "fast food", eats)
        for each in sorted(fast, key=lambda r: r["name"]):
            if each["category"] == restaurant["category"]:
                print(type(each["eat_how"]) + "  " + each["name"] + "  " + food(each["category"]))


def get_answers():
    q = [
        inquirer.List('eat_how',
                    message = 'What type of restaurant are you looking for?',
                    choices = ['sit down', 'take out', 'fast food']
                    ),
        inquirer.List('category',
                    message = 'What type of food?',
                    choices = ['light-healthy', 'Asian', 'steaks/burgers'])
    ]
    answers = inquirer.prompt(q)
    return answers

def food(category):
    match category:
            case "light-healthy":
                return "🥦"
            case "Asian":
                return "🍣"
            case "steaks/burgers":
                return "🥩"

def type(eat_how):
    match eat_how:
        case "sit down":
            return "🍽️"
        case "take out":
            return "🥡"
        case "fast food":
            return "🍔"




if __name__ == "__main__":
    main()