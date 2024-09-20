import os
import africastalking as at
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
username = os.getenv("USERNAME")

at.initialize(username, api_key)
sms = at.SMS

def send_sms_alert(customer_name, customer_number, order_item):
    message = f"Hello {customer_name}, your order for {order_item} has been placed."
    try:
        response = sms.send(message, [customer_number])
        print(response)
    except Exception as e:
        print(f"Error sending SMS: {e}")
