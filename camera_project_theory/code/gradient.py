from OpenGL.GL import *
from OpenGL.GLUT import *


angle = 10
def draw():
  
  global angle 
  
  glClearColor(1,1,1,1)
  glClear(GL_COLOR_BUFFER_BIT)
  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  
  
  glBegin(GL_POLYGON)
  
  glColor3f(1,0,0)
  glVertex2d(0,0)

  glColor3f(0,1,0)
  glVertex2d(0,1)

  glColor3f(0,0,1)
  glVertex2d(1,0)
  
  glEnd()
  
  glFlush()








glutInit()
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"gradient colors")
glutDisplayFunc(draw)
glutMainLoop()

