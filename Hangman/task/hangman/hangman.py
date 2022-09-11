import random

list_of_words = ("python", "java", "swift", "javascript")
lower_case_list = "abcdefghijklmnopqrstuvwxyz"
wins_count = 0
lost_count = 0


def menu(wins, lost):
    print("H A N G M A N  # 8  attempts")  # output of attempts number'
    user_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if user_input == "play":
        main_program()
    elif user_input == "results":
        print(f"You won: {wins} times")
        print(f"You lost: {lost} times")
        menu(wins, lost)
    elif user_input == "exit":
        exit()


def main_program():
    global wins_count
    global lost_count
    entered_letters = []
    tries = 8
    secret_word = random.choice(list_of_words)
    number_of_letters = len(secret_word)  # the length of secret word
    dash = ['-' for _ in range(number_of_letters)]  # number of letters in word = number of "-"
    while tries > 0:
        print("".join(dash))
        letter = input("Input a letter: ")
        if len(letter) != 1 or letter == " ":
            print("Please, input a single letter.\n")
        elif letter not in lower_case_list:
            print("Please, enter a lowercase letter from the English alphabet.\n")
# searching of letters in secret word and replacement "-"
        elif letter in entered_letters:
            print("You've already guessed this letter.\n")
        elif letter in secret_word:
            print()
            for index, value in enumerate(secret_word):
                if value == letter:
                    dash[index] = letter
                    number_of_letters -= 1
                if "-" not in dash:
                    wins_count += 1
                    win_message(secret_word, wins_count, lost_count)
        else:
            print("That letter doesn't appear in the word.")
            tries -= 1
            print(f"# {tries} attempts\n ")
        entered_letters.append(letter)
    print("You lost!")
    lost_count += 1
    menu(wins_count, lost_count)


def win_message(secret, wins, lost):
    print(f"You guessed the word {secret}!")
    print("You survived!")
    menu(wins, lost)


if __name__ == '__main__':
    menu(0, 0)
