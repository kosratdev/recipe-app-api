from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "kosrat@dev.com"
        password = "kosrat123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test new user with normalized email"""
        email = "kosrat@DEV.com"
        user = get_user_model().objects.create_user(email, '123456')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '2342')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser('kosdf@ema.cm',
                                                         '234234')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
