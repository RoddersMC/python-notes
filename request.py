from requests import get

response = get('https://catfact.ninja/fact')
print(response.text)