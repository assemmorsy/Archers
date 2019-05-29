from loadfile import loadFunc
from camera import *
from player import *
from enemy import *
from arrows import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# ========some definitions=========
rotx = 0
roty = 0
# =================================
tx = 0
tz = 0
# =================================
i =  0.7
k =  -1
# =================================
arrows_on_air = []
arrows_on_ground = []
v0=10
# =================================
eye = [0, 4, 0]
center = [0, 4, 1]
up = [0, 1, 0]
cam = Camera(eye, center, up, 120, 1, 0.01, 1000)
# =================================
archer = PLAYER(cam.eye[0],cam.eye[1],cam.eye[2],roty,i,k)
# =================================
x = randrange(-20,20)
alive_enemy = [ENEMY(x , 135)]
died_enemy = []
# ================================
interval = 30

def drawText(string, x, y):
    glLineWidth(2)
    #glColor(1, 1, 0)  # Yellow Color
    glLoadIdentity()  # remove the previous transformations
    glScale(0.13,0.13,1)  # Try this line
    glTranslate(x, y, 0)
    #glRotate(roty ,0,1,0)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN , c)

def charMov(key, x, y):
    global tx
    global tz
    global roty
    global v0

    if key == b"d" :
        cam.translatex(1,deg2rad(roty))

    elif key == b"a":
        cam.translatex(-1,deg2rad(roty))

    if key == b"w":
        cam.translatez(1,deg2rad(roty))

    elif key == b"s":
        cam.translatez(-1,deg2rad(roty))

    if key == b"e" :
        v0 += 1
        #archer.cursor(roty,rotx,v0)
    draw()


def upkey(key,x,y):
    global v0
    if key == b"e" :
        arrows_on_air.append\
            (ARROW(cam.eye[0],cam.eye[1],cam.eye[2],roty,rotx,v0,i,k))
        v0 = 5


def charRot(key, x, y):
    global rotx
    global roty

    if key == GLUT_KEY_RIGHT:
        roty -= 5
        cam.rotatey(deg2rad(roty))

    elif key == GLUT_KEY_LEFT:
        roty += 5
        cam.rotatey(deg2rad(roty))

    if key == GLUT_KEY_UP and rotx < 50 :
        rotx += 5

    elif key == GLUT_KEY_DOWN and rotx > -10:
        rotx -= 5
    draw()


def myinit():
    cam.updateCam()
    glEnable(GL_DEPTH_TEST)
    glClearColor(1, 1, 1, 1)


def timer(z):
    draw()
    glutTimerFunc(interval, timer, 1)


def draw():
    global arrows_on_air
    global alive_enemy
    global arrows_on_ground
    global died_enemy

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # =======render enviroment ==============
    glCallList(obj[3].gl_list)
    glLoadIdentity()
    # =======render & move chracter==========
    archer.player_motion\
    (cam.eye[0],cam.eye[1],cam.eye[2],roty,rotx)

    # =============render arrows===============
    for i in arrows_on_air:
        i.update()
        if i.update() == 1 :
            arrows_on_ground.append(i)
            arrows_on_air.remove(i)
    for i in arrows_on_ground:
        i.update()

    # ===========================
    for e in alive_enemy :
        e.move(archer)
        r = e.arrow_collition(arrows_on_air)
        if  r is not None :
            arrows_on_air.remove(r)
            died_enemy.append(e)
            alive_enemy.remove(e)
            x = randrange(-20,20)
            alive_enemy.append(ENEMY(x , 135))
    # ================= the writing on screen  ===========================
    string = "Score :  " + str(len(died_enemy))
    drawText(string, 10 ,400)
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(1920, 1080)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Archers")
    myinit()
    loadFunc()
    glutDisplayFunc(draw)
    glutTimerFunc(interval,timer,1)
    glutSpecialFunc(charRot)
    glutKeyboardFunc(charMov)
    glutKeyboardUpFunc(upkey)
    glutMainLoop()

main()
