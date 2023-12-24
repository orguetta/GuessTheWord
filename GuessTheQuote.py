# Import the necessary modules from Python's standard library.
import random  # For random operations like selecting a random phrase.
import time    # For time-related operations, like measuring how long the game takes.

# Define a function to create an underscore version of a phrase.
def create_underscore_phrase(phrase):
    # Initialize a variable to hold the underscore phrase. It's initially empty.
    underscore_phrase = ''
    # Loop over each word in the phrase.
    for word in phrase:
        # For each word, create a string of underscores (_) that's the same length as the word.
        underscore_word = '_' * len(word)
        # If it's not the first word, add a dash (-) before the underscores to separate words.
        if underscore_phrase:
            underscore_phrase += '-' + underscore_word
        else:
            # For the first word, just set it to the underscores.
            underscore_phrase = underscore_word
    # Return the complete underscore phrase wrapped in a list.
    return [underscore_phrase]

# Define a function to update the underscore phrase based on the guessed letter.
def update_underscore_phrase(phrase, underscore_phrase, guess):
    # Initialize a variable to hold the new underscore phrase.
    new_underscore_phrase = ''
    # Split the underscore phrase into words on dashes (-).
    underscore_words = underscore_phrase.split('-')
    # Loop over the indices of the words in the phrase.
    for i in range(len(phrase)):
        # Get the current word and its underscore version.
        word = phrase[i]
        underscore_word = underscore_words[i]
        # Initialize a variable to build the new word with guessed letters revealed.
        new_word = ''
        # Loop over the characters in the word.
        for j in range(len(word)):
            # Get the current character and the corresponding underscore character.
            char = word[j]
            underscore_char = underscore_word[j]
            # If the character matches the guess, add it to the new word. Otherwise, add the underscore.
            new_word += char if char == guess else underscore_char
        # Add the new word to the new underscore phrase, separated by dashes.
        if new_underscore_phrase:
            new_underscore_phrase += '-' + new_word
        else:
            new_underscore_phrase = new_word
    # Return the updated underscore phrase.
    return new_underscore_phrase

# Define the main game function.
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

# List of phrases to be used in the game.
phrases = [
    ['speak', 'as', 'if'],
    ['act', 'without', 'expectation'],
    ['all', 'is', 'well'],
    ['allow', 'for', 'delays'],
    ['always', 'be', 'honest'],
    ['never', 'see', 'yourself'],
    ['sometimes', 'deliver', 'quality'],
    ['ask', 'powerful', 'questions'],
    ['audit', 'your', 'metrics'],
    ['own', 'their', 'mistakes']
]

# Start the game by calling the play_game function with the list of phrases.
play_game(phrases)
