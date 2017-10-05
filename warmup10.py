#Charlie Goodrich
#10/04/17
#warmup10.py - making wallpaper

from ggame import *

black = Color(0x000000, 1)
red = Color(0xFF0000, 1)
yellow = Color(0xFFFF00, 1)

blackRect = RectangleAsset(200, 100, LineStyle(1, black), black)
redRect = RectangleAsset(200, 67, LineStyle(1, red), red)
yellowRect = RectangleAsset(200, 33, LineStyle(1, yellow), yellow)

for j in range(10):
    for i in range(10):
        Sprite(blackRect, (0 + 233*i, 0 + 133*j))
        Sprite(redRect, (0 + 233*i, 33 + 133*j))
        Sprite(yellowRect, (0 + 233*i, 67 + 133*j))

App().run()