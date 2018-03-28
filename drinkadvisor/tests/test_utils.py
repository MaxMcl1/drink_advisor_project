from drinkadvisor.models import Comment, DrinkProfile, User, UserProfile




def create_drinks():
    # List of drinks
    drinks = []

    # Create few random drinks
    for i in range(1, 11):
        bool = False
        # if i is even
        if (i % 2) == 0:
            bool = True
        drink = DrinkProfile(name = 'drink' + str(i),
                             calories = (i + 1 + i) % 10 +1,
                             sugar = i,
                             is_energy_drink = bool)

        drink.save()
        drinks.append(drink)

    return drinks


def create_comments(drinks):
    # List of comments
    comments = []

    # for each drink create 2 comments
    for i in range(0, len(drinks)):
        drink = drinks[i]

        # generate random comments
        for j in range(0, 2):
            content = "Hi! I am comment " + str(j)
            comment = Comment(drink = drink,
                              comment = content)

            comment.save()
            comments.append(comment)

    return comments

def create_user():
    user = User.objects.get_or_create(username='test_user_1', password='test_user_1',
                                      email='test_1@outlook.com')[0]

    user.set_password(user.password)
    user.save()

    user_1 = UserProfile.objects.get_or_create(user=user,
                                               website = "http://www.testuser.com")[0]
    user_1.save()

    return user, user_1