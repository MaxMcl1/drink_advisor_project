import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'drink_advisor_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from drinkadvisor.models import DrinkProfile, Comment, UserProfile

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
        { "comment": "It is a nice drink. I drink it once a day at least.",  },

        { "comment": "That's awesome. It doesn't have that many calories and it is really tasty.",},

        {"comment": "Awful drink. I suggest you to stop drinking it.",},
    ]

    comments2 = [
        { "comment": "Where did you get that drink from? It looks really tasty and it doesn't"
                        "have a lot of calories. Great drink!",},

        { "comment": "Saw it few times in the shop but never tried it. How is it?", },

        { "comment": "I don't like it. I tasted once and I vomited. I don't recommend it to anyone!",},
    ]

    comments3 = [
        { "comment": "You always drink that. You better change!", },

        { "comment": "My favourite drink!", },

        { "comment": "How many times a day do you drink it?", },
    ]


    drinks = {
        "Fanta" : { "calories": 19, "sugar": 4, "picture": "profile_images/fanta.jpg", "feedback": comments1},
        "CocaCola" : { "calories" : 42, "sugar": 10,"picture": "profile_images/coke.jpg", "feedback": comments3},
        "CocaCola Zero": { "calories": 0, "sugar_free": True, "picture": "profile_images/coca_cola_zero.jpg" },
        "Red Bull" : { "calories": 45, "sugar": 11, "energy": True, "picture": "profile_images/redbull.png"  },
        "Sprite" : {  "calories" : 14, "sugar": 3, "picture": "profile_images/sprite.jpg"},
        "Oasis Light Peach and Passionfruit": {  "calories": 3, "sugar": 0, "picture": "profile_images/oasis.jpg"},
        "Powerade Berry": {  "calories": 18, "sugar": 4,"energy": True, "picture": "profile_images/powerade_berry.jpg",  "feedback": comments2}
    }


    for drink_name , properties in drinks.items():
        calories = properties["calories"]
        del properties["calories"]
        picture = properties["picture"]
        del properties["picture"]


        drink = add_drink(drink_name, calories , picture, properties)

        if "feedback" in properties:
            for f in properties["feedback"]:
                print ("printing f = ", f)
                add_feedback(drink, f["comment"])





def add_drink(name, calories, picture, *properties):

    drink = DrinkProfile.objects.get_or_create(name = name)[0]
    drink.calories = calories
    drink.picture = picture


    if not len(properties) == 0:
        print (properties)
        for property in properties:

            print ("this is a property ", property)
            for property_name, property_value in property.items():
                print ("property name = ", property_name)
                print ("property_value = ", property_value)
                if property_name == "sugar":
                    drink.sugar = property_value
                elif property_name == "energy":
                    drink.is_energy_drink = property_value
                elif property_name == "feedback":
                    continue
                else: # is sugar free
                    drink.sugar_free = property_value


    drink.save()
    return drink

def add_feedback(drink, comment):

    f = Comment.objects.get_or_create(drink = drink, comment = comment)[0]
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
    n_profile.picture = picture
    n_profile.save()
    return n_profile


# Start execution here!
if __name__ == '__main__':
    print("Starting population script...")
    populate()