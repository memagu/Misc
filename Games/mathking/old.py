import tkinter as tk
import random
from time import sleep

score = 0

root = tk.Tk()


def button():
    root.geometry("500x500")
    root.title("Multimath demo")

    while True:

        n1 = (random.randint(1, 12))
        n2 = (random.randint(1, 12))
        n3 = "*"
        answer = int(n1) * int(n2)
        label = tk.Label(root, text=n1, font=("Arial", 20))
        label.pack(padx=5, pady=5)
        label2 = tk.Label(root, text=n3, font=("Arial", 20))
        label2.pack(padx=5, pady=5)
        label3 = tk.Label(root, text=n2, font=("Arial", 20))
        label3.pack(padx=5, pady=5)
        sleep(1)
        entry = tk.Entry(root)
        entry.pack()

        def on_click():
            text = entry.get()
            entry.delete(0, tk.END)
            if int(text) == int(answer):
                label.configure(text="Correct answer!!")
                label2.configure(text="")
                label3.configure(text="")
                sleep(1)

            else:
                label.configure(text="You Lost!")
                label2.configure(text="")
                label3.configure(text="")
                sleep(1)
                quit()

        submit_button = tk.Button(root, text="Submit", font=("Arial", 10), command=on_click)
        submit_button.pack(padx=10, pady=20, ipady=20)
        while True:

            root.mainloop()


button()