import curses


def main(stdscr):
    # Set up the screen
    stdscr.clear()
    stdscr.refresh()

    # Create a window
    window = curses.newwin(curses.LINES - 1, curses.COLS - 1, 0, 0)

    # Main loop
    while True:
        # Get user input
        user_input = window.getstr()

        # Process user input
        if user_input == b'quit':
            break

        # Display output
        window.addstr(f"You entered: {user_input.decode()}\n")
        window.refresh()


# Initialize curses
curses.wrapper(main)
