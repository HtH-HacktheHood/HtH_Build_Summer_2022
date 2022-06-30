full_name = "Henry Bowe"
nickname = "Henny"
age = 25
has_used_python = True

hobbies = ["making music", "playing basketball", "playing video games", "watching anime", "watching sports", "hiking"]

fav_things = {
  "movie": "Undercover Brother",
  "food": "steak",
  "hobby": hobbies[0],
  "anime": "One Piece",
  "number": 13
}

print(f"Hello world! My name is {full_name}, but many of my friends call me {nickname}. I am {age} years old.")
print()
print(f"Has Python Experience: {has_used_python}")
print()

for key in fav_things.keys():
    print(f"My favorite {key} is {fav_things[key]}.")
  
print()
print(f"Here are some of my other hobbies: {hobbies}")
print()

all_vars = dict(vars())