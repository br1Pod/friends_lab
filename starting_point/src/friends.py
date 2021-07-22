def get_name(person):
    person_name = person["name"]
    return person_name

def get_favourite_tv_show(show):
    show_name = show["favourites"]["tv_show"]
    return show_name

def likes_to_eat(person, food):
    favourite_food = person["favourites"]["snacks"]
    answer = food in favourite_food
    return answer

def add_friend(person, name):
    person["friends"].append(name)


def remove_friend(person, name):
    person["friends"].remove(name)

def total_money(people):
    total_cash = 0
    for cash in people:
        total_cash += cash["monies"]
    return total_cash

def l_money(person1, person2, money):
    person1["monies"] = person1["monies"] - money
    person2["monies"] = person2["monies"] + money


def all_favourite_foods(people):
    all_faves = []
    for food in people:
        person_fave = food["favourites"]["snacks"]
        for snack in person_fave:
            all_faves.append(snack)
    return all_faves


def find_no_friendends(person):
    no_mates = []
    for mates in person:
        if person["friends"] == []:
            no_mates.append(mates)
    return no_mates