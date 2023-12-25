import random  # for selecting a random quotes
import time  # for measuring how long it took
import json  # for being able to import an external JSON-formatted file for dynamic instead of static quotes DB.


# load the external JSON-formatted quotes DB.
def load_quotes_from_json(json_file):
    with open(json_file, 'r') as file:
        quote_list = json.load(file)
    return quote_list


# defines a function to create an underscored version of a quote
def create_underscored_quote(quote):
    # initialize a variable to hold the underscored quote. It's initially empty.
    underscored_quote = ''
    # loop over each word in the quote.
    for word in quote:
        # the creation of a string made out of underscores (_) that's the same length as the word.
        underscored_word = '_' * len(word)
        # adding a dash (-) before the underscores to separate words.
        if underscored_quote:
            underscored_quote += '-' + underscored_word
        else:
            # for the first word, just set it to the underscores.
            underscored_quote = underscored_word
    # return the complete underscored quote wrapped in a list.
    return [underscored_quote]


# define a function to update the underscored quote based on the guessed letter.
def update_underscored_quote(quote, underscored_quote, guess):
    # initialize a variable to hold the new underscored quote.
    new_underscored_quote = ''
    # split the underscored quote into words on dashes (-).
    underscored_words = underscored_quote.split('-')
    # loop over the indices of the words in the quote.
    for i in range(len(quote)):
        # get the current word and its underscored version.
        word = quote[i]
        underscored_word = underscored_words[i]
        # build the new word with guessed letters revealed
        new_word = ''
        # loop over the characters in the word
        for j in range(len(word)):
            # get the character and the corresponding underscored character.
            char = word[j]
            underscored_char = underscored_word[j]
            # add the guessed character to the word
            new_word += char if char == guess else underscored_char
        # adds the word to the underscored quote
        if new_underscored_quote:
            new_underscored_quote += '-' + new_word
        else:
            new_underscored_quote = new_word
    # return the "new" underscored quote.
    return new_underscored_quote


# start the game
def game(guess_the_quotes):
    # choose a random quote from the JSON
    selected_quote = random.choice(guess_the_quotes)
    # underscore the quote
    underscored_quote = create_underscored_quote(selected_quote)[0]
    # print the underscored quote
    print("Guess the quote:", underscored_quote)

    # start the timer and counting score
    score = 0
    start_time = time.time()

    # keep asking for guesses until no more left
    while '_' in underscored_quote:
        # ask for letters.
        guess = input("Enter a letter: ").lower()
        # check if the letter exists
        if any(guess in word for word in selected_quote):
            # fill up the guessed letter
            underscored_quote = update_underscored_quote(selected_quote, underscored_quote, guess)
            # add points for correct guess
            score += 5
        else:
            # take points for incorrect guess
            score -= 1

        # print the quote after each guess
        print("quote:", underscored_quote)

    # calculate the time it took to get the correct answer
    total_time = time.time() - start_time
    # add 100 points if it took less than 30 seconds to finish
    if total_time <= 30:
        score += 100

    # check the score and print a corresponding message
    if score > 150:
        print(f"Amazing work! Your final score is {score}. No one ever scored so high before!")
    elif 100 <= score <= 150:
        print(f"Good job! Your final score is {score}. Your score is considered very high!")
    elif 50 <= score < 100:
        print(f"Nice job! Your final score is {score}. But im sure you can do better..")
    else:
        print(f"You found the answer! Your final score is {score}. We suggest you keep practicing to improve it.")

    # print the final result with the time it took
    print(f"It took you {total_time:.0f} seconds to find the correct answer.")


# load the quotes and start the game
quotes = load_quotes_from_json('quotes.json')
game(quotes)