import tkinter as tk


def clicked():
    label.configure(text=entry.get())


def reset():
    entry.delete(0, "end")


window = tk.Tk()
window.title("appster")
window.geometry("600x500")

entry = tk.Entry(window, width=10)
entry.grid(column=2, row=0)

button = tk.Button(window, text="button", command=clicked, )
button.grid(column=1, row=0)

button2 = tk.Button(window, text="reset", command=reset)
button2.grid(column=3, row=0)

entry = tk.Entry(window, width=10)
entry.grid(column=2, row=0)

window.mainloop()


