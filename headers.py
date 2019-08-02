import requests
url = "https://icanhazdadjoke.com/search"
user_input = input("What do you want a joke about? ")

#response = requests.get(url, headers={"Accept":"text/plain"}) #it sends plain text, if API is available
response = requests.get(
    url, 
    headers={"Accept":"application/json"},
    params={"term":user_input}
    ) 

#print (response.text)
data = response.json()
#print(type(data))
#print(data["joke"])
print(data["results"])
