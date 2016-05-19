#!/usr/bin/env python3

import curses
import time
import random
from curses import KEY_ENTER

def main(screen):
    curses.noecho()
    curses.curs_set(0)

    screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    screen.keypad(1)
    screen.nodelay(1)
    key = 0
    rock_y = 1
    rock = str(random.randint(0, 9))

    while key != 27:
        keystroke = screen.getch()
        if keystroke in [KEY_ENTER, 27]:
            key = keystroke
        if rock_y == int(curses.LINES - 1):
            rock = str(random.randint(0, 9))
            rock_y = 1

        screen.clear()
        screen.border(0)
        screen.addstr(0, curses.COLS // 2 - 9, "Castle Rock Popper")
        screen.addstr(z, curses.COLS // 2, rock)
        screen.refresh()
        time.sleep(0.05)
        rock_y = rock_y + 1

        if key == 27: break


curses.wrapper(main)
