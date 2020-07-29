from math import *


# Discrete Fourier Transform of complex function
def dft(func):
    new_func = []
    num = len(func)

    for i in range(-1 * num // 2, num // 2):
        sum = complex(0, 0)
        for j in range(num):
            angle = ((2 * pi) * i * j) / num
            c = complex(cos(angle), -1 * sin(angle))
            sum += func[j] * c
        re = sum.real / num
        im = sum.imag / num
        sum = complex(re, im)
        new_func += [(sum.real, sum.imag, i, sqrt(sum.real ** 2 + sum.imag ** 2), atan2(sum.imag, sum.real))]

    return new_func
