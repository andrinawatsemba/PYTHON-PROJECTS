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

    # Initial direction
    key = curses.KEY_RIGHT

    while True:
        next_key = win.getch()
        key = key if next_key == -1 else next_key

        # Calculate new head
        y = snake[0][0]
        x = snake[0][1]
        if key == curses.KEY_DOWN:
            y += 1
        elif key == curses.KEY_UP:
            y -= 1
        elif key == curses.KEY_LEFT:
            x -= 1
        elif key == curses.KEY_RIGHT:
            x += 1

        new_head = [y, x]

        # Game over conditions
        if (
            y in [0, sh] or
            x in [0, sw] or
            new_head in snake
        ):
            msg = "Game Over! Press any key to exit."
            win.addstr(sh//2, sw//2 - len(msg)//2, msg)
            win.refresh()
            win.getch()
            break

        snake.insert(0, new_head)

        if new_head == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh-2),
                    random.randint(1, sw-2)
                ]
                food = nf if nf not in snake else None
            win.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        win.addch(snake[0][0], snake[0][1], '#')

if __name__ == "__main__":
    curses.wrapper(main)