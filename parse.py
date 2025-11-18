import json
import os
import re


MEAT_TERMS = {
    "beef", "chicken", "fish", "pork", "mutton", "lamb",
    "turkey", "duck", "veal", "ham", "bacon", "sausage",
    "shrimp", "crab", "lobster", "clam", "oyster", "salmon"
}

def is_vegetarian(desc):
    """Return True if no meat terms found in description."""
    desc_lower = desc.lower()
    return not any(re.search(r"\b" + re.escape(meat) + r"\b", desc_lower) for meat in MEAT_TERMS)

def parse_menu_file(filepath):
    """Parse one JSON menu file for one day."""
    day = os.path.splitext(os.path.basename(filepath))[0].replace("menus_", "")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    parsed_items = []

    for meal_name, meal_data in data.items():
        if not isinstance(meal_data, dict):
            continue
        menu_items = meal_data.get("menuItems", [])
       
        for item in menu_items:
            if not isinstance(item, dict):
                continue
            name = item.get("name", "").strip()
            description = item.get("description", "").strip()
           
            if not name or not description:
                continue
            category = "vegetarian" if is_vegetarian(description) else "non-vegetarian"
            parsed_items.append({
                "day": day,
                "meal": meal_name,
                "name": name,
                "description": description,
                "start_date": item.get("startDate") or item.get("start_date"),
                "end_date": item.get("endDate") or item.get("end_date"),
                "category": category
            })

    return parsed_items

def parse_all_menu_files(folder_path):
    """Parse all menu JSON files in the folder and combine parsed results."""
    all_parsed = []
    for filename in os.listdir(folder_path):
        if filename.startswith("menus_") and filename.endswith(".json"):
            filepath = os.path.join(folder_path, filename)
            day_parsed = parse_menu_file(filepath)
            all_parsed.extend(day_parsed)
    return all_parsed

if __name__ == "__main__":
    
    menu_folder = r"C:\Users\adusu\Hypertrophy\HypertrophyApp"
    parsed_menus = parse_all_menu_files(menu_folder)

   
    print(json.dumps(parsed_menus, indent=2, ensure_ascii=False))







