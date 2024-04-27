
from OpenGL.GL import *
from OpenGL.GLU import * 
from OpenGL.GLUT import * 

zloc = 0
angle = 0

def init():
  glClearColor(1,1,1,1)
  
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(120,1,.1,10)
  
  # glOrtho(-2,2,-2,2,-3,3)
  # gluLookAt(.2,0.2,0.2,0,0,0,0,1,0)
  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()

  glEnable(GL_DEPTH_TEST)
def display_1():
  global zloc
  global angle
  
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glColor(0,0,1)
  
  glLoadIdentity() # necessary to remove the transformation effect
  glTranslate(0,0,zloc)
  glRotate(angle,0,1,0)
  
  glutWireTeapot(1)
  
 
  
  angle+=.1
  zloc-=.0005
  
  glFlush()


def main():
          glutInit( ) 
          glutInitWindowSize(500, 500) 
          glutInitWindowPosition(0,100)
          glutCreateWindow(b'animation_02') 
          glutDisplayFunc(display_1)
          glutIdleFunc(display_1)
          init() # Any function name for initialization
          glutMainLoop()
main()