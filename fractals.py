# -.- coding: utf-8 -.-

#
# fractals.py: some functios to draw fractals representations
#
# Author: Christian Felipe Álvarez <sigilioso@gmail.com>
#

def in_mandelbrot(c=complex(0.7,1.5), maxIt=100):
	"""
	Determine if a complex number c is in the Mandelbrot set for a maximum
	number of iterations.
	Return max_it if c is in the Mandelbrot set, and returns the number of
	iterations needed to discover that c is not in the Mandelbrot set otherwise.
	"""
	z = complex(0, 0)
	for i in range(0, maxIt):
		if abs(z) > 4:
			return i
		else:
			z = z**2 + c
	return maxIt


def in_julia(z=complex(0,0), c=complex(0.742,0.1), exp=2, maxIt=100):
	"""
	Determine if a complex number z is in the Julia J(c) set for a maximum number
	of iterations. J(c) --> z' = z^exp + c
	Returns max_it if c is in this Julia set, and returns the number of
	iterations needed to discover that c is not in J(c) set otherwise.
	"""
	for i in range(0, maxIt):
		if abs(z**2) > 4:
			return i
		else:
			z = z**exp + c
	return maxIt

def increment(length, minimun, maximun):
	"""
	Returns the dinstance between maximun and minimun
	"""
	return (maximun - minimun) / length

def mandelbrot(minimun, maximun, width, height, maxIt):
	"""
	Get a table representation of a Mandelbrot set whose size is
	width x height.
	minimun and maximun are, respectively, the minimun and maximun complex
	numbers that are represented (minimun in the bottom-left and maximun in
	the top-right)
	"""
	incReal = increment(width, minimun.real, maximun.real)
	incImag = increment(height, minimun.imag, maximun.imag)

	ch = minimun.imag
	cw = minimun.real

	imag = []

	for w in range(height):
		row = []
		for h in range(width):
			row.append(in_mandelbrot(complex(cw,ch),maxIt))
			cw += incReal
		imag.append(row)
		ch += incImag
		cw = minimun.real
	return imag

def julia(c, exp, minimun, maximun, width, height, maxIt):
	"""
	Get a table representation of a Julia (J(c) for exp exponent) set
	whose size is width x height.
	minimun and maximun are, respectively, the minimun and maximun complex
	numbers that are represented (minimun in the bottom-left and maximun in
	the top-right)
	"""
	incReal = increment(width, minimun.real, maximun.real)
	incImag = increment(height, minimun.imag, maximun.imag)

	ch = minimun.imag
	cw = minimun.real

	imag = []

	for w in range(height):
		row = []
		for h in range(width):
			row.append(in_julia(complex(cw,ch), c, exp, maxIt))
			cw += incReal
		imag.append(row)
		ch += incImag
		cw = minimun.real
	return imag

