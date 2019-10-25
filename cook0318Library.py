# This function takes the input of a circles radius (r), and uses pi from Python's math module to return the variable a, which 
# is the area of a circle. In my testdriver I prompted the user for the required input and output a simple sentence delcaring the area.

from math import pi
def calculateAreaOfCircle(r):
    a = round((pi * r **2), 2)
    return(a)


# This function takes the input of a vehicles miles driven (m) and gallons of fuel used (g) and computes the variable MPG, which is the 
# vehicles Miles Per Gallon.  In my testdriver I prompted the user for the required inputs and output a simple sentence delcaring the MPG.
def calculateMpg(m, g):
    MPG = round((m / g), 2)
    return(MPG)

# This function takes the input of the temperature in degrees Fahrenheit(f) and converts it into variable c, which is degrees Celsius.
#  In my testdriver I prompted the user for the required input and output a simple sentence delcaring the new temperature.
def convertFahrenheitToCelsius(f):
    c = (round(((f - 32) * (5/9)), 2))
    return(c)

# This function takes the input in the form of two coordinates (x,y) and (x1,y1) and computes the distance (d) between them.
# In my testdriver I prompted the user for the required inputs and output a simple sentence delcaring the distance.
from math import sqrt
def calculateDistanceBetweenPoints(x,y,x1,y1):
    d = round((sqrt((x1-x)**2 + (y1-y)**2)), 2)
    return(d)

# This function creates a verticle line on the Rasperry Pi's GFXHAT at a user-given X-Coordinate.
from gfxhat import lcd

def vertLine (x,y):
    while (y < 63):
        lcd.set_pixel(x,y,1)
        lcd.show()
        y = y + 1

# This function creates a horizontal line on the Rasperry Pi's GFXHAT at a user-given Y-Coordinate.
from gfxhat import lcd

def horizLine(x,y):
    while (x < 128):
        lcd.set_pixel(x,y,1)
        lcd.show()
        x = x + 1

# This function creates a staircase pattern on the Rasperry Pi's GFXHAT using a user-given starting (x,y) coordinate, 
# the step's height and width, and which direction the stairs will go.
from gfxhat import lcd

def stairs(a,b,i,j,choice):
    if choice == 1:
        while (a + i <= 127) and (b + j <= 63):
            for a in range(a, a + i):
                lcd.set_pixel(a,b,1)
                lcd.show()
            for b in range(b,b+j):
                lcd.set_pixel(a,b,1)
                lcd.show()
        if (a + i >= 127):
            for a in range(a,127):
                lcd.set_pixel(a,b,1)
                lcd.show()
        elif (b + j >= 63):
            for a in range(a,a + i):
                ldc.set_pixel(a,b,1)
                lcd.show()
            for b in range(b, 63):
                lcd.set_pixel(a,b,1)
                lcd.show()

    elif choice == 2:
        while (a - i >= 0) and (b + j <= 127):
            for a in range(a-i,a):
                lcd.set_pixel(a,b,1)
                lcd.show()
            for b in range(b,b+j):
                lcd.set_pixel(a-i,b,1)
                lcd.show()
            a = a-i
        if (a - i <= 0):
            for a in range(0,a):
                lcd.set_pixel(a,b,1)
                lcd.show()
        elif (b + j >= 63):
            for b in range(b, 63):
                lcd.set_pixel(a,b,1)
                lcd.show()

    elif choice == 3:
        while (a + i <= 127) and (b - j >= 0):
            for a in range(a, a + i):
                lcd.set_pixel(a,b,1)
                lcd.show()
            for b in range(b-j,b):
                lcd.set_pixel(a,b,1)
                lcd.show()
            b = b - j

        if (b - j <= 0):
            for b in range(0, b):
                lcd.set_pixel(a,b,1)
                lcd.show()
        elif (a + i >= 127):
            for a in range(a,127):
                lcd.set_pixel(a,b,1)
                lcd.show()

    elif choice == 4:
        while (a - i >= 0) and (b - j >= 0):
            for a in range(a-i,a):
                lcd.set_pixel(a,b,1)
                lcd.show()
            for b in range (b-j,b):
                lcd.set_pixel(a-i,b,1)
                lcd.show()
            if a - i <= 0:
                for a in range(0,a):
                    lcd.set_pixel(a,b,1)
            if b - j <= 0:
                for b in range (b-j,b):
                    lcd.set_pixel(a-i,b,1)
                    lcd.show()
            a = a - i
            b = b - j

# This function displays a radom pixel on the GFXHAT screen for a specified number of seconds. 
# The inputs are the length of time each pixel lasts on the screen for, and how long the whole function will run for.
from gfxhat import lcd
import random
import time

def randPixel(pixelDuration,functionDuration):
    endTime = time.time() + functionDuration
    while (time.time() < endTime):
        a = random.randint(0,127)
        b = random.randint(0,63)
        lcd.set_pixel(a,b,1)
        lcd.show()
        time.sleep(pixelDuration)
        lcd.clear()
    lcd.clear()
    lcd.show()

# This function clears the backlight on the GFXHAT.
# It does not take any inputs.
from gfxhat import backlight

def clearBacklight():
    backlight.set_all(0,0,0)
    backlight.show()


# This function creates a bouncing ball on the GFXHAT.
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