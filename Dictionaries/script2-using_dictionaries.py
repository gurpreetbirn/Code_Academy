zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"],
                   "earth": ["Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

key_to_check = "energy"

if key_to_check in zodiac_elements:
    print(zodiac_elements["energy"])

zodiac_elements.update({"energy": "Not a Zodiac element"})

# T2 - Safely Get a Key

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931,
            "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

# T3 - Delete a Key
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25,
                   "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
print(health_points)

health_points += available_items.pop("power stew", 0)
print(health_points)

health_points += available_items.pop("mystic bread", 0)
print(health_points)
print(available_items)

# T4 - Get All Keys
print("\nT4 - Get All Keys")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931,
            "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18,
                 "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)

# T5 - Get All Values
print("\nT5 - Get All Values")

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18,
                 "dictionaries": 18}
total_exercises = 0

for exercises in num_exercises.values():
    total_exercises += exercises
print(total_exercises)

# T6 - Get All Items
print("\nT6 - Get All Items")

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37,
                           "Aerospace Engineer": 9}

for key, value in pct_women_in_occupation.items():
    print("Women make up", str(value), "percent of", key)

# T7 - Get All Items
print("\nT7 - Review")
tarot = {1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant",
         6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice",
         12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star",
         18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

spread = {}

spread["past"] = (tarot.pop(13))
spread["present"] = (tarot.pop(22))
spread["future"] = (tarot.pop(10))

for key, value in spread.items():
    print("Your", str(key), "is the", value, "card.")
