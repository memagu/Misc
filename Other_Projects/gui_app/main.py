import tkinter as tk

# init
root = tk.Tk()
root.title("melcalc")
root.geometry("400x500")
root.resizable(False, False)
FONT = "Corbel 40"
BG = "#1d1d1d"
FG = "#3d3d3d"
root.config(bg=BG)

entry = tk.Entry(root, width=14, font=FONT, border=False, bg=FG, fg=BG, insertontime=0, justify="center")
entry.grid(column=0, row=0)
entry.place(x=0, y=0, width=400)
entry.pack(padx=1, pady=10)




root.mainloop()


