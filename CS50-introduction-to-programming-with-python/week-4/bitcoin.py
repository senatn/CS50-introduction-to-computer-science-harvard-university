import requests
import sys

def main():
    btc_price = 0
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    else:
        btc_price = price_request()

    amount = btc_price * float(sys.argv[1])
    print(f"${amount:,.4f}")


def price_request():
    while True:
        try:
            price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
            return float(price['bpi']['USD']['rate_float'])
        except requests.RequestException:
            pass


if __name__ == "__main__":
    main()