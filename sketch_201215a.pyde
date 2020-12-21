width=640
height=400
speed=10
radiushero=100
radiusenemy=0
speedenemy=1
counter=-1
xpositionhero=width/2
ypositionenemy=0
xpositionenemy=0

def setup():
    size(width, height)
    frameRate(120)

def draw():
    global ypositionenemy, xpositionhero, xpositionenemy, radiushero, radiusenemy, counter, speedenemy
    background(0)
    fill(255)
    textSize(20)
    text(counter, 30, 175)
    fill(0, 102, 153)
    ellipse(xpositionhero, height-radiushero/2, radiushero, radiushero)
    fill(255, 0, 0)
    if (ypositionenemy>height):
        ypositionenemy=0
        xpositionenemy=random(width)
        radiusenemy=random(10, 60)
        counter=counter+1
    for i in range(height):
        ypositionenemy=ypositionenemy+0.02*speedenemy
        ellipse(xpositionenemy, ypositionenemy, radiusenemy*2, radiusenemy*2)
    if (abs(xpositionhero-xpositionenemy) < (radiushero+radiusenemy)/2) and ((abs(height-radiushero/2) - ypositionenemy) < (radiushero+radiusenemy)/2):
            background(255,0,0)
            counter=-1
            fill(255)
            textSize(70)
            text("Try again!", width/4, height/2)
            
def keyPressed():
    global xpositionhero, ypositionhero, speed
    if (keyCode==39):
        xpositionhero+=speed
    if (keyCode==37):
        xpositionhero-=speed
        
