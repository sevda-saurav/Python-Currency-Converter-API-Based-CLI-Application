from requests import get
from config import API_KEY, BASE_URL

def get_rates(base_currency="USD"):
    params = {
        "apikey" : API_KEY,
        "base_currency" : base_currency
    }

    response = get(BASE_URL, params=params)
    data = response.json()

    return data["data"]

def convert_currency(amount, from_currency, to_currency):
    rates = get_rates(from_currency)

    if to_currency not in rates:
        return "Currency not available"
    
    rate = rates[to_currency]

    result = amount * rate

    return result