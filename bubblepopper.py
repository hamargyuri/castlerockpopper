#!/usr/bin/env python3

import curses
import time
import random
from curses import KEY_ENTER, KEY_RIGHT

def main(screen):
    curses.noecho()
    curses.curs_set(0)

    screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    screen.keypad(1)
    screen.nodelay(1)
    key = KEY_RIGHT
    z = 1
    rock = str(random.randint(0, 9))

    while key != 27:
        keystroke = screen.getch()
        if keystroke in [KEY_ENTER, 27]:
            key = keystroke
        if z == int(curses.LINES - 1):
            rock = str(random.randint(0, 9))
            z = 1

        screen.clear()
        screen.border(0)
        screen.addstr(0, curses.COLS // 2 - 9, "Castle Rock Popper")
        screen.addstr(z, curses.COLS // 2, rock)
        screen.refresh()
        time.sleep(0.05)
        z = z + 1

        if key == 27: break


curses.wrapper(main)
