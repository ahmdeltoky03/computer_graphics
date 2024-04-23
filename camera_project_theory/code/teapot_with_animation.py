from OpenGL.GL import *
from OpenGL.GLUT import *


angle = 10
def draw():
  
  global angle 
  
  glClearColor(1,1,1,1)
  glClear(GL_COLOR_BUFFER_BIT)
  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  
  glRotate(angle,0,0,1)
  # glRotate(angle,0,1,0)
  # glRotate(angle,1,0,0)

  # teapot
  glColor3f(1,0,0)
  glutWireTeapot(.5)

  
  angle+=.1
  print(angle)
  
  
  
  
  glutSwapBuffers()








glutInit()
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"teapot")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()

# use glutIdleFunc(draw)
# replace glFlush() -->> glutSwapBuffers()
# GLUT_SINGLE -->> GLUT_DOUBLE