from django.test import TestCase
from ..models import MenuItem


class TestMenu(TestCase):
    def test_menu_instance(self):
        item = MenuItem.objects.create(title='IceCream', price=80, inventory=100)
        self.assertEqual(item.__str__(), 'IceCream : 80')
        

        

        
        
