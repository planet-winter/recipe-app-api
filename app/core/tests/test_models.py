from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test createing a user with an email address is successful"""
        email = "test@planets.world"
        password = "testpassword1234"
        user = get_user_model().objects.create_user(
            email=email
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(pasword))
