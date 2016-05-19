#!/usr/bin/env python3

import curses
import time
import random
from curses import KEY_ENTER
from curses import textpad

def main(screen):
    curses.noecho()             # read keystrokes instantly, without waiting for enter to ne pressed
    curses.curs_set(0)          # set cursor visibility to invisible
    curses.cbreak()             # enable keypad mode

    screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    screen.keypad(1)            # enable processing of functional keys by curses
    screen.nodelay(1)
    key = 0
    rock_y = 1
    rock = str(random.randint(0, 9))

    while key != 27:
        new_text()
        keystroke = screen.getch()
        if keystroke in [KEY_ENTER, 27]:
            key = keystroke
        if rock_y == int(curses.LINES - 1):
            rock = str(random.randint(0, 9))
            rock_y = 1

        screen.clear()
        screen.border(0)
        screen.addstr(0, curses.COLS // 2 - 9, "Castle Rock Popper")
        screen.addstr(rock_y, curses.COLS // 2, rock)
        screen.refresh()
        time.sleep(0.05)
        rock_y = rock_y + 1

        if key == 27: break


curses.wrapper(main)
