from django.http import response
from django.test import TestCase
from django.urls import reverse


class TestSnacks(TestCase):
    def test_home_status_code(self):
        #Arrange
        url = reverse("home")

        #Act
        response = self.client.get(url).status_code

        #Assert
        self.assertEqual(response, 200)

    def test_snack_list_status_code(self):
        #Arrange
        url = reverse("snack_list")

        #Act
        response = self.client.get(url).status_code

        #Assert
        self.assertEqual(response, 200)

    def test_home_template(self):
        #Arrange
        url = reverse("home")

        #Act
        response = self.client.get(url)

        #Assert
        self.assertTemplateUsed(response, "home.html")        
        self.assertTemplateUsed(response, "base.html")

    def test_snack_list_template(self):
        #Arrange
        url = reverse("snack_list")

        #Act
        response = self.client.get(url)

        #Assert
        self.assertTemplateUsed(response, "snack_list.html")        
        self.assertTemplateUsed(response, "base.html")
              