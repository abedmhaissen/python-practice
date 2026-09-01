import random


def play(low=1, high=100):
    secret = random.randint(low, high)
    tries = 0
    print(f"Guess the number between {low} and {high}.")
    while True:
        raw = input("Your guess: ").strip()
        if not raw.isdigit():
            print("Enter a whole number.")
            continue
        guess = int(raw)
        tries += 1
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct in {tries} tries.")
            return


if __name__ == "__main__":
    play()
