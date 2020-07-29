from xml.dom import minidom


# Convert SVG path to array of (x, y) points.
# SVG paths made in GIMP
def svg_to_points(svg):
    svg_file = open(svg, "r")

    file = minidom.parse(svg_file)
    path_strings = [path.getAttribute('d') for path in file.getElementsByTagName('path')]

    curve = []
    path = path_strings[0]
    while "Z" in path:
        curve += [element for element in path[path.index('C') + 1: path.index('Z')].split()]
        path = path[path.index("Z") + 1: len(path)]

    pair_array = []
    points = []
    for x in range(len(curve)):
        points += curve[x].split(",")
        if points[-1] is not None:
            pair_array += [(float(points[0]), float(points[1]))]
            points = points[2: -1]

    return pair_array
