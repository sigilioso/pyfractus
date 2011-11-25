# -.- coding: utf-8 -.-

from multiprocessing import Process, Manager
# TODO Actually use multiprocessing

#
# fractals.py: Fractals, Class to manage fractals representations
#
# Author: Christian Felipe Álvarez <sigilioso@gmail.com>
#
class Fractals:
    """
    A Class to manage fractals representations
    """

    def __init__(self, num_procs=1):
        """
        Create a new instance of Fractals specifiying optionally the number of
        proccesses that are going to be used to create fractals.
        num_procs: default=1, a number in [1, 2, ..., 20] is required.
        """
        self.numThreads = num_procs
        if num_procs < 1 or num_procs > 20:
            raise NameError("""Value not valid
                    num_procs has to be in [1, 2, ..., 20]""")

    def in_mandelbrot(self, c=complex(0.7,1.5), max_it=100):
        """
        Determine if a complex number c is in the Mandelbrot set for a maximum
        number of iterations.
        Return max_it if c is in the Mandelbrot set, and returns the number of
        iterations needed to discover that c is not in the Mandelbrot set otherwise.
        """
        z = complex(0, 0)
        for i in range(0, max_it):
            if abs(z) > 4:
                return i
            else:
                z = z**2 + c
        return max_it

    def in_julia(self, z=complex(0,0), c=complex(0.742,0.1), exp=2, max_it=100):
        """
        Determine if a complex number z is in the Julia J(c) set for a maximum number
        of iterations. J(c) --> z' = z^exp + c
        Returns max_it if c is in this Julia set, and returns the number of
        iterations needed to discover that c is not in J(c) set otherwise.
        """
        for i in range(0, max_it):
            if abs(z**2) > 4:
                return i
            else:
                z = z**exp + c
        return max_it

    def __increment(self, length, minimun, maximun):
        """
        Returns the dinstance between maximun and minimun
        """
        return (maximun - minimun) / length

    def mandelbrot(self, minimun, maximun, width, height, max_it):
        """
        Get a table representation of a Mandelbrot set whose size is
        width x height.
        minimun and maximun are, respectively, the minimun and maximun complex
        numbers that are represented (minimun in the bottom-left and maximun in
        the top-right)
        """
        inc_real = self.__increment(width, minimun.real, maximun.real)
        inc_imag = self.__increment(height, minimun.imag, maximun.imag)

        #Use this function to calculate some colums with each thread
        def calculate_colums(num_procs=1, id_proc=0):
            """
            Each process has to calculate some colums, for example if there is
            two process:
            proc 0 will calculate colums 0, 2, 4, ...
            proc 1 will calculate colums 1, 3, 5, ...
            """
            ch = minimun.imag
            cw = minimun.real
            imag = []
            ch += id_proc*inc_imag
            for w in range(height):
                row = []
                for h in range(width):
                    row.append(self.in_mandelbrot(complex(cw,ch),max_it))
                    cw += inc_real
                imag.append(row)
                ch += num_procs*inc_imag
                cw = minimun.real
            return imag

        imag = []
        if self.num_procs == 1:
            imag = calculate_colums()
        else:
            pass #TODO call calculate_colums to get the colums

        #TODO join the colums to get the image and return it
        return imag

    def julia(self, c, exp, minimun, maximun, width, height, max_it):
        """
        Get a table representation of a Julia (J(c) for exp exponent) set
        whose size is width x height.
        minimun and maximun are, respectively, the minimun and maximun complex
        numbers that are represented (minimun in the bottom-left and maximun in
        the top-right)
        """
        incReal = self.__increment(width, minimun.real, maximun.real)
        incImag = self.__increment(height, minimun.imag, maximun.imag)

        ch = minimun.imag
        cw = minimun.real

        imag = []
        for w in range(height):
            row = []
            for h in range(width):
                row.append(self.in_julia(complex(cw,ch), c, exp, max_it))
                cw += incReal
            imag.append(row)
            ch += incImag
            cw = minimun.real
        return imag

