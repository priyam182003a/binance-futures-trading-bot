import os
from binance.client import Client
from dotenv import load_dotenv
import logging
import questionary

# Load .env
load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

# Logging setup
logging.basicConfig(
    filename="futures_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logging.info(f"Market Order Response: {order}")
            print(f"✅ Market Order Placed: {order}")
        except Exception as e:
            logging.error(f"Market Order Error: {e}")
            print(f"[DRY RUN] Would place MARKET {side} for {symbol} qty {quantity}")

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )
            logging.info(f"Limit Order Response: {order}")
            print(f"✅ Limit Order Placed: {order}")
        except Exception as e:
            logging.error(f"Limit Order Error: {e}")
            print(f"[DRY RUN] Would place LIMIT {side} for {symbol} qty {quantity} at price {price}")

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                timeInForce="GTC",
                quantity=quantity,
                price=price,
                stopPrice=stop_price
            )
            logging.info(f"Stop-Limit Order Response: {order}")
            print(f"✅ Stop-Limit Order Placed: {order}")
        except Exception as e:
            logging.error(f"Stop-Limit Order Error: {e}")
            print(f"[DRY RUN] Would place STOP-LIMIT {side} for {symbol} qty {quantity} at limit price {price} with stop price {stop_price}")

if __name__ == "__main__":
    print("🚀 Binance Futures Testnet Bot (with Questionary CLI) 🚀")
    bot = BasicBot(api_key, api_secret)

    symbol = questionary.text(
        "Enter trading pair (e.g., BTCUSDT):"
    ).ask().upper()

    order_type = questionary.select(
        "Select order type:",
        choices=["market", "limit", "stop-limit"]
    ).ask()

    side = questionary.select(
        "Select side:",
        choices=["BUY", "SELL"]
    ).ask()

    quantity = float(questionary.text(
        "Enter quantity:"
    ).ask())

    if order_type == "market":
        bot.place_market_order(symbol, side, quantity)
    elif order_type == "limit":
        price = questionary.text("Enter limit price:").ask()
        bot.place_limit_order(symbol, side, quantity, price)
    elif order_type == "stop-limit":
        price = questionary.text("Enter limit price:").ask()
        stop_price = questionary.text("Enter stop price:").ask()
        bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)
    else:
        print("❌ Invalid order type.")

