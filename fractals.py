# -.- coding utf-8 -.-

import threading

#
# fractals.py: Fractals, Class to manage fractals representations
#
# Author: Christian Felipe Álvarez <sigilioso@gmail.com>
#

class Fractals:
	"""
	A Class to manage fractals representations
	"""
	
	def __init__(self, numThreads=1):
		"""
		Create a new instance of Fractals specifiying optionally the number of
		threads that are going to be used to create fractals.
		numThreads: default=1, a number in [1, 2, ..., 20] is required.
		"""
		try:
			self.numThreads = int(numThreads)
			if numThreads < 1 or numThreads > 20:
				raise NameError("""Value not valid, 
						numThreads has to be in [1, 2, ..., 20]""")
		except NameError:
			raise


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
	
	def __increment(length, minimun, maximun):
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
		incReal = __increment(width, minimun.real, maximun.real)
		incImag = __increment(height, minimun.imag, maximun.imag)
	
		ch = minimun.imag
		cw = minimun.real

		#Use this function to calculate some colums with each thread
		def calculate_colums(colums, numThreads=1, idThread=0):
			imag = []
			ch += idThread*incImag
			for w in colums:
				row = []
				for h in range(width):
					row.append(in_mandelbrot(complex(cw,ch),maxIt))
					cw += incReal
				imag.append(row)
				ch += numThreads*incImag
				cw = minimun.real
			return imag
		
		if self.numThreads == 1:
			calculate_colums(height)
		else:
			pass #TODO call calculate_colums to get the colums

		#TODO join the colums to get the image and return it
		return imag
	
	def julia(c, exp, minimun, maximun, width, height, maxIt):
		"""
		Get a table representation of a Julia (J(c) for exp exponent) set 
		whose size is width x height.
		minimun and maximun are, respectively, the minimun and maximun complex
		numbers that are represented (minimun in the bottom-left and maximun in
		the top-right)
		"""
		incReal = __increment(width, minimun.real, maximun.real)
		incImag = __increment(height, minimun.imag, maximun.imag)
	
		ch = minimun.imag
		cw = minimun.real
	
		imag = []
		#TODO add threading as in mandelbrot	
		for w in range(height):
			row = []
			for h in range(width):
				row.append(in_julia(complex(cw,ch), c, exp, maxIt))
				cw += incReal
			imag.append(row)
			ch += incImag
			cw = minimun.real
		return imag

