import requests
r = requests.get("https://api.github.com/users/bhumika")
print(r.text)