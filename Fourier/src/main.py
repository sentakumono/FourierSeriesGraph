from matplotlib.pyplot import *
from math import *
import svg_xy
import fourier_transform
import graph


# SVG function
img = svg_xy.svg_to_points("elmo.svg")

SKIP = 3
NUM_CIRCLES = len(img) // SKIP

function, x_values, y_values = [], [], []
for i in range(0, len(img), SKIP):
    function += [complex(img[i][0] - 320, -1 * img[i][1] + 240)]
    x_values += [img[i][0] - 320]
    y_values += [-1 * img[i][1] + 240]

# # ellipse function
# NUM_CIRCLES = 100
# x_values, y_values, function = [], [], []
# for p in np.linspace(0, 2 * pi, 100):
#     x_values += [3 * cos(p) + 3]
#     y_values += [2 * sin(p) - 2]
#     function += [complex(3 * cos(p) + 3, 2 * sin(p) - 2)]


trans_func = fourier_transform.dft(function)


# sort circles by radius
def sort_func(lst):
    return lst[3]


trans_func.sort(key=sort_func, reverse=True)

circles, lines = graph.draw_circle(trans_func, NUM_CIRCLES)

wave_x, wave_y, image = graph.draw_outline(x_values, y_values)

# -------------------------------------------------------
# animation loop
for p in np.linspace(0, 6 * pi, 10 * NUM_CIRCLES):
    x, y = graph.update(p, trans_func, circles, lines, NUM_CIRCLES)

    wave_x.pop(-1)
    wave_x.insert(0, x)
    wave_y.pop(-1)
    wave_y.insert(0, y)

    image.set_xdata(wave_x)
    image.set_ydata(wave_y)

    # Reset outline after whole rotation
    if p % (2 * pi) == 0:
        wave_x = [None] * 2000
        wave_y = [None] * 2000

    pause(0.01)
show()
