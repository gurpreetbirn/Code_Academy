sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
print(sensors)

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

animals_in_zoo = {"zebras": 8, "monkeys": 12, "dinosaurs": 0}

print(animals_in_zoo)

# Add multiple keys
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone",
                 "Animated Feature": "Zootopia", "Supporting Actress": "Viola Davis"}
print(oscar_winners)
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

# new task

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print()
print(drinks_to_caffeine)

# Review

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song: playcount for song, playcount in zip(songs, playcounts)}

print(plays)

plays.update({"Purple Haze": 1})
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)






