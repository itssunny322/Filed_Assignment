from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from .models import *
from rest_framework import status
from datetime import datetime,date
import re
# Create your views here.



def cheap_payment_gateway(amount):
    try:
        if int(amount)<=20:
            return "Accepted1"
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def premium_payment_gateway(amount):
    try:
        if int(amount)>=500:
            return "Accepted2"
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def process_payment(request):
    if request.method == 'POST':
        try:
            payment = Details()
            payment.CreditCardNumber = request.POST['CreditCardNumber']
            payment.CardHolder = request.POST['CardHolder']
            payment.ExpirationDate = request.POST['ExpirationDate']
            payment.SecurityCode = request.POST['SecurityCode']
            payment.Amount = request.POST['Amount']


            expiry = datetime.strptime(request.POST['ExpirationDate'], "%Y-%m-%d").date()

            cc_number = request.POST['CreditCardNumber']
            security_code = request.POST['SecurityCode']

            if len(str(request.POST['CreditCardNumber'])) != 16  :
                return Response({'ValidationError': 'Invalid creditcard number,given credit card number is less than or more than 16 digits,Please provide a valid creditcard number to proceed'},
                                status=status.HTTP_400_BAD_REQUEST)

            elif cc_number.isdigit() == False:
                return Response({'ValidationError': 'Invalid creditcard number, its should not include special character or aplhabets,Please provide a valid creditcard number to proceed'},
                                status=status.HTTP_400_BAD_REQUEST)

            elif expiry < date.today():
                return Response({'ValidationError': "Expiry date cant be less than today's date"},
                                status=status.HTTP_400_BAD_REQUEST)
            elif len(str(request.POST['SecurityCode'])) != 3:
                return Response({'ValidationError': "Invalid Security code , please enter correct one to proceed"},
                                status=status.HTTP_400_BAD_REQUEST)
            elif security_code.isdigit() == False:
                return Response({'ValidationError': "Invalid Security code , it should not include special character or alphabets, please enter correct one to proceed"},
                                status=status.HTTP_400_BAD_REQUEST)
            elif int(request.POST['Amount']) <0:
                return Response({'ValidationError': "Invalid Amount , please enter correct one to proceed"},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                if cheap_payment_gateway (request.POST['Amount']) == "Accepted1":
                    payment.save()
                    return Response({'response': 'your payment done successfully via cheap payment gateway'}, status=status.HTTP_200_OK)
                elif premium_payment_gateway (request.POST['Amount']) == "Accepted2":
                    payment.save()
                    return Response({'response': 'your payment done successfully via premium payment gateway'}, status=status.HTTP_200_OK)
                else:
                    payment.save()
                    return Response({'response': 'your payment done successfully via expensive payment gateway'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


