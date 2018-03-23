import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'drink_advisor_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from drinkadvisor.models import DrinkProfile, CommentProfile, UserProfile

def populate():

    users = []
    pictures = []
    users_created = []

    with open("Users.txt", encoding='utf-8') as users_name_file, open("pictures_profile.txt") as pictures_file:
        for line in users_name_file:
            users.append(line.strip())

        for line in pictures_file:
            pictures.append(line.strip())

    i = 0
    for user in users:
        name = user.split(" ")[0]
        print ("name = " + name)
        surname = user.split(" ")[1]
        print ("surname = " + surname)
        picture = pictures[i]
        users_created.append(add_user(name = name, surname = surname, picture = picture))
        i += 1

    comments1 = [
        {
            "owner": users_created[0],
            "content": "It is a nice drink. I drink it once a day at least.",
            "rate": 3
        },
        {
            "owner": users_created[1],
            "content": "That's awesome. It doesn't have that many calories and it is really tasty.",
            "rate": 5
        },
        {
            "owner": users_created[2],
            "content": "Awful drink. I suggest you to stop drinking it.",
            "rate": 1
        },
    ]

    comments2 = [
        {
            "owner": users_created[0],
            "content": "Where did you get that drink from? It looks really tasty and it doesn't"
                        "have a lot of calories. Great drink!",
            "rate": 3
        },
        {
            "owner": users_created[3],
            "content": "Saw it few times in the shop but never tried it. How is it?",
            "rate": None
        },
        {
            "owner": users_created[10],
            "content": "I don't like it. I tasted once and I vomited. I don't recommend it to anyone!",
            "rate": 0
        },
    ]

    comments3 = [
        {
            "owner": users_created[9],
            "content": "You always drink that. You better change!",
            "rate": 3
        },
        {
            "owner": users_created[5],
            "content": "My favourite drink!",
            "rate": 5
        },
        {
            "owner": users_created[0],
            "content": "How many times a day do you drink it?",
            "rate": 3
        },
    ]


    drinks = {
        "Fanta" : { "owner": users_created[0],"calories": 19, "sugar": 4.6, "picture": "profile_images/fanta.jpg", "views":23, "feedback": comments1},
        "CocaCola" : { "owner": users_created[1],"calories" : 42, "sugar": 10.6,"picture": "profile_images/coke.jpg", "views":2, "feedback": comments3},
        "CocaCola Zero": { "owner": users_created[5], "calories": 0.3, "sugar_free": True, "picture": "profile_images/coca_cola_zero.jpg", "views":15 },
        "Red Bull" : { "owner": users_created[7],"calories": 45, "sugar": 11, "energy": True, "picture": "profile_images/redbull.png", "views":12, },
        "Sprite" : { "owner": users_created[8], "calories" : 14, "sugar": 3.3, "picture": "profile_images/sprite.jpg", "views":14},
        "Oasis Light Peach and Passionfruit": { "owner": users_created[3], "calories": 3.5, "sugar": 0.6, "picture": "profile_images/oasis.jpg", "views":0 },
        "Powerade Berry": { "owner": users_created[10], "calories": 18, "sugar": 4.1,"energy": True, "picture": "profile_images/powerade_berry.jpg", "views":9, "feedback": comments2}
    }


    for drink_name , properties in drinks.items():
        owner = properties["owner"]
        del properties["owner"]
        calories = properties["calories"]
        del properties["calories"]
        picture = properties["picture"]
        del properties["picture"]
        views = properties["views"]
        del properties["views"]




        drink = add_drink(owner ,drink_name, calories , picture, views, properties)

        if "feedback" in properties:
            for f in properties["feedback"]:
                print ("printing f = ", f)
                add_feedback(drink, f["owner"],  f["content"], f["rate"])





def add_drink(owner ,name, calories, picture, views, *properties):

    drink = DrinkProfile.objects.get_or_create(name = name, owner = owner)[0]
    drink.calories = calories
    drink.picture = picture
    drink.views = views

    if not len(properties) == 0:
        print (properties)
        for property in properties:
            print ("this is a property ", property)
            for property_name, property_value in property.items():

                if property_name == "sugar":
                    drink.sugar = property_value
                elif property_name == "energy":
                    drink.is_energy_drink = property_value
                elif  property_name == "feedback":
                    print ("feedback found ")
                else: # is sugar free
                    drink.sugar_free = property_value


    drink.save()
    return drink

def add_feedback(drink, owner, content, rate):

    f = CommentProfile.objects.get_or_create(drink = drink, owner = owner)[0]
    f.content = content
    f.rate = rate
    f.save()
    return f


user_id = 0
def add_user(name, surname, picture):

    global user_id
    user_id += 1

    user = User.objects.get_or_create( username= surname + "." + name[0] + str(user_id),
                                       email=name + str(user_id) + "@outlook.com")[0]
    random_password = User.objects.make_random_password()
    user.set_password(random_password)
    user.save()

    n_profile = UserProfile.objects.get_or_create(user=user)[0]
    n_profile.name = name
    n_profile.surname = surname
    n_profile.picture = picture
    n_profile.save()
    return n_profile


# Start execution here!
if __name__ == '__main__':
    print("Starting population script...")
    populate()