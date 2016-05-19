#!/usr/bin/env python3

import curses
import time
import random

result = ""
solution = ""
rock_x = ""
rock = ""

def main(screen):
    curses.noecho()             # read keystrokes instantly, without waiting for enter to ne pressed
    curses.curs_set(0)          # set cursor visibility to invisible

    screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    screen.keypad(1)            # enable processing of functional keys by curses
    screen.nodelay(1)

    def generate_rock():    #function for generating rocks
        global result
        global solution
        global rock_x
        rock_x = random.randint(1, curses.COLS - 4) + 1
        solution = ""
        num_1 = int(random.randint(0, 9))
        num_2 = int(random.randint(1, 9))
        operators = ["+", "-", "*", "/"]
        rock_operator = str(random.choice(operators))
        if rock_operator == "+":
            result = num_1 + num_2
        if rock_operator == "-":
            result = num_1 - num_2
        if rock_operator == "*":
            result = num_1 * num_2
        if rock_operator == "/":
            result = num_1 // num_2
        return (str(num_1) + str(rock_operator) + str(num_2))

    global rock
    rock = str(generate_rock())
    key = 0
    rock_y = 1

    while key != 27:    #function runs until esc is pressed
        key = ""
        global solution
        screen.clear()
        screen.border(0)
        screen.addstr(0, curses.COLS // 2 - 9, "Castle Rock Popper")
        screen.addstr(rock_y, rock_x, rock)
        screen.addstr(curses.LINES - 1, 5, "Solution: " + str(solution))
        screen.refresh()
        time.sleep(0.3)
        rock_y = rock_y + 1
        keystroke = screen.getch()

        if keystroke == 45:    #sense "-"
            solution = solution + "-"

        if keystroke in [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]:    #sense numbers of solutions
            solution = solution + str(keystroke - 48)

        if keystroke in [263, 10, 27]:    #sense space or esc  ohh JewRy pls ... 10 is the ascii code for enter
            key = keystroke               #263 is the ascii code for backspace - enables to erase solution line

        if rock_y == int(curses.LINES - 1):     #new rock if reached bottom
            rock = str(generate_rock())
            rock_y = 1

        if key == 10:               #space is pressed (how to change to enter?--> change it to 10)
            if solution is not '':
                if int(solution) == result:
                    #here comes what happens if you enter the right solution
                    bravo = "Grat"
                    screen.addstr(curses.LINES // 2, curses.COLS // 2 - len(bravo), bravo)
                    screen.refresh()
                    time.sleep(2)
                    rock = str(generate_rock())
                    rock_y = 1
                else:
                    wrong_result = "Wrong solution"
                    screen.addstr(curses.LINES // 2, curses.COLS // 2 - len(wrong_result), wrong_result)
                    screen.refresh()
                    time.sleep(2)
                    #life--
            else:
                warning = "Type in a solution"
                screen.addstr(curses.LINES // 2, curses.COLS // 2 - len(warning), warning)
                screen.refresh()
                time.sleep(2)

        if key == 263:
            solution = ""
            screen.addstr(curses.LINES - 1, 5, "Solution: " + str(solution))
            screen.refresh()

        if key == 27: break         #quit if esc is pressed


curses.wrapper(main)
