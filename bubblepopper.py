#!/usr/bin/env python3

import curses
import time
import random
from curses import KEY_ENTER, KEY_RIGHT

def main(scr):
    curses.noecho()
    curses.curs_set(0)

    screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    screen.border(0)
    screen.keypad(1)
    screen.nodelay(1)
    key = KEY_RIGHT

    while key != 27:
        rock = str(random.randint(0, 9))
        keystroke = screen.getch()
        if keystroke in [KEY_ENTER, 27]:
            key = keystroke

        for z in range (curses.LINES - 1):
            screen.clear()
            screen.addstr(0, curses.COLS // 2 - 9, "Castle Rock Popper")
            screen.addstr(z + 1, curses.COLS // 2, rock)
            screen.refresh()
            time.sleep(0.05)


curses.wrapper(main)
