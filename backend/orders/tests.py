from django.test import TestCase
from .models import Customer, Order

class CustomerOrderTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="Michael Mike", code="12345")
        self.order = Order.objects.create(customer=self.customer, item="Laptop", amount=1500.00)

    def test_order_creation(self):
        self.assertEqual(self.order.item, "Laptop")
