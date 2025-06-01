import curses
import random

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    sh, sw = stdscr.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(True)
    win.timeout(100)

    # Snake & food
    snk_x = sw//4
    snk_y = sh//2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x-2]
    ]
    food = [random.randint(1, sh-2), random.randint(1, sw-2)]
    win.addch(food[0], food[1], curses.ACS_PI)

    