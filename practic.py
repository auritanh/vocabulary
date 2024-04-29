import requests 

api_key = 'c654b433-0fe0-46df-ad29-d0901c937a8d'
word = 'voluminous'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'

r = requests.get(final_url)

result = r.json()
 
print(result)