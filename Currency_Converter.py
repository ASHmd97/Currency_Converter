import requests


url = "https://api.apilayer.com/fixer/symbols"

payload = {}
headers= {
  "apikey": "AttXxZ1mKVs3oJqRWedfvy38rg81F8G9"
}

sym_response = requests.request("GET", url, headers=headers, data = payload)
status_code = sym_response.status_code
sym_result = sym_response.json()

print("Welcome to Almdrasa currency converter")
user_answer = input("You need to show the country symbols? if yes enter (y), if you don't press (enter): ").lower()

if user_answer == "y":
    for symbol, country in sym_result["symbols"].items():
        print(f"{symbol} : {country}")
    print("x"*30)


from_currency = input("Enter currency you wont converting from: ").upper()
to_currency = input("Enter currency you wont converting to: ").upper()


while True:
    try:    
        amount = float(input("Enter the amount: "))
    except:
        print("The amount must be a numeric value!")
        continue
    
    if amount <= 0:
        print("The amount must be greater than 'zero'.!")
        continue
    else:
        break



url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={amount}"

payload = {}
headers= {
  "apikey": "AttXxZ1mKVs3oJqRWedfvy38rg81F8G9"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.json()

print(f"{amount} {from_currency} = {result['result']:.2f} {to_currency}")
