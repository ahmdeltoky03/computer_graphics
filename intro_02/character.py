from OpenGL.GL import *
from OpenGL.GLUT import *
from math import sin, cos, pi
from numpy import arange


def draw():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0, 0)
    glLineWidth(2)

    # head
    draw_circle(0, 0.45, 0, 360, .15, .01)

    # stomach
    glBegin(GL_POLYGON)
    glVertex2f(-.1, .32)
    glVertex2f(.1, .32)
    glVertex2f(.3, -.3)
    glVertex2f(-.3, -.3)
    glEnd()

    #right arm
    glBegin(GL_LINES)
    slope_1 = (.32+.3)/(.1-.3)
    y_1 = .32 + slope_1 * (.13 - .1)
    glVertex2f(.13, y_1)
    glVertex2f(.41, -.1)
    glEnd()

    # left arm
    glBegin(GL_LINES)
    slope_2 = (.32 + .3)/(-.1 + .3)
    y_2 = .32 + slope_1 * (.13 - .1)
    glVertex2f(-.13, y_2)
    glVertex2f(-.41, -.1)
    glEnd()

    # left leg
    glScale(.7, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2f(-.3, -.3)
    glVertex2f(-.2, -.3)
    glVertex2f(-.2, -.5)
    glVertex2f(-.3, -.5)
    glEnd()
    # right leg
    glBegin(GL_POLYGON)
    glVertex2f(.3, -.3)
    glVertex2f(.2, -.3)
    glVertex2f(.2, -.5)
    glVertex2f(.3, -.5)

    glEnd()



    glFlush()


def draw_circle(shift_x, shift_y, start_ang, end_angle, _radius, _resolution):
    glBegin(GL_POLYGON)
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
