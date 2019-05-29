from numpy import sin, arctan, cos, deg2rad, sqrt, rad2deg
from OpenGL.GL import *
from loadfile import obj

g = 9.8

class ARROW():
    def __init__(self, eyex, eyey, eyez, roty, rotx, v0,x,z):
        self.t = 0
        self.alpha = deg2rad(rotx)
        self.beta = deg2rad(roty)
        self.v0 = v0
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
        # ============change in roty ===================
        self.delta = deg2rad(roty + self.r_angle)
        dx = sin(self.delta) *self.raduis
        dz = cos(self.delta) *self.raduis
        # ===============================================
        self.origin = [eyex-dx , eyey , eyez-dz]
        # ===============================================
        self.tmax = self.v0 * sin(self.alpha) / g
        self.H = ((v0*sin(self.alpha))**2)/2*g
        self.projectle_motion()

    def projectle_motion(self):
        self.vx =  self.v0*cos(self.alpha)
        self.vy = (self.v0 * sin(self.alpha))-(g * self.t)
        self.r  =  self.v0 * self.t *cos(self.alpha)
        self.ry = (self.v0 *self.t *sin(self.alpha))-(0.5*g*(self.t**2))
        self.v  = sqrt((self.vx**2)+(self.vy**2))
        self.theta = -rad2deg(arctan(self.vy/self.vx))
        self.rx = self.r * sin(self.beta)
        self.rz = self.r * cos(self.beta)

    def update(self):
        if self.ry + self.origin[1] - 1.677*sin(deg2rad(self.theta)) > 0 :
            self.t += 0.05
            x = 0
            self.projectle_motion()
        else :
            x = 1
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslate(self.origin[0]+self.rx,self.origin[1]+self.ry,self.origin[2]+self.rz)
        glRotate(rad2deg(self.beta),0,1,0)
        glRotate(self.theta,1,0,0)
        glCallList(obj[1].gl_list)
        glLoadIdentity()
        return x
