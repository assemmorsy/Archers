import OpenGL.GL
from OpenGL.GLU import *
from numpy import sin, cos, deg2rad


class Camera():
    def __init__(self, eye, center, up, fovy, aspect, near, far):
        self.eye = eye
        self.center = center
        self.up = up
        self.fovy = fovy
        self.aspect = aspect
        self.near = near
        self.far = far

    def updateCam(self):
        OpenGL.GL.glMatrixMode(OpenGL.GL.GL_PROJECTION)
        OpenGL.GL.glLoadIdentity()
        gluPerspective(self.fovy, self.aspect, self.near, self.far)
        gluLookAt(self.eye[0], self.eye[1], self.eye[2],
                  self.center[0], self.center[1], self.center[2],
                  self.up[0], self.up[1], self.up[2])

    def get_cam_mat(self):
        return [self.eye, self.center, self.up]

    def set_cam_mat(self, eye, center, up):
        self.eye = eye
        self.center = center
        self.up = up

    def translatex(self,tx,roty):
        self.rotatey(roty-deg2rad(90))
        self.translatez(tx,roty-deg2rad(90))
        self.rotatey(roty)
        self.updateCam()

    def translatez(self,tz,roty):
        i = sin(roty)
        k = cos(roty)
        self.eye[0] += i*tz
        self.eye[2] += k*tz
        self.center[0] += i*tz
        self.center[2] += k*tz
        self.updateCam()

    def rotatey(self, theta):
        self.center[0] = 2* sin(theta) + self.eye[0]
        self.center[2] = 2* cos(theta) + self.eye[2]
        self.updateCam()
