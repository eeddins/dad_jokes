import json
import random

# Open the file and load the JSON data
with open("dadjokes.list", "r") as f:
    jokes = json.load(f)

# Pick a random joke from the list
random_joke = f"{random.choice(jokes)}\n\n - Jokes of the Day (https://jokesoftheday.net/jokes-feed/)"

# Save the joke to a file
with open("jod.txt", "w") as f:
    f.write(random_joke)