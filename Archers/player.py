from numpy import sin, arctan, cos, deg2rad, sqrt, rad2deg
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from loadfile import obj
g = 9.8
class PLAYER():
    def __init__(self, eyex, eyey, eyez, roty,x,z):
        # =============================================
        self.raduis = sqrt(x**2+z**2)
        if x < 0 and z < 0 :
            self.r_angle =  0  + rad2deg(arctan(abs(x)/abs(z)))
        elif x > 0 and z < 0 :
            self.r_angle = 180 - rad2deg(arctan(abs(x)/abs(z)))
        elif x >0 and z > 0 :
            self.r_angle = 180 + rad2deg(arctan(abs(x)/abs(z)))
        elif x < 0 and z > 0 :
            self.r_angle = 360 - rad2deg(arctan(abs(x)/abs(z)))
        # ============change in roty ==================
        self.delta = deg2rad(roty + self.r_angle )
        dx = sin(self.delta) *self.raduis
        dz = cos(self.delta) *self.raduis
        self.origin = [eyex-dx , eyey , eyez-dz]
        # ==============================================
    def player_motion(self, eyex, eyey, eyez ,roty , rotx):
        # ================ make position ===============
        self.delta = deg2rad(roty + self.r_angle)
        dx = sin(self.delta) *self.raduis
        dz = cos(self.delta) *self.raduis
        self.origin = [eyex-dx , eyey , eyez-dz]
        # ==============================================
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslate(self.origin[0],self.origin[1],self.origin[2])
        glRotate(roty ,0,1,0)
        glRotate(-rotx,1,0,0)
        glCallList(obj[0].gl_list)
        glLoadIdentity()
    # def projectle_motion(self,t, roty, rotx, v0):
    #     alpha = deg2rad(roty)
    #     beta  = deg2rad(rotx)
    #     r  =  v0 * t *cos(alpha)
    #     ry = (v0 * t *sin(alpha))-(0.5*g*(t**2)) + self.origin[1]
    #     rx = r * sin(beta)+ self.origin[0]
    #     rz = r * cos(beta)+ self.origin[2]
    #     return [rx,ry,rz]
    #
    # def cursor(self,roty, rotx, v0):
    #     t = 0
    #     alist = []
    #     alpha = deg2rad(roty)
    #     tmax = 2 * v0 * sin(alpha)/ g
    #
    #     while(t > tmax):
    #         alist.append(self.projectle_motion(t,roty, rotx, v0))
    #         t += tmax/10
    #     glMatrixMode(GL_MODELVIEW)
    #     glLoadIdentity()
    #     for i in alist :
    #         glTranslate(i[0],i[1],i[2])
    #         glCallList(obj[5].gl_list)
    #     glLoadIdentity()
