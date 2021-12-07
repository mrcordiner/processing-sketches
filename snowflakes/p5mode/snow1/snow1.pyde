from random import randint

mode = 2 # 1 - large, 2 - composite
W,H = 1000,1000

def setup():
    size(1000,1000)
    global nextFrame
    nextFrame = 0

def flake(w,h):
    pushMatrix()

    translate(500,500)

    stroke(randint(200,255),randint(200,255),randint(200,255))
    strokeWeight(2)

    a = randint(30,80)
    b = randint(30,80)
    c = randint(300,700)
    
    r = randint(7,22)
    for n in range(r+1):
    
        line(0,0,0,-w)
        
        line(-a,-b,0,c)
        line(a,-b,0,c)
    
        rotate(radians(360/r))

    popMatrix()
    
def draw():

    global nextFrame
    if frameCount > nextFrame:
        nextFrame = frameCount + 60

        if mode == 1:
            
                background(158, 149, 222)
                flake(W,H)   
                        
        elif mode == 2:
            background(158, 149, 222)
            translate(75,75)
            
            for y in range(0,500,50):
                for x in range(0,500,50):
                    pushMatrix()
                    translate(x*1.5,y*1.5)
                    scale(0.1)
                    flake(x,y)
                    popMatrix()
