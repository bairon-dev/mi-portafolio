import requests

def get_usd_rate():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url, timeout=5)
        data = response.json()
        return data["rates"]["MXN"]
    except:
        return 17.50

def convert_mxn_to_usd():
    rate = get_usd_rate()
    print(f"Current rate: 1 USD = {rate:.2f} MXN")
    mxn_amount = float(input("Enter amount in MXN pesos: $"))
    usd_amount = mxn_amount / rate
    print(f"\n${mxn_amount:.2f} MXN = ${usd_amount:.2f} USD")
    print(f"Rate source: Live API | Project 9/20 by Bairon")

if __name__ == "__main__":
    print("=== DOLLAR TRACKER 9/20 ===")
    convert_mxn_to_usd()

