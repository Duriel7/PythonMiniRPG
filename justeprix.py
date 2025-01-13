import random

price = random.randint(0, 1000);

#debug log
print(price);

inc = 0;
guess = int(input("Guess price between 0 and 1000: "));
guessList = [];

while (guess != price):
    inc += 1;

    if guess in guessList:
        print("You already tried that one !");
    else:
        if guess < price:
            print("Higher !");
        else:
            print("Lower !");

    guessList.append(guess);

    guess = int(input("Wrong, guess again : "));

print("You guessed right in ", inc, " tries");

