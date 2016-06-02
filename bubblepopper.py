#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import time
import random
import sys
from curses import KEY_BACKSPACE

result = ""  # result of the equation stored here
solution = ""  # solution entered by the player
rock_x = ""  # x coordinate of rocks
rock = ""  # the appearing rock of equation
rock_y = ""  # y coordinate of rocks
lives = 5       # number of lives
score = 0    # number of good solutions


def main(screen):
    screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    screen.nodelay(1)
    screen.keypad(1)
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    screen.bkgd(' ', curses.color_pair(1))

    def generate_rock():  # function for generating rocks of equations
        global result
        global solution
        global rock_x
        global rock_y
        rock_x = random.randint(1, curses.COLS - 25)
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
        rock = str(num_1) + str(rock_operator) + str(num_2)
        rock_bordered = ['◭◮▲◭◮', "▌%s ▌" % (rock), '⧩⧨▽⧩⧨', '◮◭△◮◭', "▐%s▐" % (rock), '⧨⧩▼⧨⧩']
        return rock_bordered

    def blast():
        screen.addstr(rock_y, rock_x + 1, "○◌○")
        screen.refresh()
        time.sleep(0.1)
        screen.addstr(rock_y, rock_x + 1, "◎○◎")
        screen.refresh()
        time.sleep(0.1)
        screen.addstr(rock_y, rock_x + 1, "◌◎◌")
        screen.refresh()
        time.sleep(0.1)

    def main_graphics():
        screen.border(0)
        title = "Equation Popper beta"
        screen.addstr(0, (curses.COLS - len(title)) // 2, title, curses.A_BOLD)
        screen.addstr(6, curses.COLS - 20, "Solution: " + str(solution), curses.A_BOLD)
        lives_count()
        player_score()

    def lives_count():
        screen.addstr(2, curses.COLS - 20, "♥ " * lives, curses.color_pair(2))

    def player_score():
        global score
        screen.addstr(4, curses.COLS - 20, "Your score: " + str(score), curses.A_BOLD)
        score = int(score)

    def game():
        keystroke = ""
        global score
        score = 0
        global lives
        lives = 5
        rock = generate_rock()
        while keystroke != 27:  # the followings run in a loop until esc (27) is pressed
            # initial settings
            global solution
            global rock_x
            global rock_y
            keystroke = ""
            screen.clear()  # clear screen before generating next position of rock
            main_graphics()
            # rock spawn and movement
            for i, j in enumerate(rock):
                if rock_y % 2 == 0:
                    if i < 3:
                        screen.addstr(rock_y + i, rock_x, j)
                else:
                    if i > 2:
                        screen.addstr(rock_y + i - 3, rock_x, j)
            screen.refresh()
            time.sleep(0.2)
            rock_y += 1
            # reactions to specified keystrokes (in ASCII)
            keystroke = screen.getch()

            if keystroke == 45:  # sense "-" entered for negative numbers
                solution = solution + "-"

            if keystroke in [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]:  # sense numbers entered for solution
                solution = solution + str(keystroke - 48)

            if rock_y == int(curses.LINES - 3):  # generate new rock if reached bottom
                rock = generate_rock()
                rock_y = 1
                lives = lives - 1
                screen.clear()
                main_graphics()

            if keystroke == 10:  # what happens if enter (10) is pressed
                if len(solution) > 0:  # so it won't crash when "solution" is empty
                    if int(solution) == result:
                        # here comes what happens if you entered the correct solution
                        for _ in range(3):
                            blast()
                        score += 1
                        screen.clear()
                        main_graphics()
                        time.sleep(0.2)
                        rock = generate_rock()
                    else:
                        lives -= 1
                        screen.clear()
                        main_graphics()
                    solution = ""

            if lives == 0:
                game_over(score)

            if keystroke == 263:  # backspace deletes whatever's enetered as solution
                solution = ""

            if keystroke == 27:
                exit()  # quit if esc (27) is pressed

    def welcome_screen():
        screen.clear()
        keystroke = ""
        with open('welcome.txt', 'r') as welcome:
            welcome_msg = welcome.readlines()
            for i, j in enumerate(welcome_msg):
                screen.addstr(1 + i, (curses.COLS - len(j)) // 2, j)
        screen.refresh()
        while keystroke != 10:
            keystroke = screen.getch()
            if keystroke == 27:
                exit()
        game()

    def game_over(score):
        screen.clear()
        keystroke = ""
        with open('game_over.txt', 'r') as gameover:
            game_over_msg = gameover.readlines()
            final_score = "Your score: %d" % (score)
            for i, j in enumerate(game_over_msg):
                screen.addstr(curses.LINES // 2 - 4 + i, (curses.COLS - len(j)) // 2, j)
        screen.addstr(curses.LINES // 2, (curses.COLS - len(final_score)) // 2, final_score, curses.A_BOLD)
        screen.refresh()
        while keystroke != 10:
            keystroke = screen.getch()
            if keystroke == 27:
                exit()
        welcome_screen()

    welcome_screen()

curses.wrapper(main)
