# necessary imports
from gfxhat import lcd 
from gfxhat import backlight
import time
import random 

# function to draw object
def displayObj(obj,x,y):
    c = 0
    while c <= len(obj) - 1:
        w = 0
        while w <= len(obj[c]) - 1:
            if obj[c][w] == 1:
                lcd.set_pixel(x,y,1)
                w += 1
                x += 1
            else:
                w += 1
                x += 1
                continue
        x = x - len(obj[c])
        y += 1
        c += 1
    lcd.show()

# function to erase object
def eraseObject(obj,x,y):
    c = 0
    while c <= len(obj) - 1:
        w = 0
        while w <= len(obj[c]) - 1:
            if obj[c][w] == 1:
                lcd.set_pixel(x,y,0)
                w += 1
                x += 1
            else:
                w += 1
                x += 1
                continue
        x = x - len(obj[c])
        y += 1
        c += 1
    lcd.show()

# function to 'move' object
def moveObject(obj,x,y,vx,vy):
    x = x + vx
    y = y + vy
    return x,y
    
# function to check if object cannot travel any further, and if so, changes it's directory
def checkCollision(obj,x,y,vx,vy,Sx,Sy):
    if y >= Sy:
        if y >= Sy and x >= Sx:
            vy = -(vy)
            vx = -(vx)
        elif y >= Sy and x <= abs(vx):
            vy = -(vy)
            vx = -(vx)
        else:
            vy = -(vy)
        return vx,vy

    if y <= abs(vy):
        if y <= abs(vy) and x >= Sx:
            vy = -(vy)
            vx = -(vx)
        elif y <= abs(vy) and x <= abs(vx):
            vy = -(vy)
            vx = -(vx)
        else:
            vy = -(vy)
        return vx,vy

    if x >= Sx:
        if x >= Sx and y >= Sy:
            vy = -(vy)
            vx = -(vx)
        elif x >= Sx and y <= abs(vy):
            vy = -(vy)
            vx = -(vx)
        else:
            vx = -(vx)
        return vx,vy

    if x <= abs(vx):
        if x <= abs(vx) and y <= abs(vy):
            vy = -(vy)
            vx = -(vx)
        if x <= abs(vx) and y >= Sy:
            vy = -(vy)
            vx = -(vx)    
        else:
            vx = -(vx)
        return vx,vy
    return vx,vy

# extra function to change background color
def randBackground():
    a = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)
    backlight.set_all(a,b,c)
    backlight.show()

# main function that calls all previous functions, and also delays transitioning between object locations        
def bounceObj(x,y,vx,vy):  
    g = 0
    while g == 0:
        # randBackground()
        g += 1
    while g != 0:
        displayObj(obj,x,y)
        time.sleep(t)
        eraseObject(obj,x,y)
        x,y = moveObject(obj,x,y,vx,vy)
        vx,vy = checkCollision(obj,x,y,vx,vy,Sx,Sy)

# object variable
ball =  [
[0,0,0,1,1,0,0,0],
[0,0,1,1,1,1,0,0],
[0,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[0,0,1,1,1,1,0,0],
[0,0,0,1,1,0,0,0]
]

obj = ball

# variables to be set/altered
x = 30
y = 30
vx = 4
vy = 4
Sx = 128 - len(obj[0]) - abs(vx)
Sy = 64 - len(obj) - abs(vy)
t = 0.2

# main function call 
bounceObj(x,y,vx,vy)
