import requests

class MenuChecker:
    def __init__(self):
        self.url = "https://widget.api.eagle.bigzpoon.com/menuitems"

        self.params = {
            "categoryId": "61bd80d68b34640010e194b8",
            "locationId": "61df4a34d5507a00103ee41e",
            "menuGroupId": "61bd808b5f2f930010bb6a7a",
            "userPreferences": '{"allergies":[],"lifestyleChoices":[],"medicalGoals":[],"preferenceApplyStatus":false}'
        }

        # Start session and set persistent headers
        self.session = requests.Session()
        self.session.headers.update({
         "device-id": "f85c2536-0638-41d7-8ab7-d78905e4779e",
            "location-id": "61df4a34d5507a00103ee41e",
            "x-comp-id": "61bd7ecd8c760e0011ac0fac",
        })

    def fetch_menu(self):
        response = self.session.get(self.url, params=self.params)
        data = response.json()
        return data


menucheck = MenuChecker()

print(menucheck.fetch_menu())