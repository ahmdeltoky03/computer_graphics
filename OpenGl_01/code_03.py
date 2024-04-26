# drawing wire cube using OpenGl
from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import *


def InitGl():
  
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  
  gluLookAt(.2,.1,.1, 0,0,0 , 0,1,0)
  # gluLookAt(2,1,1, 0,0,0 , 0,1,0)

  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  



def draw():
  
  glClearColor(1,1,1,0)
  glClear(GL_COLOR_BUFFER_BIT)
  
  
  glPointSize(5)

  glColor(0,1,0)
  glBegin(GL_POINTS)
  glVertex3d(0,.1,0)
  glEnd() 
  
  glLineWidth(3)
  # glRotate(30,0,0,1)
  # glScale(.5,.5,.5)
  glutWireCube(1)
  


  glFlush()



def main():
  """main function
  """
  glutInit()
  glutInitWindowPosition(0,100)
  glutInitWindowSize(500,500)
  glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
  glutCreateWindow(b"Wire Cube")
  glutDisplayFunc(draw)
  InitGl()
  glutMainLoop()
  
  
main()