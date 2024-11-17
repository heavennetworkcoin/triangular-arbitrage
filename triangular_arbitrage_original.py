#!/usr/bin/env python3

from binance.client import Client
import time

# Initialize the Binance Testnet client
api_key = "UBKIYGJhEKWB5I4gJGqknEyOh9V3XKjp0mxd0RVxJlQU60k8I9GjkuZeJJxj4HO7"
api_secret = "x4LeXf1mfB34zlXYWyzPSO9DiRN1H0qp0l5DzXzG109ykdGaQXH3g5ArKfHwvsGC"

client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'

# Define trading pairs
pair_1 = 'BTCUSDT'
pair_2 = 'ETHBTC'
pair_3 = 'ETHUSDT'

# Set a minimum profit threshold
MIN_PROFIT_THRESHOLD = 1.001  # 0.1% profit after fees

# Function to fetch the latest prices
def get_prices():
    try:
        price_1 = float(client.get_ticker(symbol=pair_1)['askPrice'])
        price_2 = float(client.get_ticker(symbol=pair_2)['askPrice'])
        price_3 = float(client.get_ticker(symbol=pair_3)['bidPrice'])  # Use bid price for sell
        return price_1, price_2, price_3
    except Exception as e:
        print(f"Error fetching prices: {e}")
        return None, None, None

# Function to calculate potential profit
def calculate_profit(price_1, price_2, price_3):
    # Simulate the buy-buy-sell sequence
    starting_usdt = 100  # Example starting capital in USDT
    btc_amount = starting_usdt / price_1
    eth_amount = btc_amount * price_2
    final_usdt = eth_amount * price_3
    return final_usdt / starting_usdt

# Main loop
while True:
    price_1, price_2, price_3 = get_prices()
    if price_1 and price_2 and price_3:
        profit_ratio = calculate_profit(price_1, price_2, price_3)
        print(f"Profit ratio: {profit_ratio:.4f}")

        if profit_ratio > MIN_PROFIT_THRESHOLD:
            print("Arbitrage opportunity detected!")
            print(f"Start trading: {pair_1}, {pair_2}, {pair_3}")

            # Simulate placing orders (replace these with real trading logic)
            try:
                order_1 = client.create_order(
                    symbol=pair_1,
                    side='BUY',
                    type='MARKET',
                    quantity=0.001  # Replace with calculated quantity
                )
                print(f"Order 1 executed: {order_1}")

                order_2 = client.create_order(
                    symbol=pair_2,
                    side='BUY',
                    type='MARKET',
                    quantity=0.001  # Replace with calculated quantity
                )
                print(f"Order 2 executed: {order_2}")

                order_3 = client.create_order(
                    symbol=pair_3,
                    side='SELL',
                    type='MARKET',
                    quantity=0.001  # Replace with calculated quantity
                )
                print(f"Order 3 executed: {order_3}")

            except Exception as e:
                print(f"Error executing trade: {e}")
    else:
        print("Failed to fetch prices. Retrying...")

    # Sleep for a short time before checking again
    time.sleep(5)
