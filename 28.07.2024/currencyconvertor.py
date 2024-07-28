import requests

def convert_currency(amount, from_currency, to_currency):
    api_key = 'your_api_key'  # Replace with your actual currency converter API key
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    response = requests.get(url)
    data = response.json()

    if to_currency in data['rates']:
        rate = data['rates'][to_currency]
        converted_amount = amount * rate
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print("Currency not found.")

amount = float(input("Enter amount: "))
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()
convert_currency(amount, from_currency, to_currency)
