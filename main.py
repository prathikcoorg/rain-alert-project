import requests
from twilio.rest import Client

API_KEY = "YOUR API"

MY_LAT = "YOUR_LAT"
MY_LONG = "YOUR LONG"
account_sid = "YOUR ACC SID"
auth_token = "YOUR AUTH"


parameters ={
    "lon":MY_LONG,
    "lat":MY_LAT,
    "appid":API_KEY,
    "cnt": 4,
}
weather = requests.get(" https://api.openweathermap.org/data/2.5/forecast?",params=parameters)
weather.raise_for_status()
weather_data = weather.json()
print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its going to rain today remember to bring an umbrella",
        from_="YOUR TWILIO PHONE NUMBER",
        to="YOUR PHONE NUMBER",
    )
    print(message.status)
