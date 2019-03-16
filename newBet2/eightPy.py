import sys,os
import curses

home = "home = "
away = "away = "
qtr = "qtr = "
ascore = "ascore = "
hscore = "hscore = "
uhscore = ""
uacscore = ""
uqtr = ""



def datPrint(var):
    file = open("sbdat.txt", "r")
    writer = file.read()
    out = writer[writer.find(var) + len(var):-(len(writer) - writer.find(";", writer.find(var)))]
    file.close()
    return out


def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # CLEAR SCREEN
    stdscr.clear()
    stdscr.refresh()

    # COLOR SETTINGS
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height = 8
        width = 40


        line1 = "{} {} {}".format(datPrint(away).center(10), "QTR".center(10), datPrint(home).center(10))
        line2 = "{} {} {}".format(datPrint(ascore).center(10), datPrint(qtr).center(10), datPrint(hscore).center(10))

        # OUTPUT
        top = ('*' * 32)[:width-1]
        namesQtr = "{}".format(line1)[:width-1]
        scoreQTR = "{}".format(line2)[:width-1]
        bottom = top
        statusbarstr = "PRESS ANY KEY TO UPDATE"[:width-1]

        # CENTER EVERYTHING
        start_x_top = int((width // 2) - (len(top) // 2) - len(top) % 2)
        start_x_namesQTR = int((width // 2) - (len(top) // 2) - len(top) % 2)
        start_x_scoreQTR = int((width // 2) - (len(top) // 2) - len(top) % 2)
        start_x_bottom = int((width // 2) - (len(top) // 2) - len(top) % 2)
        start_y = 1

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))


        # PRINT ALL OF THE TEXT
        stdscr.addstr(start_y, start_x_top, top)
        stdscr.addstr(start_y + 1, start_x_namesQTR, namesQtr)
        stdscr.addstr(start_y + 2, start_x_scoreQTR, scoreQTR)
        stdscr.addstr(start_y + 3, start_x_bottom, bottom)
        stdscr.move(cursor_y, cursor_x)

        # REFRESH
        stdscr.refresh()

        # WAIT
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
