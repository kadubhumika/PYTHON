import requests

print("Please check out my LinkedIn Profile:")
url = "https://www.linkedin.com/in/bhumika786/"
response = requests.get(url)

print(response.text)  # This prints the HTML content of the page
