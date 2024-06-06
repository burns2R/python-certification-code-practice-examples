import requests

url = "https://www.amazon.com/testing"
# correct!!! its the good ol' try-except Python programming 
# exception handling
try:
    r = requests.get(url, timeout=1)
    r.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("HTTP Error")
    print(errh.args[0])

print(r)