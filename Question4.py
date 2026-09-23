# Question 4

# Three main parts

# A function that creates an n-sided polygon
# A function that waits for the Graph button click, reads the Entry box, and draws the polygon
# main() that creates the window, Entry box, Graph button, and eventually closes the window

from graphics import *
import math

def makePolygon(n):
    angle = 360 / n
    vertices = []

    centerX = 250
    centerY = 250
    radius = 150

    for i in range(n):
        currentAngle = i * angle
        radians = math.radians(currentAngle)

        x = centerX + radius * math.cos(radians)
        y = centerY + radius * math.sin(radians)

        point = Point(x, y)
        vertices.append(point)

    polygon = Polygon(vertices)
    return polygon



def graphPolygon(win, entry, buttonText):
    win.getMouse()

    n = int(entry.getText())

    polygon = makePolygon(n)
    polygon.draw(win)

    buttonText.setText("Exit")
    


def main():
    win = GraphWin("Polygon", 500, 500)

    label = Text(Point(150, 30), "Number of sides:")
    label.draw(win)

    entry = Entry(Point(300, 30), 5)
    entry.draw(win)

    button = Rectangle(Point(200, 450), Point(300, 490))
    button.draw(win)

    buttonText = Text(Point(250, 470), "Graph")
    buttonText.draw(win)

    graphPolygon(win, entry, buttonText)    

    win.getMouse()
    win.close()

main()

