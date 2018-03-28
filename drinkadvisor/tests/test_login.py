from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse

from django.contrib.staticfiles import finders
import drinkadvisor.tests.test_utils as test_utils
import os

class LoginTests(TestCase):

    def test_invalid_login_data_supplied(self):
        test_utils.create_user()
        logged_in = self.client.login(username='testuser', password='test_user')
        self.assertFalse(logged_in)

        logged_in = self.client.login(username='test_user', password='test_user_1')
        self.assertFalse(logged_in)

        logged_in = self.client.login(username='test_user_1', password='test_user_')
        self.assertFalse(logged_in)


    def test_correct_login_data_supplied(self):
        test_utils.create_user()
        logged_in = self.client.login(username='test_user_1', password='test_user_1')
        self.assertTrue(logged_in)

    # check if when logged in, in the index page we have urls to the pages accessible
    # by logged in person
    def test_url_reference_in_index_page_when_logged(self):
        # Create user and log in
        test_utils.create_user()
        self.client.login(username='test_user_1', password='test_user_1')

        # Access index page
        response = self.client.get(reverse('index'))

        # Check links that appear for logged person only
        self.assertIn(reverse('logout'), response.content.decode('ascii'))
        self.assertIn(reverse('profile'), response.content.decode('ascii'))


    # check if when not logged in, in the index page we have urls to the other pages
    # accessible for not logged in person
    def test_url_reference_in_index_page_when_not_logged(self):
        #Access index page with user not logged
        response = self.client.get(reverse('index'))

        # Check links that appear for not logged person
        self.assertIn(reverse('drinks'), response.content.decode('ascii'))
        self.assertIn(reverse('sugar_free'), response.content.decode('ascii'))
        self.assertIn(reverse('energy_drinks'), response.content.decode('ascii'))
        self.assertIn(reverse('about'), response.content.decode('ascii'))
        self.assertIn(reverse('register'), response.content.decode('ascii'))
        self.assertIn(reverse('login'), response.content.decode('ascii'))


    # check that we don't have access to the pages that require login
    def test_inappropriate_access_when_not_logged(self):

        drinks = test_utils.create_drinks()

        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/drinkadvisor/login/?next=/drinkadvisor/profile/',
                             status_code=302, target_status_code=200)

        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/drinkadvisor/login/?next=/drinkadvisor/logout/',
                             status_code=302, target_status_code=200)

        response = self.client.get(reverse('add_drink'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/drinkadvisor/login/?next=/drinkadvisor/add_drink/',
                             status_code=302, target_status_code=200)

        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/drinkadvisor/login/?next=/drinkadvisor/edit_profile/',
                             status_code=302, target_status_code=200)

        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/drinkadvisor/login/?next=/drinkadvisor/change_password/',
                             status_code=302, target_status_code=200)


        response = self.client.get(reverse('add_comment', args=[drinks[0].slug]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/drinkadvisor/login/?next=/drinkadvisor/drink/' + drinks[0].slug +'/add_comment/',
                             status_code=302, target_status_code=200)


    # check that once logged in, we have access to the pages for registered users
    def test_appropriate_access_when_logged(self):
        # Create user and log in
        test_utils.create_user()
        self.client.login(username='test_user_1', password='test_user_1')

        # create a list of drinks and see the status code
        drinks = test_utils.create_drinks()

        # try to go to the profile page and see the status code
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

        # try to go to the add_drink_page and see the status code
        response = self.client.get(reverse('add_drink'))
        self.assertEqual(response.status_code, 200)

        # try to go to the edit_profile page and see the status code
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)

        # try to go to the change_password page and see the status code
        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200)

        # try to go to the add_comment page and see the status code
        response = self.client.get(reverse('add_comment', args=[drinks[0].slug]))
        self.assertEqual(response.status_code, 200)

        # try to logout and see the status code
        # should be run as last otherwise it will log out and get wrong status code for the others
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/drinkadvisor/',
                             status_code=302, target_status_code=200)


    def test_login_provides_error_message(self):
        # Access login page
        try:
            response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpass'})
        except:
            try:
                response = self.client.post(reverse('drinkadvisor:login'), {'username': 'wronguser', 'password': 'wrongpass'})
            except:
                return False

        try:
            self.assertIn('wronguser', response.content.decode('ascii'))
        except:
            self.assertIn('Invalid login details supplied.', response.content.decode('ascii'))
