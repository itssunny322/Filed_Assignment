import unittest
from django.test import Client
from .views import *
from django.urls import reverse
import json



class PaymentTest(unittest.TestCase):


    def setUp(self):
        self.eventurl = reverse('process_payment')
        self.content_type = 'application/json'
        self.client= Client()

    def test_event_create(self):
        data = {
            "CreditCardNumber": 3233456723435642,
            "CardHolder": "Sunny",
            "ExpirationDate": "2021-03-02",
            "SecurityCode": 333,
            "Amount": 10
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(200, response.status_code)

    def test_event_for_cheap_payment_gateway(self):
        data = {
            "CreditCardNumber": 3233456723435642,
            "CardHolder": "Sunny",
            "ExpirationDate": "2021-03-02",
            "SecurityCode": 333,
            "Amount": 10
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(200, response.status_code)

    def test_event_for_expensive_payment_gateway(self):
        data = {
            "CreditCardNumber": 3233456723435642,
            "CardHolder": "Sunny",
            "ExpirationDate": "2021-03-02",
            "SecurityCode": 333,
            "Amount": 100
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(200, response.status_code)

    def test_event_for_expensive_payment_gateway(self):
        data = {
            "CreditCardNumber": 3233456723435642,
            "CardHolder": "Sunny",
            "ExpirationDate": "2021-03-02",
            "SecurityCode": 333,
            "Amount": 100
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(200, response.status_code)

    def test_event_for_premium_payment_gateway(self):
        data = {
            "CreditCardNumber": 3233456723435642,
            "CardHolder": "Sunny",
            "ExpirationDate": "2021-03-02",
            "SecurityCode": 333,
            "Amount": 100
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(200, response.status_code)

    def test_event_with_negative_amount(self):
        data = {
            "CreditCardNumber": 3233456723435642,
            "CardHolder": "Sunny",
            "ExpirationDate": "2021-03-02",
            "SecurityCode": 333,
            "Amount": -10
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(400, response.status_code)

    def test_event_with_invalid_card_number(self):
        data = {
            "CreditCardNumber": 323345672335642,
            "CardHolder": "Sunny",
            "ExpirationDate": "2021-03-02",
            "SecurityCode": 333,
            "Amount": 10
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(400, response.status_code)

    def test_event_with_negative_card_number(self):
        data = {
            "CreditCardNumber": "-323345672335642",
            "CardHolder": "Sunny",
            "ExpirationDate": "2021-03-02",
            "SecurityCode": 333,
            "Amount": 10
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(400, response.status_code)

    def test_event_with_alphanumeric_card_number(self):
        data = {
            "CreditCardNumber": "a323345672335642",
            "CardHolder": "Sunny",
            "ExpirationDate": "2021-03-02",
            "SecurityCode": 333,
            "Amount": 10
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(400, response.status_code)


    def test_event_with_invalid_date_fromat(self):
        data = {
            "CreditCardNumber": "a323345672335642",
            "CardHolder": "Sunny",
            "ExpirationDate": "02-03-2021",
            "SecurityCode": 333,
            "Amount": 10
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(500, response.status_code)

    def test_event_with_expire_date_before_today(self):
        data = {
            "CreditCardNumber": 323345672335642,
            "CardHolder": "Sunny",
            "ExpirationDate": "2020-03-02",
            "SecurityCode": 333,
            "Amount": 10
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(400, response.status_code)

    def test_event_with_invalid_security_code(self):
        data = {
            "CreditCardNumber": 323345672335642,
            "CardHolder": "Sunny",
            "ExpirationDate": "2020-03-02",
            "SecurityCode": 3331,
            "Amount": 10
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(400, response.status_code)

    def test_event_with_alphanumeric_security_code(self):
        data = {
            "CreditCardNumber": 323345672335642,
            "CardHolder": "Sunny",
            "ExpirationDate": "2020-03-02",
            "SecurityCode": "33a",
            "Amount": 10
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(400, response.status_code)

    def test_event_with_invalid_security_code2(self):
        data = {
            "CreditCardNumber": 323345672335642,
            "CardHolder": "Sunny",
            "ExpirationDate": "2020-03-02",
            "SecurityCode": 33,
            "Amount": 10
        }

        response = self.client.post(self.eventurl, data, format='json')
        self.assertEqual(400, response.status_code)
