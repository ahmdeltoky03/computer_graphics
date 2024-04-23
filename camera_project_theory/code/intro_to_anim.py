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
  
  # rectangle
  glColor3f(0,1,.8)
  glBegin(GL_POLYGON)
  glVertex2d(.5,.5)
  glVertex2d(-.5,.5)
  glVertex2d(-.5,-.5)
  glVertex2d(.5,-.5)
  glEnd()

  
  angle+=.1
  print(angle)
  
  
  
  
  glutSwapBuffers()








glutInit()
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"intro_to_animation")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()

# use glutIdleFunc(draw)
# replace glFlush() -->> glutSwapBuffers()
# GLUT_SINGLE -->> GLUT_DOUBLE