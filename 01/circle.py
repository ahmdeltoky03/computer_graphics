from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # Blue Triangle
    glColor3f(0, 1, 1)
    r = 1
    glBegin(GL_LINE_LOOP)
    for i in range(0, 360):
        x = r * cos(i*pi/180)
        y = r * sin(i*pi/180)
        glVertex2d(x, y)
    glEnd()
    glFlush()


glutInit()
glutInitWindowPosition(0, 100)
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b" Triangle ")
glutDisplayFunc(display)
glutMainLoop()
