import time
import yfinance as yf
from status_hub_hardware import green_alert, red_alert, idle_state

# -----------------------------
# CONFIG
# -----------------------------
CHECK_INTERVAL = 60  # seconds

STOCKS = {
    "NVDA": {
        "low": 180,
        "high": 190
    },
    "PLTR": {
        "low": 160,
        "high": 180
    }
}

# -----------------------------
# FUNCTIONS
# -----------------------------
def get_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d", interval="1m")

    if data.empty:
        return None

    return float(data["Close"].iloc[-1])


# -----------------------------
# MAIN LOOP
# -----------------------------
print("Stock Tracker Starting...")
idle_state()

while True:
    try:
        for symbol, levels in STOCKS.items():
            price = get_price(symbol)

            if price is None:
                print(f"{symbol}: Price unavailable")
                continue

            print(f"{symbol}: ${price:.2f}")

            if price >= levels["high"]:
                print(f"{symbol} ABOVE threshold → GREEN alert")
                green_alert()

            elif price <= levels["low"]:
                print(f"{symbol} BELOW threshold → RED alert")
                red_alert()

            else:
                print(f"{symbol} within normal range")
                idle_state()

        time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("Stopping Stock Tracker")
        idle_state()
        break

    except Exception as e:
        print(f"Error: {e}")
        idle_state()
        time.sleep(30)
