# -*- coding: utf-8 -*-

#
# Author: Christian Felipe Álvarez <sigilioso@gmail.com>
#

def color(pixel, colour='blue', increment=90):
	"""
	Defines the color of a pixel depending on the distance from the point 
	to the set. The procedure to color the pixel is de following:
	The pixel correspondig to points in the set are painted black (value is 0),
	but if the the pixel is not in the set its colors is darker when its further
	from the set.
	colour: red, green, blue or gray.
	increment: the amount of the colour selected to increase to when seting the
	colour.
	"""
	indexes = dict(red=(0,), green=(1,), blue=(2,), gray=(0,1,2), brown=(0,1), 
			violet=(0,2), yellow=(1,2))
	for i in indexes[colour]:
		if pixel[i] != 0: pixel[i] = pixel[i] + increment \
			if pixel[i] + increment < 255 else 255
	return pixel

def color_pixels(p, maxIt, colour='blue'):
	"""
	Defines the color of a pixel depending on the distance from the point p to the set
	"""
	def to_byte(e):
		return 0 if e == maxIt else 255 * e / maxIt
	pixel = map(to_byte, [p, p, p])
	return tuple(color(pixel, colour))


