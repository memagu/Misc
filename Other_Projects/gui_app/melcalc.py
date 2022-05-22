import tkinter as tk

# init
root = tk.Tk()
root.title("melcalc")
root.geometry("400x500")
root.resizable(False, False)
FONT = "Monoton 32"
BG = "#1d1d1d"
FG = "#4d4d4d"
pad_amt = 2
root.config(bg=BG)

frame_display = tk.Frame(root, bg=BG, padx=pad_amt, pady=pad_amt)
frame_display.pack(side=tk.TOP)
frame_buttons = tk.Frame(root, bg=BG, padx=pad_amt, pady=pad_amt)
frame_buttons.pack(side=tk.TOP)
frame_buttons.grid_columnconfigure("all", uniform="column")

display = tk.Entry(frame_display, width=16, border=False, font=FONT, bg=BG, fg=FG, highlightcolor=FG, highlightbackground=FG, highlightthickness=2, justify=tk.CENTER, insertontime=0)
display.pack(padx=1, pady=10)


def enter_item(item):
    text = display.get()
    text += item
    display.insert(tk.END, item)


def delete_item():
    text = display.get()
    text = text[:-1]
    clear_display()
    display.insert(0, text)


def clear_display():
    display.delete(0, tk.END)


def evaluate():
    text = str(eval(display.get()))
    clear_display()
    display.insert(0, text)


def button(text, pos):
    btn = tk.Button(frame_buttons, font=FONT, border=False, bg=BG, fg=FG, text=text, command=lambda: enter_item(text), activebackground=FG, activeforeground=BG)
    btn.grid(column=pos[0], row=pos[1])
    return btn


button_clear = tk.Button(frame_buttons, font=FONT, border=False, bg=BG, fg=FG, text="C", command=lambda: clear_display(), activebackground=FG, activeforeground=BG)
button_clear.grid(column=0, row=0)
button("(", [1, 0])
button(")", [2, 0])
button("1", [0, 1])
button("2", [1, 1])
button("3", [2, 1])
button("4", [0, 2])
button("5", [1, 2])
button("6", [2, 2])
button("7", [0, 3])
button("8", [1, 3])
button("9", [2, 3])
button("0", [0, 4])
button("/", [3, 0])
button("*", [3, 1])
button("+", [3, 2])
button("-", [3, 3])
button_del = tk.Button(frame_buttons, font=FONT, border=False, bg=BG, fg=FG, text="DEL", command=lambda: delete_item(), activebackground=FG, activeforeground=BG)
button_del.grid(column=1, row=4)
button_enter = tk.Button(frame_buttons, font=FONT, border=False, bg=BG, fg=FG, text="ENTER", command=lambda: evaluate(), activebackground=FG, activeforeground=BG)
button_enter.grid(column=2, row=4, columnspan=2)

root.mainloop()


