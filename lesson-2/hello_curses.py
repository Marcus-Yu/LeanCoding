import curses

def window(stdscr):

  sh, sw = stdscr.getmaxyx()

  msg = "Hello Curses! Type ESC to exit!"
  stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg )
  
  stdscr.addstr(sh- 1, 0, str(ord('o')))
  stdscr.addstr(sh- 5, 0, chr(120))
  
  while True:
    userKey = stdscr.getch()
    stdscr.addstr(str(userKey))
    stdscr.addstr(chr(userKey))
    if userKey == 27:
      break
curses.wrapper(window)