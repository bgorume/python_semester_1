import requests, sys


if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    num = float(sys.argv[1])
except ValueError:
    print("Command-line argument must be a number")
    sys.exit(1)

try:
    response = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=3cdfaba69c30a1ade2126b1c670a52717392975e972692f40345818c6e04c121')
    data = response.json()

    rate = float(data['data']['priceUsd'])
    amount = num * rate
    print(f'${amount:,.4f}')

except requests.RequestException:
    print("Error processing your request. Goodbye!")
    sys.exit(1)