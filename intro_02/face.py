from OpenGL.GL import *
from OpenGL.GLUT import *
from math import sin, cos, pi
from numpy import arange


def draw():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 0.8, 1.0)
    glLineWidth(3)

    draw_circle(0, -.31, -180, 0, .12, .01)
    draw_circle(.15, .1, 0, 360, .04, .01)
    draw_circle(-.15, .1, 0, 360, .04, .01)
    draw_circle(0, -.2, 0, 360, .04, .01)
    draw_circle(0, 0, 0, 360, .55, .01)

    glFlush()


def draw_circle(shift_x, shift_y, start_ang, end_angle, _radius, _resolution):
    glBegin(GL_LINE_STRIP)
    r = _radius
    resolution = _resolution
    for i in arange(start_ang, end_angle, resolution):
        x = r * cos(i * pi / 180) + shift_x
        y = r * sin(i * pi / 180) + shift_y
        glVertex2d(x, y)
    glEnd()


glutInit()
glutInitWindowSize(500, 500)  # Set the window's initial width & height # TODO: try commenting this
glutInitWindowPosition(1000, 100)  # position # TODO: try commenting this
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # GLUT_SINGLE:single buffer [or operator, logically and]
glutCreateWindow(b"Draw Face")  # action bar # TODO: try changing this
glutDisplayFunc(draw)  # main loop  # TODO: try commenting this
glutMainLoop()

