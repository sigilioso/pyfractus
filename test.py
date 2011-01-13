# -*- coding: utf-8 -*-

import fractals
import png

# Test File

def color_pixel(it, maxIt):
	"""
	Defines the color of a pixel depending on the distance to the set
	"""
	if it == maxIt:
		return 0
	else:
		return 255 * it / maxIt

width = 800
height = 600

elems = fractals.mandelbrot(-2.5-1.5j, 1.5+1.5j, width, height, 250)
img = []
for row in elems:
	rowImg = ()
	for elem in row:
		rowImg += (color_pixel(elem,250), 
				color_pixel(elem,250), 
				color_pixel(elem,250))
	img.append(rowImg)

f = open('mandel.png', 'wb')
w = png.Writer(width, height)
w.write(f,img)
f.close()
