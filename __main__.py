import nltk
# Edit distance gives us the Levenshtein distance
from nltk.metrics import edit_distance
from random import randint

def play_again():
    input("Press enter to play again.\n")

word_list = [
    "apple", "banana", "cherry", "date", "egg", "fish", "grape", "hat",
    "ice", "juice", "kite", "lemon", "moon", "note", "orange", "pear",
    "queen", "rose", "sun", "tree", "umbrella", "vase", "water", "xylophone",
    "yogurt", "zebra"
]

while True:
    word_to_guess = word_list[randint(0,len(word_list)-1)].lower()
    disguised = ""
    clue_count = 1
    for i in range(len(word_to_guess)):
        disguised += "*"
    print("Welcome to Tom's word guessing game!")
    print("type 'give up' to give up, type 'clue me' for a clue")
    print("I'm thinking of the word {} which has a length of {}\n".format(disguised, len(word_to_guess)))
    while True:
        answer = input("What do you think it is:").lower()
        if answer == word_to_guess:
            print("\nCongratulations, you were right! The answer was {}. Thank you for playing!".format(word_to_guess))
            play_again()
            break
        elif answer == "give up":
            print("Unlucky!, the answer was " + word_to_guess)
            play_again()
            break
        elif answer == "clue me":
            if clue_count == len(word_to_guess)-1:
                print("You've ran out of clues, and you've lost! The answer was " + word_to_guess)
                play_again()
                break
            else:
                print("Your clue is {}\n".format(word_to_guess[:clue_count]))
                clue_count += 1 
        else:
            diff = edit_distance(answer, word_to_guess)
            print("Incorrect! You were wrong by a Levenshtein Distance of {}\nTry again!\n".format(diff))


