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

    rock = str(random.randint(0, 9))
    key = 0
    rock_y = 1

    while key != 27:
        key = 0
        screen.clear()
        screen.border(0)
        screen.addstr(0, curses.COLS // 2 - 9, "Castle Rock Popper")
        screen.addstr(rock_y, curses.COLS // 2, rock)
        screen.refresh()
        time.sleep(0.05)
        rock_y = rock_y + 1
        keystroke = screen.getch()

        if keystroke in [32, 27]:
            key = keystroke

        if rock_y == int(curses.LINES - 1):     #new rock if reached bottom
            rock = str(random.randint(0, 9))
            rock_y = 1

        if key == 32:               #space is pressed (how to change to enter?)
            rock = str(random.randint(0, 9))
            rock_y = 1

        if key == 27: break         #quit if esc is pressed


curses.wrapper(main)
