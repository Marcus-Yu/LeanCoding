import math
import random

field = []
center=[5,5]
size = [4, 4]
r, c = 0, 0
   # nested loop
for y in range(center[0] - size[0] // 2, center[0] + size[0] // 2):
        # go through each row.
        print([[0, 0, 0]] * size[1])
        field.append([[0, 0, 0]] * size[1])
        for x in range(center[1] - size[1], center[1] + size[1], 2):
            # go through each column of a row
            field[r][c] = [y, x, 0]
            print(str(r)+':'+str(c))
            print(field )
            #stdscr.addstr(y, x, chr(9608))
            c = c + 1
        r = r + 1
        c = 0
print(math.prod(size) // 7)
  # generate the bombs!
i = 0 # track the bomb count.


