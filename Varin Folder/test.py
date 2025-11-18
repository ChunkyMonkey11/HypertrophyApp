import requests
import json
from datetime import datetime, timedelta

class MenuChecker:
    def __init__(self):
        self.url = "https://widget.api.eagle.bigzpoon.com/menuitems"
        self.location_id = "61df4a34d5507a00103ee41e"
        self.menu_group_id = "61bd808b5f2f930010bb6a7a"

        self.categories = {
            "breakfast": "61bd80d05f2f930010bb6a81",
            "lunch": "61bd80d68b34640010e194b8",
            "dinner": "61bd80b08b34640010e194b4"
        }

        self.user_preferences = '{"allergies":[],"lifestyleChoices":[],"medicalGoals":[],"preferenceApplyStatus":false}'

        self.session = requests.Session()
        self.session.headers.update({
            "device-id": "f85c2536-0638-41d7-8ab7-d78905e4779e",
            "location-id": self.location_id,
            "x-comp-id": "61bd7ecd8c760e0011ac0fac",
        })

    def fetch_menu_for_category(self, category_name, category_id, date_str):
        params = {
            "categoryId": category_id,
            "isPreview": "false",
            "locationId": self.location_id,
            "menuGroupId": self.menu_group_id,
            "userPreferences": self.user_preferences,
            "date": date_str   # <-- new date parameter
        }
        try:
            response = self.session.get(self.url, params=params)
            response.raise_for_status()
            data = response.json()
            if data.get("code") == 200:
                print(f" {date_str}: Fetched {category_name} menu")
                return data.get("data", {})
            else:
                print(f" {date_str}: API error for {category_name}: {data.get('message', 'No message')}")
        except requests.RequestException as e:
            print(f" {date_str}: Request error for {category_name}: {e}")
        except ValueError:
            print(f" {date_str}: Response parsing error for {category_name}")
        return None

    def fetch_menus_for_date(self, date_str):
        daily_menus = {}
        for category_name, category_id in self.categories.items():
            menu_data = self.fetch_menu_for_category(category_name, category_id, date_str)
            if menu_data:
                daily_menus[category_name] = menu_data

        # Save daily menus to JSON file
        filename = f"menus_{date_str}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(daily_menus, f, ensure_ascii=False, indent=2)
        print(f" Menus for {date_str} saved to {filename}")

        return daily_menus

    def fetch_menus_for_next_days(self, num_days=7):
        all_days = {}
        for i in range(num_days):
            date_str = (datetime.today() + timedelta(days=i)).strftime("%Y-%m-%d")
            print(f"\n Fetching menus for {date_str}...")
            all_days[date_str] = self.fetch_menus_for_date(date_str)
        print(" Finished fetching all menus")
        return all_days


if __name__ == "__main__":
    menucheck = MenuChecker()
    menus = menucheck.fetch_menus_for_next_days(7)

