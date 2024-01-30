import requests
import json
import win32com.client as wincom

speak=wincom.Dispatch("SAPI.SpVoice")

city=input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=72fa93925d1c453ab91164828231111&q={city}"

# url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r=requests.get(url)

# print(r.text)
wdic=json.loads(r.text)
print(f"Temperature : {wdic['current']['temp_c']} degree Celsius")
w=wdic['current']['temp_c']
text=f"The current weather in {city} is {w} degrees"
speak.Speak(text)
