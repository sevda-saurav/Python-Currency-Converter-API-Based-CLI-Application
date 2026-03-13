from converter import convert_currency

def main():
    print("Currency Converter")
    print("------------------")

    amount = float(input("Enter Amount: "))
    from_currency = input("From currency (USD, INR, EUR): ").upper()
    to_currency = input("To currency (USD, INR, EUR): ").upper()

    res = convert_currency(amount , from_currency, to_currency)

    print(f"\nConverted Amount: {res:.2f} {to_currency}")

if __name__ == "__main__":
    main()