# Hänga gubbe. Slumpmässiga ord på engelska.

HANGMAN_DRAWINGS = ("""
       ____
      |    |
      |    o
      |   /|\\
      |    |
      |   / \\
   ___|___
  (       )
 (         )
(           )

GAME OVER""", """
       ____
      |    |
      |    o
      |   /|\\
      |    |
      |   / 
   ___|___
  (       )
 (         )
(           )""", """
       ____
      |    |
      |    o
      |   /|\\
      |    |
      |
   ___|___
  (       )
 (         )
(           )""", """
        ____
      |    |
      |    o
      |   /|
      |    |
      |
   ___|___
  (       )
 (         )
(           )""", """
       ____
      |    |
      |    o
      |    |
      |    |
      |
   ___|___
  (       )
 (         )
(           )""", """
       ____
      |    |
      |    o
      |
      |
      |
   ___|___
  (       )
 (         )
(           )""", """
       ____
      |    |
      |
      |
      |
      |
   ___|___
  (       )
 (         )
(           )""", """
      |
      |
      |
      |
      |
   ___|___
  (       )
 (         )
(           )""", """





   _______
  (       )
 (         )
(           )""")

print("Hangman. Random words in english.")

# addWords = input("Do you want to add words to the vocabulary")

with open("english.txt", 'r') as f:
    word = {line.strip() for line in f.readlines()}.pop()

print(word)

lives = 8
used_letters = "" # bank
win = False
guessed = "_" * len(word)

# EgnaOrd = input("Vill du köra med egna ord? ")
#
# if EgnaOrd == "ja":
#     läggTill = input("Lägg till ett ord i din egen lista: ")
#     word = random.get(EgenLista)
#
#
# elif EgnaOrd == "nej":

while lives > -1 and not win:
    # print(guessed)
    print(f"{HANGMAN_DRAWINGS[lives]} - {guessed}")
    print(" Letters so far: ", used_letters, "\n" * 5)

    if lives == 0:
        break

    guess = input("Guess a letter: ")
    if guess not in word:
        if guess in used_letters:
            print("\n", "You already guessed this letter.")
            continue

        lives -= 1
        used_letters += guess + " "
        print("\n", "Wrong,", guess, " is not in the word.", "\n")
        continue

    if guess in guessed:
        print("\n", "You already guessed this letter.")
        continue

    for i, char in enumerate(word):
        if guess == char:
            if guessed[i] == "_":
                guessed = guessed[:i] + guess + guessed[i + 1:]

    used_letters += guess + " "

    if guessed == word:
        win = True
        print(f"Congratulations, you won!")


print(f"The word was > {word} <")

input("\n\nDone! Press enter to exit.")
