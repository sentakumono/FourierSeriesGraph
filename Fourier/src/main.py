from matplotlib.pyplot import *
from math import *
import svg_xy
import fourier_transform

fig = figure(figsize=(10, 10))
sp = fig.add_subplot(111)
sp.set_aspect('equal')


# Initialize graphs for circles and arms
def draw_circle(func, x=0, y=0):
    circles, lines = [], []
    for i in range(NUM_CIRCLES):
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


# Animate graphs for circles and arms
def update(time, func, cir, lin, x=0, y=0):
    for i in range(NUM_CIRCLES):
        prevx = x
        prevy = y
        re, im, freq, rad, angle = func[i]

        x += rad * cos(freq * time + angle)
        y += rad * sin(freq * time + angle)

        cir[i].center = prevx, prevy
        lin[i].set_xdata((prevx, x))
        lin[i].set_ydata((prevy, y))

    return x, y


# -------------------------------------------------------

# SVG function
img = svg_xy.svg_to_points("elmo.svg")

function, x_values, y_values = [], [], []

print(len(img))
SKIP = 3
NUM_CIRCLES = len(img) // SKIP

for i in range(0, len(img), SKIP):
    function += [complex(float(img[i][0]) - 320, -1 * float(img[i][1]) + 240)]
    x_values += [float(img[i][0]) - 320]
    y_values += [-1 * float(img[i][1]) + 240]
#
# # ellipse function
# x, y, function = [], [], []
# for p in np.linspace(0, 2 * pi, 100):
#     x += [3 * cos(p) + 3]
#     y += [2 * sin(p) - 2]
#     function += [complex(3 * cos(p) + 3, 2 * sin(p) - 2)]

sp.plot(x_values, y_values, c="999999")

trans_func = fourier_transform.dft(function)


# sort circles by radius
def sort_func(lst):
    return lst[3]


trans_func.sort(key=sort_func, reverse=True)

circles, lines = draw_circle(trans_func)

# resulting function
wave_x = [None] * 2000
wave_y = [None] * 2000
image, = sp.plot(wave_x, wave_y, color="#000aaa")

# -------------------------------------------------------
# animation loop
for p in np.linspace(0, 6 * pi, 6000):
    x, y = update(p, trans_func, circles, lines)

    wave_x.pop(-1)
    wave_x.insert(0, x)
    wave_y.pop(-1)
    wave_y.insert(0, y)

    image.set_xdata(wave_x)
    image.set_ydata(wave_y)

    pause(0.01)
show()
