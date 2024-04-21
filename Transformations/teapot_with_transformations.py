from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



def draw():
  glClearColor(1.0,1.0,1.0,1.0)
  glClear(GL_COLOR_BUFFER_BIT)


  glColor3d(0.0,0.0,0.0)
  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  
  
  # transformation 1
  # glScale(3.0,1,1)
  # glTranslate(0,-.7,0)
  # glRotate(120,0,0,1)
  
  
  # transformation 2
  # glTranslate(0.0,-.7,0)
  # glRotate(120,0,0,1)
  # glScale(3,1,1)
  
  
  # transformation 3
  glRotate(120,0,0,1)
  glTranslate(0.0,-.7,0)
  glScale(3,1,1)
  
  
  
  glutSolidTeapot(.1)
  glFlush()
  


glutInit()
glutInitWindowSize(500,500)
glutInitWindowPosition(0,100)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"teapot_with_transformations")
glutDisplayFunc(draw)
glutMainLoop()

# transformations 1,2,3 are not same because martix multiplication is not commutative SRT != STR != RTS
# 1- RTS
# 2- SRT
# 3- STR