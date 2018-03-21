import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'drink_advisor_project.settings')

import django
django.setup()
from drinkadvisor.models import Drink, Feedback

def populate():

    feedback_1 = [
        {
            "content": "It is a nice drink. I drink it once a day at least.",
            "rate": 3
        },
        {
            "content": "That's awesome. It doesn't have that many calories and it is really tasty.",
            "rate": 5
        },
        {
            "content": "Awful drink. I suggest you to stop drinking it.",
            "rate": 1
        },
    ]

    feedback_2 = [
        {
            "content": "Where did you get that drink from? It looks really tasty and it doesn't"
                        "have a lot of calories. Great drink!",
            "rate": 3
        },
        {
            "content": "Saw it few times in the shop but never tried it. How is it?",
            "rate": None
        },
        {
            "content": "I don't like it. I tasted once and I vomited. I don't recommend it to anyone!",
            "rate": 0
        },
    ]

    feedback_3 = [
        {
            "content": "You always drink that. You better change!",
            "rate": 3
        },
        {
            "content": "My favourite drink!",
            "rate": 5
        },
        {
            "content": "How many times a day do you drink it?",
            "rate": 3
        },
    ]


    drinks = {
        "Fanta" : { "calories": 29, "picture": "fanta.jpg", "views":12, "feedback": feedback_1},
        "CocaCola" : { "calories" : 42, "picture": "coke.jpg", "views":12, "feedback": feedback_3},
        "CocaCola Zero": { "calories": 0.3, "sugar_free": True, "picture": "coca_cola_zero.jpg", "views":12, },
        "Powerade Berry": { "calories": 18, "energy": True, "picture": "powerade_berry.jpg", "views":12, "feedback": feedback_2}
    }


    for drink_name , properties in drinks.items():
        calories = properties["calories"]
        del properties["calories"]
        picture = properties["picture"]
        del properties["picture"]
        views = properties["views"]
        del properties["views"]




        drink = add_drink(drink_name, calories , picture, views, properties)

        if "feedback" in properties:
            for f in properties["feedback"]:
                print ("printing f = ", f)
                add_feedback(drink, f["content"], f["rate"])





def add_drink(name, calories, picture, views, *properties):

    drink = Drink.objects.get_or_create(name = name)[0]
    drink.calories = calories
    drink.picture = picture
    drink.views = views

    if not len(properties) ==0:
        print (properties)
        for property in properties:
            print ("this is a property ", property)
            for property_name, property_value in property.items():

                if property_name == "caffeine":
                    drink.caffeine = property_value
                elif property_name == "energy":
                    drink.isEnergyDrink = property_value
                elif  property_name == "feedback":
                    print ("feedback found ")
                else: # is sugar free
                    drink.isSugarFree = property_value


    drink.save()
    return drink

def add_feedback(drink, content, rate):

    f = Feedback.objects.get_or_create(drink = drink, content = content)[0]
    f.rate = rate
    f.save()
    return f


# Start execution here!
if __name__ == '__main__':
    print("Starting population script...")
    populate()