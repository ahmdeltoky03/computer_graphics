# draw many shapes
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 


v0  =  [-1.4 ,  0.5 , 0.0 ]   
v1  =  [-1.2 , -0.5 , 0.0 ] 

v2  =  [-1.0 ,  0.5 , 0.0 ] 
v3  =  [-0.8 , -0.5 , 0.0 ] 

v4  =  [-0.6 ,  0.5 , 0.0 ] 
v5 =   [-0.4 , -0.5 , 0.0 ]  

v6  =  [-0.2 ,  0.5 , 0.0 ]   
v7  =  [ 0.0 , -0.5 , 0.0 ] 

v8  =  [0.2 ,  0.5  , 0.0 ] 
v9  = [0.4 , -0.5  , 0.0 ] 

v10  = [0.6 ,  0.5  , 0.0 ] 
v11 =  [0.8 , -0.5  , 0.0 ]  

v12  = [1.0 ,  0.5  , 0.0 ]   
v13  = [1.2 , -0.5  , 0.0 ] 

def draw_vert(): 
    glVertex(v0[0], v0[1], v0[2]) 
    glVertex(v1[0], v1[1], v1[2]) 
    glVertex(v2[0], v2[1], v2[2]) 
    glVertex(v3[0], v3[1], v3[2]) 
    glVertex(v4[0], v4[1], v4[2]) 
    glVertex(v5[0], v5[1], v5[2]) 
    glVertex(v6[0], v6[1], v6[2]) 
    glVertex(v7[0], v7[1], v7[2]) 
    glVertex(v8[0], v8[1], v8[2]) 
    glVertex(v9[0], v9[1], v9[2]) 
    glVertex(v10[0], v10[1], v10[2]) 
    glVertex(v11[0], v11[1], v11[2]) 
    glVertex(v12[0], v12[1], v12[2]) 
    glVertex(v13[0], v13[1], v13[2]) 


def points():
  glColor(1,0,0)
  
  glPointSize(3)
  glBegin(GL_POINTS)
  draw_vert()
  
  glEnd()
  

def unjoined_line(): 
    """ Joins PAIRS of unconnected segments. """ 
    glBegin(GL_LINES) 
    glColor(1.0, 0.0, 0.0)  # Red 
    draw_vert() 
    glEnd() 

def joined_line(): 
    """ Joins all points in sequence. """ 
    glBegin(GL_LINE_STRIP) 
    glColor(0.2, 0.2, 1.0)  # Blue 
    draw_vert() 
    glEnd() 

def line_loop(): 
    """ Joins all points in sequence, closing the loop. """ 
    glBegin(GL_LINE_LOOP) 
    glColor(0.0, 1.0, 1.0)  # Turquoise 
    draw_vert() 
    glEnd() 

def triangles(): 
    """ Makes triangles of groups of three. """ 
    glBegin(GL_TRIANGLES) 
    glColor(0.0, 1.0, 0.0)  # Green 
    draw_vert() 
    glEnd() 

def triangle_strip(): 
    """ First triangle using the first, second, and third vertices,
        and then another using the second, 
        third, and fourth vertices, and so on. """ 
    glBegin(GL_TRIANGLE_STRIP) 
    glColor(0.8, 1.0, 0.0)  # Orange 
    draw_vert() 
    glEnd() 
    
def triangle_fan(): 
    """ First triangle using the first, second, and third vertices,
        and then another using the second, 
        third, and fourth vertices, and so on. """ 
    glBegin(GL_TRIANGLE_FAN) 
    glColor(0.0, 0.8, 0.0)  # Orange 
    draw_vert() 
    glEnd() 

def quads(): 
    """ First quadrilateral using the first four vertices, 
        and then another using the next four, 
        and so on. 
    """ 
    glBegin(GL_QUADS) 
    glColor(1.0, 0.40, 0.0)  # Orange 
    draw_vert() 
    glEnd() 
    
def quads_strip(): 
    """ A linked strip of four-sided polygons. """ 
    glBegin(GL_QUAD_STRIP) 
    glColor(1.0, 0.20, 0.0)  # Dark Orange 
    draw_vert() 
    glEnd() 
    
def polygon(): 
    
    glBegin(GL_POLYGON) 
    glColor(1.0, 1.0, 0)  # Yellow 
    ############vertex_set()  # Unexpected Behavior
    draw_vert()
    glEnd() 
    
def draw():
  glClear(GL_COLOR_BUFFER_BIT)
  glClearColor(1,1,1,1)
  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  
  glScale(.6,.6,1)
  points()
  # unjoined_line()
  # joined_line()
  line_loop()
  # triangles()
  # triangle_strip()
  # triangle_fan()
  # quads()
  # quads_strip()
  # polygon()
  
  glFlush()

glutInit()
glutInitWindowPosition(0,100)
glutInitWindowSize(500,500)
glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
glutCreateWindow(b"Shape")
glutDisplayFunc(draw)
glutMainLoop()

