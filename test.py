# -*- coding: utf-8 -*-

from fractals import Fractals
import colors
import png

# Test File

width = 800
height = 600
maxIt = 150

fractals = Fractals(num_procs=2)

elems = fractals.mandelbrot(-2.5-1.5j, 1.5+1.5j, width, height, maxIt)
img = []
for row in elems:
	rowImg = ()
	for p in row:
		rowImg += colors.color_pixels(p, maxIt, 'red')
	img.append(rowImg)

f = open('mandel.png', 'wb')
w = png.Writer(width, height)
w.write(f,img)
f.close()
