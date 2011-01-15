# -*- coding: utf-8 -*-

def color(pixel, colour='blue', increment=90):
	indexes = dict(red=(0,), green=(1,), blue=(2,), gray=(0,1,2))
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


