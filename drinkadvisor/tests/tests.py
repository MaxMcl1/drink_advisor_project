from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse

from django.contrib.staticfiles import finders
import drinkadvisor.tests.test_utils as test_utils
from drinkadvisor.models import User, UserProfile, Comment
import os

class StaticFileTests(TestCase):

    def test_static_file_folder_exists(self):

        result = finders.find('')
        self.assertIsNotNone(result)

    def test_static_file_contains_css(self):

        result_1 = finders.find('drink_advisor_project/base.css')
        result_2 = finders.find('drink_advisor_project/drinks_css.css')

        self.assertIsNotNone(result_1)
        self.assertIsNotNone(result_2)

    def test_static_file_contains_images_folder(self):

        result = finders.find('images/')
        self.assertIsNotNone(result)



class TemplateTests(TestCase):
    # Check base.html exists inside template folder
    def test_base_template_exists(self):
        path_to_base = settings.TEMPLATE_DIR + '/drinkadvisor/base.html'
        print(path_to_base)
        self.assertTrue(os.path.isfile(path_to_base))






class UserProfileTests(TestCase):


    def test_user_profile_model(self):
        # Create a user
        user, user_profile = test_utils.create_user()

        # Check there is only the saved user and its profile in the database
        all_users = User.objects.all()
        self.assertEquals(len(all_users), 1)

        all_profiles = UserProfile.objects.all()
        self.assertEquals(len(all_profiles), 1)

        # Check profile fields were saved correctly
        all_profiles[0].user = user


class ViewsTests(TestCase):


    def test_drink_page_displays_comments(self):
        #Create categories in database
        drinks = test_utils.create_drinks()

        # Create comments for drinks
        test_utils.create_comments(drinks)

        # For each drink, access its page and check for the comments associated with it
        for drink in drinks:
            # Access drink page
            response = self.client.get(reverse('show_drink', args=[drink.slug]))

            # Retrieve comments for that drink
            comments = Comment.objects.filter(drink=drink)

            # Check comments are displayed and they have a comment
            for comment in comments:
                self.assertIn(comment.comment, response.content.decode('ascii'))
               