#!/usr/bin/env python3

import sys
import requests

def help():
    print("Python Currency Converter help")
    print("Usage:")
    print("    <amount> <base currency> <target currency> - example: python-currency-converter 10 USD PLN")
    print("    -h - print this help message")

def arguments_validator():
    if (sys.argv[1].isdigit()) and (len(sys.argv[2]) == 3) and (len(sys.argv[3]) == 3):
        return True
    else:
        return False

def convert_currency():
    amount = sys.argv[1]
    base_currency = sys.argv[2]
    target_currency = sys.argv[3]

    # this function converts only from foreign currency to PLN
    def nbp_converter():
        response = requests.get("https://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json".format(base_currency))

        if response.status_code == 200:
            rates = response.json()['rates']
            last_rate = rates[0]

        mid_price = last_rate["mid"]
        var = mid_price * float(amount)
        print("{} {} {} {} {}".format(amount, base_currency.upper(), "=", var, "PLN"))

    nbp_converter()

# Flow

if len(sys.argv) == 4:
    if arguments_validator():
        convert_currency()
elif sys.argv[1] == "-h":
    help()
else:
    print("Wrong argument, check -h for help")