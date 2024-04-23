from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw():
  glClearColor(1.0,1.0,1.0,1.0)
  glClear(GL_COLOR_BUFFER_BIT)
  
  
  # glOrtho(-1,1,-1,1,-1,1)
  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  
  gluLookAt(0,0,0,0,0,1,0,1,0)

  glColor3f(1,0,0)
  glBegin(GL_POLYGON)
  
  glVertex3f(0,0,1)
  glVertex3f(0,.5,1)
  glVertex3f(.5,0,1)
  glEnd()
  
  
  
  glColor3f(0,1,0)
  glBegin(GL_POLYGON)
  
  glVertex3f(0,0,0)
  glVertex3f(0,.1,0)
  glVertex3f(.1,0,0)
  
  glEnd()
  

  
  
  
  # glColor3f(0,1,0)
  # glBegin(GL_POLYGON)
  
  # glVertex3f(0,0,0)
  # glVertex3f(0,.1,0)
  # glVertex3f(.1,0,0)
  
  # glEnd()
  
  # glColor3f(1,0,0)
  # glBegin(GL_POLYGON)
  
  # glVertex3f(0,0,1)
  # glVertex3f(0,.5,1)
  # glVertex3f(.5,0,1)
  # glEnd()
  
  
  glFlush()


glutInit()
glutInitWindowPosition(0,100)
glutInitWindowSize(500,500)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Look_at_func")
# glEnable(GL_DEPTH_TEST)
glutDisplayFunc(draw)
glutMainLoop()