words = []
used = []

with open("words_alpha.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        words.append(line.strip())

print("Initiation complete!")
print()

while True:
    hint = input("Input hint: ")
    for word in words:
        if hint in word and hint not in used:
            used.append(word)
            print(f"Unused word containing {hint} = {word}")
            break
    print()
