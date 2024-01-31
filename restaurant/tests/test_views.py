"""
restaurant\tests\test_views.py
"""
from decimal import Decimal
from unittest import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTests(TestCase):
    """
    MenuViewTests class
    """
    def setUp(self):
        """
        setUp method
        - Create Menu objects to run tests
        """
        self.client = APIClient()  # initialize client
        self.menu_item1 = Menu.objects.create(title='Broth', price=5.5, inventory=5) # create a menu item 1
        self.menu_item2 = Menu.objects.create(title='Chips', price=10.5, inventory=11) # create a menu item 2


    def test_getall(self):
        """
        Test view
        :return:
        """
        response = self.client.get('/restaurant/menu/items/') # fetch endpoint
        print(response.data)
        print(response.status_code)
        # format response to drop id field
        # id field output from response not easily predicted. Choose important data for comparison
        formated_response_data = [
            {
                "title":response_data["title"],
                "price":Decimal(response_data["price"]),
                "inventory":response_data["inventory"]
            }
            for response_data in response.data
        ]

        print(formated_response_data)

        # define expected data
        expected_data = [
                             {
                                 "title": "Broth",
                                 "price": Decimal("5.50"),
                                 "inventory": 5
                             },
                             {
                                 "title": "Chips",
                                 "price": Decimal("10.50"),
                                 "inventory": 11
                             }
                         ]
        # Check if you received 200 Ok!
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check data returned against expected
        self.assertEqual( formated_response_data, expected_data)
