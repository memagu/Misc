import mouseN
import keyboard
import time

clicker = False

while True:
    if keyboard.is_pressed("c"):
        clicker = not clicker
        time.sleep(0.2)

    if clicker:
        mouse.click()




