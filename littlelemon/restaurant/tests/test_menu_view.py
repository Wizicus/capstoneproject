from django.test import TestCase
from ..models import MenuItem
from ..serializers import TestMenuSerializer


class TestMenuView(TestCase):
    def setup(self):
        item1 =  MenuItem.objects.create(title='IceCream', price=80, inventory=100)
        item2 =  MenuItem.objects.create(title='pie', price=60, inventory=100)
        item3 =  MenuItem.objects.create(title='cake', price=70, inventory=100)
        items = [item1,item2,item3]
        return items
        
    def test_getall(self):
        items = self.setup()
        expected_data = [{'title': 'IceCream', 'price': '80.00'}, {'title': 'pie', 'price': '60.00'}, {'title': 'cake', 'price': '70.00'}]
        serialized_data = TestMenuSerializer(items, many=True)
        for i in range(len(items)):
            self.assertEqual(serialized_data.data[i], expected_data[i])