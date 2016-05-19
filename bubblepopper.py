#!/usr/bin/env python3

import curses
import time
import random

result = ""    #result of the equation stored here
solution = ""    #solution entered by the player
rock_x = ""    #x coordinate of rocks
rock = ""    #the appearing rock of equation
rock_y = ""    #y coordinate of rocks

def main(screen):
    curses.curs_set(0)          # set cursor visibility to invisible
    screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    screen.nodelay(1)

    def generate_rock():    #function for generating rocks of equations
        global result
        global solution
        global rock_x
        global rock_y
        rock_x = random.randint(1, curses.COLS - 4)
        rock_y = 1
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

    def blast():
        screen.addstr(rock_y - 1, rock_x, "○◌○ ")
        screen.refresh()
        time.sleep(0.1)
        screen.addstr(rock_y - 1, rock_x, "◎○◎ ")
        screen.refresh()
        time.sleep(0.1)
        screen.addstr(rock_y - 1, rock_x, "◌◎◌ ")
        screen.refresh()
        time.sleep(0.1)

    global rock
    rock = str(generate_rock())
    key = ""    #this gets evaluated for enter or esc or backspace

    while key != 27:    #the followings run in a loop until esc (27) is pressed
        def main_graphics():
            screen.border(0)
            screen.addstr(0, curses.COLS // 2 - 9, "Castle Rock Popper")
            screen.addstr(curses.LINES - 1, 5, "Solution: " + str(solution))
        #initial settings
        global solution
        global rock_x
        global rock_y
        key = ""
        screen.clear()    #clear screen before generating next position of rock
        main_graphics()
        #rock spawn and movement
        screen.addstr(rock_y, rock_x, rock)
        screen.refresh()
        time.sleep(0.3)
        rock_y = rock_y + 1
        #reactions to specified keystrokes (in ASCII)
        keystroke = screen.getch()
        if keystroke == 45:    #sense "-" entered for negative numbers
            solution = solution + "-"

        if keystroke in [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]:    #sense numbers entered for solution
            solution = solution + str(keystroke - 48)

        if keystroke in [10, 27, 127]:    #sense enter or esc or backspace
            key = keystroke

        if rock_y == int(curses.LINES - 1):     #generate new rock if reached bottom
            rock = str(generate_rock())
            rock_y = 1

        if key == 10:               #what happens if enter (10) is pressed
            if len(solution) > 0:   #so it won't crash when "solution" is empty
                if int(solution) == result:
                #here comes what happens if you entered the correct solution
                    for _ in range(3):
                        blast()
                    screen.clear()
                    main_graphics()
                    time.sleep(0.2)
                    rock = str(generate_rock())
                solution = ""

        if key == 127:    #backspace deletes whatever's enetered as solution
            solution = ""

        if key == 27: break         #quit if esc (27) is pressed


curses.wrapper(main)
