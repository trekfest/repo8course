from django.test import TestCase
from .models import Menu

class MenuTest(TestCase):

    def test_menu_string_representation(self):
        # Add a new instance of the Menu model
        menu_item = Menu.objects.create(title="Test Menu Item", price=80)
        expected_representation = "Test Menu Item"
        self.assertEqual(str(menu_item), expected_representation)
