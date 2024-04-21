from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



def draw():
  glClearColor(1.0,1.0,1.0,1.0)
  glClear(GL_COLOR_BUFFER_BIT)


  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()

  glRotate(-30,0,0,1)
  glScale(1.5,1,1)
  
  glRotate(30,0,0,1)
  # print("Rotation by 30 ", glGetFloatv(GL_MODELVIEW_MATRIX))
  # triangle
  
  glBegin(GL_POLYGON)
  glColor3f(0,1,0)
  glVertex2d(.5,.4)
  glVertex2d(-.5,.4)
  glVertex2d(0,.8)
  glEnd()
  
  
  # rectangle
  
  glBegin(GL_POLYGON)
  glColor3f(1,0,1)
  glVertex2d(.5,.4)
  glVertex2d(-.5,.4)
  glVertex2d(-.5,0)
  glVertex2d(.5,0)
  glEnd()
  
  glLineWidth(1.5)
  # Vertical axis
  glBegin(GL_LINES)
  glColor3f(0,0,0)
  glVertex2d(0,-1)
  glVertex2d(0,1)
  glEnd()
  
  # Horizontal axis
  glBegin(GL_LINES)
  glColor3f(0,0,0)
  glVertex2d(-1,0)
  glVertex2d(1,0)
  glEnd()
  glFlush()
  


glutInit()
glutInitWindowSize(500,500)
glutInitWindowPosition(0,100)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"house_with_transformations")
glutDisplayFunc(draw)
glutMainLoop()
