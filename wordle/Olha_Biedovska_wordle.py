import random


def get_random_word():
    with open("Olha_Biedovska_words.txt", "r") as f:
        lines = f.readlines()
    words = [l.strip() for l in lines]
    word = random.choice(words)
    return word


if __name__ == "__main__":
    # word = "кобза"
    word = get_random_word()
    # print(word)

    n_tries = 6
    for n_try in range(n_tries):
        guess = input("Make guess: ")
        guess = guess.strip()

        if len(guess) != len(word):
            print("Guess len is not eqaul to word len, try one more time")
            continue

        if guess == word:
            print("Victory")
            break

        hint = ""
        for idx in range(len(guess)):
            if guess[idx] == word[idx]:
                hint += "X"
            elif guess[idx] in word:
                hint += "x"
            else:
                hint += " "
        print(guess)
        print(hint)
    else:
        print(f"Tries are over :( the word was: {word}")

