from OpenGL.GL import *
from OpenGL.GLUT import *

"""
GL : Graphic Library
GLUT : Graphic Library Utilities Toolkit

"""


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glutWireTeapot(.5)  # draw teapot
    glFlush() 


glutInit()  # initialize glut
glutInitWindowSize(500, 500)  # window's size
glutInitWindowPosition(0, 100)  # window's position
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Hello OpenGL World")  # window name
glutDisplayFunc(draw)
glutMainLoop()  # sustaining loop
