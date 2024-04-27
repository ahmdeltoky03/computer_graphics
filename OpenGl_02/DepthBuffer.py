from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 

def InitGL(width,height):
  glClearColor(0,0,0,0)
  
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(120,width/height,.1,100)
  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  
  glEnable(GL_DEPTH_TEST)


def DrawGLScene(): 
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


  glColor(1,0,0) # red
  glBegin(GL_QUADS)
  glVertex(-.5,-.5,-1)
  glVertex(-.5,.5,-1)
  glVertex(.5,.5,-1)
  glVertex(.5,-.5,-1)
  glEnd() 
  
  glColor(1,1,0) # yellow
  glBegin(GL_QUADS)
  glVertex(-.5,-.5,-.5)
  glVertex(-.5,.5,-.5)
  glVertex(.5,.5,-.5)
  glVertex(.5,-.5,-.5)
  glEnd()
  

  

  

  

  
  
  
  glFlush()

def main(): 
        glutInit() 
        glutInitWindowSize(500,500)           # Width,Height. The line gets scaled to the window. 
        glutInitWindowPosition(10,30)      # Controls where the window starts - top-left corner of screen. 
        glutInitDisplayMode(GLUT_DEPTH)
        glutCreateWindow(b'Depth Buffer') 
        glutDisplayFunc(DrawGLScene)
        InitGL(5,5)
        glutMainLoop() 

main()
