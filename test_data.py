import math
import random
import pylab
import matplotlib.patches, matplotlib.pyplot

random.seed(0)


# WAP - Wireless Access Point
def get_test_data(start_point, points_num, WAP):
    x = []  # x coordinates
    y = []  # y coordinates
    r = []  # radiuses
    dist = [] # distances between two adjacent points

    x.append(start_point[0])
    y.append(start_point[1])

    dist_ = math.sqrt((start_point[0] - 0)**2 + (start_point[1] - 0)**2)
    dist.append(dist_)

    dist_ = math.sqrt((start_point[0] - WAP[0])**2 + (start_point[1] - WAP[1])**2)
    r.append(dist_)

    for i in range(0, points_num):
        x_ = x[-1] + random.randint(-2, 5)
        y_ = y[-1] + random.randint(-2, 5)
        dist_ = math.sqrt((x_ - x[-1])**2 + (y_ - y[-1])**2)
        dist.append(dist_)
        x.append(x_)
        y.append(y_)

        dist_ = math.sqrt((x[-1] - WAP[0])**2 + (y[-1] - WAP[1])**2)
        r.append(dist_)

    return x, y, r, dist


def draw_circles(axes, radiuses, WAP):
    for r in radiuses:
        circle = matplotlib.patches.Circle((WAP[0], WAP[1]), radius=r, fill=False, color="r")
        axes.add_patch (circle)


def show_coordinates(x, y):
    for i in range(len(x)):
        annt = '(' + str(x[i]) + ',' + str(y[i]) + ')'
        matplotlib.pyplot.annotate(annt, xy=(x[i], y[i]))


def draw_trajectory(x, y):
    pylab.plot(x, y, 'bo', label='sampled')
    pylab.plot(x, y, label='continuous')

    show_coordinates(x, y)
    # pylab.legend()


# WAP - Wireless Access Point
def main():
    start_point = [0,0]
    points_num = 20
    WAP = [0, 0]

    x, y, radiuses, distances = get_test_data(start_point, points_num, WAP)

    axes = pylab.gca()
    axes.set_aspect("equal")

    y_min = min(y)
    x_min = min(x)
    y_max = max(y)
    x_max = max(x)

    pylab.ylim(y_min - 1, y_max + 1)
    pylab.xlim(x_min - 1, x_max + 1)
    pylab.grid()

    draw_trajectory(x, y)
    draw_circles(axes, radiuses, WAP)

    pylab.plot(start_point[0], start_point[1], 'bo', color='red', label='start_point')
    pylab.plot(x[-1], y[-1], 'bo', color='red', label='end_point')

    pylab.show()

main()