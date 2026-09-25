# Question 5

import math
from graphics import *

# making equation into its own funtion
def logistic(L, k, i):
    y = L / (1 + math.exp(-k * i))
    return y

def main():

    print("This program graphs a logistic funtion.")
    
    win = GraphWin("Logistic Function", 500, 500)

    L = 100
    k = 0.1

    # draw x-axis
    x_axis = Line(Point(50, 450), Point(450, 450))
    x_axis.draw(win)

    # draw y-axis
    y_axis = Line(Point(50, 450), Point(50, 50))
    y_axis.draw(win)

    for i in range(100):
        y = logistic(L, k, i)

        x_coord = 50 + (i * 4)
        y_coord = 450 - (y * 4)

        point = Point(x_coord, y_coord)
        point.draw(win)

    win.getMouse()
    win.close()


main()