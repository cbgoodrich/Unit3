#Charlie Goodrich
#10/05/17
#dotsDemo.py - making some dots

from ggame import *

red = Color(0xFF0000, 1)

dot = CircleAsset(20, LineStyle(1, red), red)

for j in range(13): #prints the row 13 times
    for i in range(25): #prints one row of dots
        Sprite(dot, (20 + 40*i, 20 + 40*j))

App().run()
