#!/usr/bin/env python3

import curses
import time
import random

def main(scr):
    screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    rock = str(random.randint(0,9))

    for z in range (curses.LINES - 1):
        screen.clear()
        screen.addstr(0, curses.COLS // 2 - 9, "Castle Rock Popper")
        screen.addstr(z+1, curses.COLS // 2, rock)
        screen.refresh()
        time.sleep(0.1)

    screen.getkey()

curses.wrapper(main)
