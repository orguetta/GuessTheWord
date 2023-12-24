import json
import random
import time

def load_phrases_from_json(json_file):
    with open(json_file, 'r') as file:
        phrases = json.load(file)
    return phrases

# Other functions and the main game function remain unchanged

# Updated main game function to use phrases loaded from JSON
def play_game(phrases):
    # Randomly choose a phrase from the list of phrases.
    selected_phrase = random.choice(phrases)
    # Create the underscore version of the phrase.
    underscore_phrase = create_underscore_phrase(selected_phrase)[0]
    # Print the initial underscore phrase for the player.
    print("Guess the phrase:", underscore_phrase)

    # Initialize the player's score and record the start time.
    score = 0
    start_time = time.time()

    # Keep asking for guesses as long as there are underscores (unrevealed letters).
    while '_' in underscore_phrase:
        # Ask the player to enter a letter guess.
        guess = input("Enter a letter: ").lower()
        # Check if the guessed letter is in any word of the phrase.
        if any(guess in word for word in selected_phrase):
            # Update the underscore phrase with the guessed letter.
            underscore_phrase = update_underscore_phrase(selected_phrase, underscore_phrase, guess)
            # Increase the score for a correct guess.
            score += 5
        else:
            # Decrease the score for an incorrect guess.
            score -= 1

        # Print the updated underscore phrase after each guess.
        print("Phrase:", underscore_phrase)

    # Calculate the total time taken for the game.
    total_time = time.time() - start_time
    # Add a bonus to the score if the player finishes within 30 seconds.
    if total_time <= 30:
        score += 100

    # Print the final results: the time taken and the final score.
    print(f"Congratulations! You completed the phrase in {total_time:.0f} seconds.")
    print(f"Your final score is: {score}")

# Load phrases from the JSON file
phrases = load_phrases_from_json('phrases.json')

# Start the game by calling the play_game function with the list of phrases.
play_game(phrases)
