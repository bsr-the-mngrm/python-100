import requests

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

