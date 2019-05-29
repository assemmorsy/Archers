from random import randrange
from OpenGL.GL import *
from loadfile import obj
from numpy import sin, arctan, cos, deg2rad, sqrt, rad2deg

step = 0.01
class ENEMY():
    def __init__(self,x,z):
        self.x = x
        self.z = z

    def move(self,player):
        a = player.origin
        dz = self.z - a[2]
        dx = self.x - a[0]
        # ==============translate calc.==================
        sx = self.x - dx * step
        sz = self.z - dz * step
        # ==============rotate calc.==================
        if dx < 0 and dz < 0 :
            zeta =  180  + rad2deg(arctan(abs(dx)/abs(dz)))
        elif dx > 0 and dz < 0 :
            zeta = 180 - rad2deg(arctan(abs(dx)/abs(dz)))
        elif dx >0 and dz > 0 :
            zeta = 0 + rad2deg(arctan(abs(dx)/abs(dz)))
        elif dx < 0 and dz > 0 :
            zeta = 360 - rad2deg(arctan(abs(dx)/abs(dz)))
        # =====================render =================
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslate(sx ,0, sz)
        glRotate((180+zeta),0,1,0)
        glScale(2.5,2.5,2.5)
        glCallList(obj[2].gl_list)
        glLoadIdentity()
        #====================saving ==============
        self.x = sx
        self.z = sz

    def arrow_collition(self,arrow_on_air):
        for i in arrow_on_air:
            if i.origin[1]+i.ry  <  4.75 :
                if i.origin[0]+i.rx > (self.x - 1.5) and i.origin[0]+i.rx < (self.x + 1.5) :
                    if i.origin[2]+i.rz > (self.z -0.5) and i.origin[2]+i.rz < (self.z +0.5) :
                        return  i
