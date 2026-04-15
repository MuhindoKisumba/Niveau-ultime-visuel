import requests

ABUSEIPDB_KEY = "YOUR_API_KEY"

def check_ip(ip):
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}"
    headers = {
        "Key": ABUSEIPDB_KEY,
        "Accept": "application/json"
    }
    r = requests.get(url, headers=headers)
    return r.json()

# TEST
print(check_ip("8.8.8.8"))
