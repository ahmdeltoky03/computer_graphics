from OpenGL.GL import *
from OpenGL.GLUT import *


def display():
    # glClear(GL_COLOR_BUFFER_BIT)
    # Blue Triangle
    glColor3f(0, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2f(.7, .5)
    glVertex2f(.7, -.5)
    glVertex2f(-.7, -.5)
    glVertex2f(-.7, .5)
    glEnd()
    glFlush()


glutInit()
glutInitWindowPosition(0, 100)
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b" Triangle ")
glutDisplayFunc(display)
glutMainLoop()
