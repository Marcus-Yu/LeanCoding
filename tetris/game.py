import curses

def initcolors():
  curses.start_color()
  curses.use_default_colors()

  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, -1)

def tetriminos(stdscr):
  curses.curs_set(0)

  x = 0
  y = 0

  # square
  stdscr.addstr(y+1,x+1,chr(9609),curses.color_pair(4))
  stdscr.addstr(x+1,x+3,chr(9609),curses.color_pair(4))
  stdscr.addstr(x+2,x+1,chr(9609),curses.color_pair(4))
  stdscr.addstr(x+2,x+3,chr(9609),curses.color_pair(4))

  # line
  stdscr.addstr(y+1,x+9,chr(9609),curses.color_pair(5))
  stdscr.addstr(y+2,x+9,chr(9609),curses.color_pair(5))
  stdscr.addstr(y+3,x+9,chr(9609),curses.color_pair(5))
  stdscr.addstr(y+4,x+9,chr(9609),curses.color_pair(5))

  # t shape
  stdscr.addstr(y+1,x+15,chr(9609),curses.color_pair(6))
  stdscr.addstr(y+2,x+15,chr(9609),curses.color_pair(6))
  stdscr.addstr(y+2,x+13,chr(9609),curses.color_pair(6))
  stdscr.addstr(y+2,x+17,chr(9609),curses.color_pair(6))

  # l shape
  stdscr.addstr(y+2,x+23,chr(9609),curses.color_pair(7))
  stdscr.addstr(y+2,x+25,chr(9609),curses.color_pair(7))
  stdscr.addstr(y+2,x+27,chr(9609),curses.color_pair(7))
  stdscr.addstr(y+1,x+27,chr(9609),curses.color_pair(7))

  # l reverse shape
  stdscr.addstr(y+1,x+33,chr(9609),curses.color_pair(10))
  stdscr.addstr(y+2,x+33,chr(9609),curses.color_pair(10))
  stdscr.addstr(y+2,x+35,chr(9609),curses.color_pair(10))
  stdscr.addstr(y+2,x+37,chr(9609),curses.color_pair(10))

  # z shape
  stdscr.addstr(y+2,x+43,chr(9609),curses.color_pair(11))
  stdscr.addstr(y+2,x+45,chr(9609),curses.color_pair(11))
  stdscr.addstr(y+1,x+45,chr(9609),curses.color_pair(11))
  stdscr.addstr(y+1,x+47,chr(9609),curses.color_pair(11))

  # z reverse shape
  stdscr.addstr(y+1,x+53,chr(9609),curses.color_pair(12))
  stdscr.addstr(y+1,x+55,chr(9609),curses.color_pair(12))
  stdscr.addstr(y+2,x+55,chr(9609),curses.color_pair(12))
  stdscr.addstr(y+2,x+57,chr(9609),curses.color_pair(12))

  stdscr.nodelay(0)
  key = stdscr.getch()

def tetris(stdscr):
  initcolors()
  tetriminos(stdscr)
curses.wrapper(tetris)