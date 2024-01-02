import json
import random

# Open the file and load the JSON data
with open("../dadjokes.list", "r") as f:
    jokes = json.load(f)

# Pick a random joke from the list
random_joke = random.choice(jokes)

# Print the joke
print(random_joke)