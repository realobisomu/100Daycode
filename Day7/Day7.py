import random

from click import clear
import hangman_art
import hangman_words


print(hangman_art.logo)


chosen_word = random.choice(hangman_words.word_list)

lives = 6

print(f'The solution is {chosen_word}')

display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += '_'


end_of_game = False
while not end_of_game:

    guess = input('Enter a letter: ').lower()
    clear()

    if guess in display:
        print(f'{guess} is already guessed')

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(
            f'\nYou guessed {guess}, that is not in the word - it will cost you a live\n')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('\nYou Lose\n')

    print(f" {' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print('\nYou win\n')
    print(hangman_art.stages[lives])
