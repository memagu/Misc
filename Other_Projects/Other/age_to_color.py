import os


dob = input("Enter date of birth (YYYY/MM/DD): ")
year = int(dob[:4])
month = int(dob[4:6])
day = int(dob[6:])

r = year % 256
g = month * int(255 / 12)
b = day * int(255 / 31)

os.system(f"start chrome https://www.google.com/search?q=rgb({r}%2C+{g}%2C+{b})")
