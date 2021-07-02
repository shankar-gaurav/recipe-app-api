from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    
    def test_create_user_with_email_successfull(self):
        """Test creating a new user with an email is successfull""" 
        email = 'testgrv@email.com'
        password = 'testPswd'

        user = get_user_model().objects.create_user(

                email=email,
                password=password
        )

        self.assertEqual(user.email,email)
        #user.check_password(password) --> check_password comes with user django model to compare password 
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""

        email = 'test@LONDONGRV.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='test123'
            
        )

        self.assertEqual(user.email,email.lower())


    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        """ when we dont pass email addres while creating a new user, raises value error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')


    def test_create_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@grvappdev.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        





