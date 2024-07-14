import requests
import json
from .models import Subscription 
from dotenv import load_dotenv
import os

load_dotenv()
def get_access_token():

  data = {
    'grant_type': 'client_credentials',
    }
  headers = {'Accept': 'application/json','Accept-Language': 'en-US'}

  client_id = os.getenv('CLIENT_ID')

  secret_key = os.getenv('SECRET_KEY')

  url = 'https://api.sandbox.paypal.com/v1/oauth2/token'

  r = requests.post(url, headers=headers, auth=(client_id, secret_key), data=data).json()

  access_token = r['access_token']
  # print(access_token)
  return access_token


def cancel_subscription_paypal(access_token, sub_id): #this function will cancel a subscription on paypal side 
  bearer_token = 'Bearer '+ access_token

  headers = {
    'Content-Type': 'application/json',
    'Authorization': bearer_token,
    }

  url  = 'https://api-m.sandbox.paypal.com/v1/billing/subscriptions/' + sub_id + '/cancel'

  r = requests.post(url, headers=headers)
  print(r.status_code)