import curses

def window(stdscr):

  block=chr(9608)+chr(9608)+chr(9608)+chr(9608)
  
  curses.start_color()
  curses.use_default_colors()
  
  for i in range(0, curses.COLORS):
    curses.init_pair(i +1, i, -1)
    #stdscr.addstr("<{0}>".format(i + 1), curses.color_pair(i + 1))
  
  for x in range(1,17):
    for y in range(1,17):
      colornumber=(x-1)*16+y
      #print(colornumber)
      #stdscr.addstr(x,y,block,curses.color_pair(colornumber))
      #print((x-1)*5+1)
      #print((y-1)*5)
      #stdscr.getch()
      stdscr.addstr(int((x-1)*3),y*4,block,curses.color_pair(colornumber))
      stdscr.addstr((x-1)*3+2,y*4,str(colornumber)+"  ", curses.color_pair(colornumber))
      #stdscr.addstr(0,0, "RED ALERT!", curses.color_pair(1))
     
  
#(y-1)*5
  stdscr.getch()

curses.wrapper(window)