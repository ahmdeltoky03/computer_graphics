from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 

angle = 10
def DrawGLScene(): 
        global angle
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1,1,1,1)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # gluPerspective(45,5/5,.1,100)
        gluLookAt(.2,.1,.1 ,0,0,0 ,0,1,0)
        
        
        glColor(1,0,1)
        glRotate(angle,0,0,1)
        
        
        glutWireSphere(.5,10,5)
        glutSwapBuffers()
        
        angle+=.01

def main(): 
        glutInit() 
        glutInitWindowSize(500,500)           # Width,Height. The line gets scaled to the window. 
        glutInitWindowPosition(10,30)      # Controls where the window starts - top-left corner of screen. 
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
        glutCreateWindow(b'Wire Sphere') 
        glutDisplayFunc(DrawGLScene)
        glutIdleFunc(DrawGLScene)# Drawing. 
        glutMainLoop() 

main()
