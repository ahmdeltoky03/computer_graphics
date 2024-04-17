from OpenGL.GL import *
from OpenGL.GLUT import *


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # blue robot

    glColor3f(0, 1, 1)

    glBegin(GL_LINE_LOOP)
    glVertex2f(.1, .48)
    glVertex2f(.1, .37)
    glVertex2f(.05, .37)
    glVertex2f(.05, .3)

    glVertex2f(.3, .3)
    glVertex2f(.3, -.3)
    glVertex2f(.2, -.3)
    glVertex2f(.2, -.15)
    glVertex2f(-.2, -.15)
    glVertex2f(-.2, -.3)
    glVertex2f(-.3, -.3)
    glVertex2f(-.3, .3)

    glVertex2f(-.05, .3)
    glVertex2f(-.05, .37)
    glVertex2f(-.1, .37)
    glVertex2f(-.1, .48)
    glEnd()

    # arm
    glBegin(GL_LINE_LOOP)
    glVertex2f(.3, .3)
    glVertex2f(.4, -.1)

    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex2f(-.3, .3)
    glVertex2f(-.4, -.1)
    glEnd()
    glFlush()


glutInit()
glutInitWindowPosition(0, 100)
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b" Robot Wallet")
glutDisplayFunc(display)
glutMainLoop()
