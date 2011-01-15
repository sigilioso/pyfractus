# -*- coding: utf-8 -*-

def color(pixel, indexes=(0,1,2), increment=90):
	for i in indexes:
		if pixel[i] != 0: pixel[i] = pixel[i] + increment \
			if pixel[i] + increment < 255 else 255
	return pixel

def simple_color(pixel, color='blue'):

	

def color_pixels(p, maxIt):
	"""
	Defines the color of a pixel depending on the distance from the point p to the set
	"""
	def to_byte(e):
		return 0 if e == maxIt else 255 * e / maxIt
	pixel = map(to_byte, [p, p, p])
	if pixel[2] != 0: pixel[2] = pixel[2] + 90 if pixel[2] + 90 < 255 else 255
	return tuple(pixel)


