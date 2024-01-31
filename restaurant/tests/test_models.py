from django.test import TestCase

from restaurant.models import Menu
# Create your tests here.
class MenItemTest(TestCase):
    def test_get_item(self):
        """
        Test Menu model get_item method.
        """
        item = Menu.objects.create(title='Broth', price=5.50, inventory=5)
        item_str = item.get_item()

        self.assertEqual(item_str, 'Broth : 5.5')