import requests

# Define the URL and parameters
url = "https://widget.api.eagle.bigzpoon.com/menuitems"

params = {
    "categoryId": "61bd80d68b34640010e194b8",
    "locationId": "61df4a34d5507a00103ee41e",
    "menuGroupId": "61bd808b5f2f930010bb6a7a",
    "userPreferences": '{"allergies":[],"lifestyleChoices":[],"medicalGoals":[],"preferenceApplyStatus":false}'
}

# Browser-like headers (these help avoid internal API errors or CORS issues)
headers = {
    "device-id": "f85c2536-0638-41d7-8ab7-d78905e4779e", #Vainavi Computer Session
    "location-id": "61df4a34d5507a00103ee41e", #Pavillion Menu
    "x-comp-id":"61bd7ecd8c760e0011ac0fac", #Grab menuitems

}

# Make the GET request
response = requests.get(url, params=params, headers=headers)

# Print the response status and data
print("HTTP Status Code:", response.status_code)
try:
    data = response.json()
    print("API Response Code:", data.get("code"))
    print("Message:", data.get("message"))
    print("\nFull Response:\n", data)
except ValueError:
    print(response.text)