import time
import keyboard
import mouse

while True:
    if keyboard.is_pressed("0"):
        print(mouse.get_position())
        time.sleep(0.2)