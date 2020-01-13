#!/usr/bin/env python3

import sys
import requests

amount = sys.argv[1]
base_currency = sys.argv[2]
target_currency = sys.argv[3]

def help():
    print("Python Currency Converter help")

def arguments_validator():
    if (sys.argv[1].isdigit()) and (len(sys.argv[2]) == 3) and (len(sys.argv[3]) == 3):
        return True
    else:
        return False

def convert_currency():

    def nbp_converter():
        response = requests.get("https://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json".format(base_currency))

        if response.status_code == 200:
            rates = response.json()['rates']
            last_rate = rates[0]

        mid_price = last_rate["mid"]
        print(mid_price)

    nbp_converter()






if len(sys.argv) == 4:
    if arguments_validator():
        convert_currency()
elif sys.argv[1] == "-h":
    help()
else:
    print("Wrong argument, check -h for help")