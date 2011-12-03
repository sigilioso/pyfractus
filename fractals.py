# -.- coding: utf-8 -.-

"""
fractals.py

Module which include a class to manage fractals representations
"""

from multiprocessing import Process
from multiprocessing.sharedctypes import Value
from ctypes import c_double

class Fractals:
    """
    A Class to manage fractals representations
    """

    def __init__(self, num_procs=1):
        """
        Create a new instance of Fractals specifiying optionally the number of
        proccesses that are going to be used to create fractals.
        `num_procs`: default=1, a number in [1, 2, ..., 20] is required.
        """
        self.num_procs = num_procs
        if num_procs < 1 or num_procs > 20:
            raise Exception("""Value not valid
                    num_procs has to be in [1, 2, ..., 20]""")

    def in_mandelbrot(self, c=complex(0.7,1.5), max_it=100):
        """
        Determine if a complex number c is in the Mandelbrot set for a maximum
        number of iterations.
        Returns `max_it` if `c` is in the Mandelbrot set, and returns the number of
        iterations needed to discover that `c` is not in the Mandelbrot set otherwise.
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
        Returns `max_it` if `c` is in this Julia set, and returns the number of
        iterations needed to discover that `c` is not in J(c) set otherwise.
        """
        for i in range(0, max_it):
            if abs(z**2) > 4:
                return i
            else:
                z = z**exp + c
        return max_it

    def __increment(self, length, minimun, maximun):
        """
        Returns the dinstance between `maximun` and `minimun`
        """
        return (maximun - minimun) / length

    def mandelbrot(self, minimun, maximun, width, height, max_it):
        """
        Get a table representation of a Mandelbrot set (for `max_it` iterations)
        whose size is `width` x `height`.
        `minimun` and `maximun` are, respectively, the minimun and maximun complex
        numbers that are represented (minimun in the bottom-left and maximun in
        the top-right)
        """
        inc_real = self.__increment(width, minimun.real, maximun.real)
        inc_imag = self.__increment(height, minimun.imag, maximun.imag)

        #Use this function to calculate some colums with each process
        def calculate(image, num_procs=1, id_proc=0):
            """
            Each process has to calculate some colums, for example if there is
            two process:
            proc 0 will calculate colums 0, 2, 4, ...
            proc 1 will calculate colums 1, 3, 5, ...
            """
            ch = minimun.imag
            cw = minimun.real
            ch += id_proc*inc_imag
            for w in range(id_proc, height, num_procs):
                for h in range(width):
                    image[w][h] = self.in_mandelbrot(c=complex(cw, ch), max_it=max_it)
                    cw += inc_real
                ch += num_procs * inc_imag
                cw = minimun.real

        # Create the image as a c_double table
        Image = (c_double * width) * height
        # Use shared memory to store the image
        image = Value(Image)

        # Use processes to do calculations
        if self.num_procs == 1:
            calculate(image)
        else:
            processes = []
            for id in range(self.num_procs):
                processes.append(Process(target=calculate,
                    args=(image, self.num_procs, id)))
                processes[-1].start()
            for p in processes:
                if p.is_alive():
                    p.join()

        # Get the image values as a double list
        return map(list, list(image))

    def julia(self, c, exp, minimun, maximun, width, height, max_it):
        """
        Get a table representation of a Julia (J(c) for exp exponent and `max_it`)
        set whose size is `width` x `height`.
        `minimun` and `maximun` are, respectively, the minimun and maximun complex
        numbers that are represented (minimun in the bottom-left and maximun in
        the top-right)
        """
        inc_real = self.__increment(width, minimun.real, maximun.real)
        inc_imag = self.__increment(height, minimun.imag, maximun.imag)

        #Use this function to calculate some colums with each process
        def calculate(image, num_procs=1, id_proc=0):
            """
            Each process has to calculate some colums, for example if there is
            two process:
            proc 0 will calculate colums 0, 2, 4, ...
            proc 1 will calculate colums 1, 3, 5, ...
            """
            ch = minimun.imag
            cw = minimun.real
            ch += id_proc*inc_imag
            for w in range(id_proc, height, num_procs):
                for h in range(width):
                    image[w][h] = self.in_julia(complex(cw, ch), c, exp, max_it)
                    cw += inc_real
                ch += num_procs * inc_imag
                cw = minimun.real

        # Create the image as a c_double table
        Image = (c_double * width) * height
        # Use shared memory to store the image
        image = Value(Image)

        # Use processes to do calculations
        if self.num_procs == 1:
            calculate(image)
        else:
            processes = []
            for id in range(self.num_procs):
                processes.append(Process(target=calculate,
                    args=(image, self.num_procs, id)))
                processes[-1].start()
            for p in processes:
                if p.is_alive():
                    p.join()

        # Get the image values as a double list
        return map(list, list(image))



