# check_google_status.py

import requests

def check_google_status():
    url = "https://www.google.com"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("✅ Google is UP.")
        else:
            print(f"⚠️ Google is reachable but returned status code: {response.status_code}")
    except requests.ConnectionError:
        print("❌ Google is DOWN - Connection Error.")
    except requests.Timeout:
        print("❌ Google is DOWN - Timeout Error.")
    except requests.RequestException as e:
        print(f"❌ Google is DOWN - Other Error: {e}")

if __name__ == "__main__":
    check_google_status()
