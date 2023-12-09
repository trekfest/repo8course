from django.test import TestCase
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        # Add test instances of the Menu model
        self.menu_item1 = Menu.objects.create(title="Test Menu Item 1", price=80, inventory=10)
        self.menu_item2 = Menu.objects.create(title="Test Menu Item 2", price=120, inventory=5)
        self.menu_item3 = Menu.objects.create(title="Test Menu Item 3", price=150, inventory=8)

    def test_getall(self):
       
        client = APIClient()
        response = client.get('/menu-items/')
        self.assertEqual(response.status_code, 200)
        expected_data = MenuSerializer([self.menu_item1, self.menu_item2, self.menu_item3], many=True).data
        self.assertEqual(response.data, expected_data)
