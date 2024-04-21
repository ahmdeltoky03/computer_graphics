from OpenGL.GL import *
from OpenGL.GLUT import *


def draw():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotate(30, 0, 0, 1)
    glLineWidth(5)

    glBegin(GL_LINE_LOOP)
    glVertex2f(.5, .5)
    glVertex2f(-.5, .5)
    glVertex2f(-.5, -.5)
    glVertex2f(.5, -.5)

    glEnd()
    glFlush()


glutInit()
glutInitWindowSize(500, 500)  # Set the window's initial width & height # TODO: try commenting this
glutInitWindowPosition(1000, 100)  # position # TODO: try commenting this
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # GLUT_SINGLE:single buffer [or operator, logically and]
glutCreateWindow(b"Hello OGL Program")  # action bar # TODO: try changing this
glutDisplayFunc(draw)  # main loop  # TODO: try commenting this
glutMainLoop()
