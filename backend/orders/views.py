from rest_framework import viewsets
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .utils import send_sms_alert
from django.http import HttpResponse

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]



def perform_create(self, serializer):
    order = serializer.save()
    customer = order.customer
    send_sms_alert(customer.name, customer.code, order.item)




def home(request):
    return HttpResponse("Welcome to the Home Page Oauth2 works")
