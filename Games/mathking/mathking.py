import tkinter as tk
import random

root = tk.Tk()
root.geometry("500x500")
root.title("Multimath demo")

label_score = tk.Label(root, font=("Arial", 20))
label_score.grid(column=1, row=0, sticky=tk.EW)

label_left = tk.Label(root, font=("Arial", 20))
label_left.grid(column=0, row=1, sticky=tk.EW)

label_mid = tk.Label(root, font=("Arial", 20))
label_mid.grid(column=1, row=1, sticky=tk.EW)

label_right = tk.Label(root, font=("Arial", 20))
label_right.grid(column=2, row=1, sticky=tk.EW)

entry = tk.Entry(root, justify=tk.CENTER)
entry.grid(column=1, row=2)

button = tk.Button(root, font=("Arial", 10))
button.grid(column=1, row=3)

root.columnconfigure(tk.ALL, weight=1)
root.rowconfigure(tk.ALL, weight=1)

score = 0
answer = 0


def generate_question() -> tuple[str, str, str, float]:
    num1 = random.randint(1, 11)
    num2 = random.randint(1, 11)
    operator = random.choice("+-*/")
    answer = eval(f"{num1}{operator}{num2}")
    return str(num1), str(num2), operator, answer


def submit():
    global score

    if not round(answer - float(entry.get().strip()), 2):
        score += 1
        play()
        return

    title_screen()


def play():
    global answer

    num1, num2, operator, _answer = generate_question()
    answer = _answer
    label_score.config(text=f"Your score: {score}")
    label_left.config(text=num1)
    label_mid.config(text=operator)
    label_right.config(text=num2)
    entry.delete(0, tk.END)
    button.config(text="submit", command=submit)


def title_screen():
    global score

    label_score.config(text=f"Your score: {score}")
    label_left.config(text="!")
    label_mid.config(text="Ma7h K1ng")
    label_right.config(text="!")
    entry.delete(0, tk.END)
    button.config(text="Play!", command=play)

    score = 0


if __name__ == '__main__':
    title_screen()
    root.mainloop()
