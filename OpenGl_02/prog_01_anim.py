
from OpenGL.GL import *
from OpenGL.GLU import * 
from OpenGL.GLUT import * 

scale = 1
increasing = 1

def init():
  glClearColor(1,1,1,1)
  
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  # gluPerspective(120,5/5,.1,10)
  
  glMatrixMode(GL_MODELVIEW)
  # glLoadIdentity()

def display_1():
  global scale
  global increasing
  
  glClear(GL_COLOR_BUFFER_BIT)
  glColor(0,0,1)
  
  glLoadIdentity()
  
  # glTranslate(0,0,-7)
  glScale(scale,scale,scale)
  glutSolidSphere(.1,100,100)
  
  if scale < 1 :
    increasing = 1
  if scale > 10 :
    increasing = 0
  
  if increasing:
    scale += .001
  else :
    scale -= .001
  
  
  
  glFlush()


def main():
          glutInit( ) 
          glutInitWindowSize(500, 500) 
          glutInitWindowPosition(0,100)
          glutCreateWindow(b'animation_01') 
          glutDisplayFunc(display_1)
          glutIdleFunc(display_1)
          init() # Any function name for initialization
          glutMainLoop()
main()