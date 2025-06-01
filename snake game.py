import curses
import random

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    sh, sw = stdscr.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(True)
    win.timeout(100)

    