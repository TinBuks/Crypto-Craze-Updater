import os
import requests

api_key = os.getenv("MIMO_CRYPTO_CRAZE_API_KEY")
headers = {"api-key": api_key}

def get_crypto_price(coin_id):
  url = f"https://crypto-craze.mimo.dev/api/coins/{coin_id}"
  response = requests.get(url, headers=headers)
  data = response.json()
  return data

def print_crypto_price(crypto):
  symbol = crypto["symbol"]
  price_usd = crypto["priceUsd"]
  print(symbol)

  print(price_usd)

bitcoin = get_crypto_price("bitcoin")
ethereum = get_crypto_price("ethereum")
solana = get_crypto_price("solana")
print_crypto_price(bitcoin)
print_crypto_price(ethereum)
print_crypto_price(solana)
