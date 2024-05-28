import tkinter as tk
import math


def put_pixel(canvas, x, y, color):
    canvas.create_rectangle((x, y, x+1, y+1), outline=color, fill=color)


def bezier(points, t):
    n = len(points) - 1
    x = sum(binomial_coeff(n, i) * (1-t)**(n-i) * t**i * points[i][0] for i in range(n+1))
    y = sum(binomial_coeff(n, i) * (1-t)**(n-i) * t**i * points[i][1] for i in range(n+1))
    return x, y


def binomial_coeff(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coeff(n-1, k-1) + binomial_coeff(n-1, k)


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def draw_bezier_curve(canvas, points, color):
    t = 0
    step = 0.001
    prev_x, prev_y = bezier(points, t)
    while t <= 1:
        x, y = bezier(points, t)
        put_pixel(canvas, x, y, color)
        d = distance(prev_x, prev_y, x, y)
        if d > 1:
            step /= 2
        else:
            step *= 1.1
        prev_x, prev_y = x, y
        t += step


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

control_points = [(50, 300), (150, 50), (250, 350), (350, 100), (222, 122)]

draw_bezier_curve(canvas, control_points, 'green')

root.mainloop()
