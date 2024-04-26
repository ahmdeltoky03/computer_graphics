# drawing line using OpenGl
from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import *

x_0 = 1.0
y_0 = 1.0
x_1 =-1.0
y_1 = 1.0


def InitGl(width,height):
  
  glClearColor(0.0,0.0,0.0,0.0)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(45,width/height,0.1,100.0)
  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  

def any_line(x_0,y_0,x_1,y_1,R,G,B):
  
  glColor(R,G,B)
  glBegin(GL_LINES)
  glVertex(x_0,y_0,-1)
  glVertex(x_1,y_1,-1)
  glEnd()

def draw():
  
  glClear(GL_COLOR_BUFFER_BIT)
  
  glTranslate(0,0,-1.5)
  # glTranslate(0,0,-1.0) # outside frustum
  # glTranslate(0,0,-99)
  # glTranslate(0,0,-100) # outside frustum



  glLineWidth(5)
  any_line(x_0,y_0,x_1,y_1,1,1,1)
  
  glFlush()



def main():
  """main function
  """
  glutInit()
  glutInitWindowPosition(0,100)
  glutInitWindowSize(500,500)
  glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
  glutCreateWindow(b"OpenGL Line")
  glutDisplayFunc(draw)
  InitGl(5,5)
  glutMainLoop()
  
  
main()