import curses
from curses.textpad import Textbox, rectangle
import time

curses.COLOR_CYAN



def main(stdscr):
    h, w = stdscr.getmaxyx()
    x, y = 0, 0
    # x = w // 2 - len(text) // 2
    # y = h // 2
    # stdscr.nodelay(True)
    # curses.curs_set(0)
    #
    # while True:
    #     try:
    #         key = stdscr.getkey()
    #     except:
    #         key = None
    #     if key == "KEY_LEFT":
    #         x -= 1
    #     if key == "KEY_RIGHT":
    #         x += 1
    #     if key == "KEY_UP":
    #         y -= 1
    #     if key == "KEY_DOWN":
    #         y += 1
    #
    #     stdscr.clear()
    #     stdscr.addstr(y, x, "0")
    #     stdscr.refresh()




curses.wrapper(main)


