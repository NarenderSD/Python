import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return None

    exchange_rate = data["rates"].get(target_currency)
    if exchange_rate is None:
        return None

    return exchange_rate

def convert_currency(amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate is None:
        return None

    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    print("=== Currency Converter ===")
    amount = float(input("Enter the amount to convert: "))
    base_currency = input("Enter the base currency code (e.g., USD): ").upper()
    target_currency = input("Enter the target currency code (e.g., EUR): ").upper()

    converted_amount = convert_currency(amount, base_currency, target_currency)
    if converted_amount is None:
        print("Unable to perform currency conversion. Please check the currency codes.")
    else:
        print(f"Converted amount: {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()
