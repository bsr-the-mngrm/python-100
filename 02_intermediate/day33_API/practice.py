import requests

MY_LAT = 47.192087
MY_LNG = 20.188501

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

# Bad practice:
# if response.status_code == 404:
#     raise Exception("Not found content!")
# elif response.status_code != 200:
#     raise Exception("Bad response from ISS API")

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split("T")[1].split("+")[0]
sunset = data['results']['sunset'].split("T")[1].split("+")[0]

print(data)
print(sunrise[:5])
print(sunset[:5])
