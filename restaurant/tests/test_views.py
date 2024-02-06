"""
restaurant\tests\test_views.py
"""
import logging
import traceback
from decimal import Decimal
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

logging.basicConfig(format='%(asctime)s - %(levelname)s - Logging from line No: %(lineno)d. \nScript: %(pathname)s.\nMessage: %(message)s',
                           datefmt='%d-%m-%Y  %H:%M:%S',level=logging.DEBUG)

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
        :return: None
        """
        try:
            response = self.client.get('/restaurant/menu/items') # fetch endpoint
            logging.debug(f"response: {response}")
            logging.debug(f"response data: {response.data}")
            logging.debug(f"response status code: {response.status_code}")
            # Format response to drop id field
            #  from response dat is not easily predicted.Choose important data for comparison
            formatted_response_data = [
                {
                    "title":response_data["title"],
                    "price":Decimal(response_data["price"]),
                    "inventory":response_data["inventory"]
                }
                for response_data in response.data
            ]
            logging.debug(f"formatted response data: {formatted_response_data}")

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
            self.assertEqual( formatted_response_data, expected_data)

        except Exception as e:
            # Option 1: Log the traceback using logging modul
            logging.error(f"This exception occurred: {e}", exc_info=True)

            # Option 2: Extract the general traceback information using traceback module then log it.
            # Similar to option 1, in fact no much difference can be observed of the logs outputs from both options.

            traceback_info = traceback.format_exc()
            # Log the traceback information
            logging.error(f"Traceback General information:\n{traceback_info}")

            # Option 3: Extract the traceback information using traceback module then log it
            # Different from option 2 because you log line by line-specific detail about the traceback.
            # In this option, you are able to select information needed or leave out unnecessary information
            logging.error("Logging Traceback information line by line:\n")
            traceback_info = traceback.extract_tb(e.__traceback__)

            # Log each frame of the traceback

            for frame in traceback_info:
                log_message = f"\nFile: {frame.filename},\nException occurred at line: {frame.lineno},\nFunction: {frame.name}"
                logging.error(log_message)
            logging.error(f"Exception occurred: {e}")
