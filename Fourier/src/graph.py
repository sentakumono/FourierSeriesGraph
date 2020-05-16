from matplotlib.pyplot import *
from math import *

fig = figure(figsize=(10, 10))
sp = fig.add_subplot(111)
sp.set_aspect('equal')

# Initialize graphs for circles and arms
def draw_circle(func, n, x=0, y=0):
    circles, lines = [], []
    for i in range(n):
        prevx = x
        prevy = y
        re, im, freq, rad, angle = func[i]
        x += rad * cos(freq + angle)
        y += rad * sin(freq + angle)

        c = Circle((prevx, prevy), rad, fill=None, color="#bfd2de")
        sp.add_patch(c)

        circles += [c]

        line, = sp.plot((prevx, x), (prevy, y), color="#cAe3ef")
        lines += [line]
    draw()
    return circles, lines


def draw_outline(x, y):
    # Plot underlining svg function
    sp.plot(x, y, c="#999999")

    # Trace Fourier output
    wave_x = [None] * 2000
    wave_y = [None] * 2000
    image, = sp.plot(wave_x, wave_y, color="#000aaa")

    return wave_x, wave_y, image


# Animate graphs for circles and arms
def update(time, func, cir, lin, n,  x=0, y=0):
    for i in range(n):
        prevx = x
        prevy = y
        re, im, freq, rad, angle = func[i]

        x += rad * cos(freq * time + angle)
        y += rad * sin(freq * time + angle)

        cir[i].center = prevx, prevy
        lin[i].set_xdata((prevx, x))
        lin[i].set_ydata((prevy, y))

    return x, y
