import random

def get_random_joke():
    # Get a random topic
    topic = random.choice(["animals", "food", "people", "places", "things"])

    # Get a random noun
    noun = random.choice(["cat", "dog", "apple", "banana", "house"])

    # Get a random verb
    verb = random.choice(["eats", "drinks", "sleeps", "walks", "talks"])

    # Get a random adjective
    adjective = random.choice(["big", "small", "fat", "thin", "happy"])

    # Build the joke
    joke = f"What do you call a {adjective} {noun} that {verb}s {topic}?"

    return joke

print(get_random_joke())


