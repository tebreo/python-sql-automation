import random

# A small movie database
movies = {
    "action": ["Mad Max: Fury Road", "John Wick", "Die Hard"],
    "comedy": ["Superbad", "The Grand Budapest Hotel", "Step Brothers"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
    "sci-fi": ["Inception", "The Matrix", "Interstellar"],
    "horror": ["Get Out", "A Quiet Place", "The Conjuring"]
}

# Show available genres
print("Available genres:")
for genre in movies:
    print(f"- {genre}")

# Get user input
choice = input("Pick a genre: ").lower()

# Recommend a movie
if choice in movies:
    recommendation = random.choice(movies[choice])
    print(f"You should watch: {recommendation}")
else:
    print("Sorry, that genre isn't in the list.")

