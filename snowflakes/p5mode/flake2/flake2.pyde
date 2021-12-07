
from random import randint, choice, random


mode = 1 # 1 - large, 2 - composite
W,H = 1000,1000
ANIMATE = True

NEXTFRAME = 60 # number of frames till redraw

def setup():
    size(1000,1000)
    
    # GUI element

    
    
    # for timing animations
    global nextFrame
    nextFrame = NEXTFRAME

    
def draw():

    global nextFrame
    
    nextFrame-=1
    if nextFrame==0 or not ANIMATE:
        nextFrame = NEXTFRAME

        if mode == 1:
            
                background(158, 149, 222)
                
                #rect(100,100,100,10)
                
                line(500,0,500,1000)
                line(0,500,1000,500)
                arrow_flake()   
                
                                                    
        elif mode == 2:
            background(158, 149, 222)
            translate(75,75)
            
            for y in range(0,500,70):
                for x in range(0,500,70):
                    pushMatrix()
                    translate(x*1.5,y*1.5)
                    scale(0.1)
                    arrow_flake()
                    popMatrix()
                    
        if not ANIMATE:
            noLoop()
            

            
                        
def display(x,y,info):
    pushMatrix()
    translate(x,y)
    
    dy = 20
    y = 0
    
    for item in info:
        y += dy
        text_str = "%s %s" % (item[0],item[1])
        text(text_str, 0,y)                      
    popMatrix()                                    
                                                                        
def arrow_flake():
    # assume size of 1000 and scale accordingly
    # start in middle
    translate(500,500)
    
    pushMatrix()
    
    # some styles
    end_cap = choice([PROJECT,ROUND])
    wide_stroke = map(random()*20,0,20,10,20)
    light_stroke = map(random()*8,0,8,7,8)
        
    # number of branches
    branches = choice([6,8])
    
    # lengths of stuff
    y_h = randint(150,450)
    leafs = randint(2,5)
    leaf_len = randint(80,160)
    leaf_alpha = randint(30,50)
    
    info = [('end_cap', end_cap),
            ('wide_stroke', wide_stroke),
            ('light_stroke', light_stroke),
            ('branches', branches),
            ('y_h', y_h),
            ('leafs', leafs),
            ('leaf_len', leaf_len),
            ('leaf_alpha', leaf_alpha)]
    
    
    
    # main line style
    stroke(randint(200,255),randint(200,255),randint(200,255))
    strokeCap(end_cap)
    
    # branches
    for _ in range(branches):
        strokeWeight(wide_stroke)

        # main branch
        line(0,0,0,-y_h)
        
        # leaves
        pushMatrix()
        for _ in range(leafs):
            translate(0,-y_h/leafs)
            pushMatrix()
            rotate(-leaf_alpha)
            strokeWeight(light_stroke)
            line(0,0,0,leaf_len)
                        
            popMatrix()
            
            pushMatrix()
            rotate(leaf_alpha)
            strokeWeight(light_stroke)
            line(0,0,0,leaf_len)
            popMatrix()
        
        popMatrix()
        
        #break
        rotate(radians(360/branches))
        
    rotate(radians(360/branches))
    popMatrix()
    
    fill(0)
    #rect(-10,-10,20,20)
    
    # middle can be a shape or intersecting lines
    if 0 == 0:
        # little flower shape
        # was suppose to be a hexagon
        # 
        pushMatrix()
        
        s = createShape()
        s.beginShape()
        s.fill(0, 0, 0)
        s.noStroke()
        s.vertex(-50, 0)
        for _ in range(branches):
            s.vertex(50, 0)
            line(-50,0,50,0)
            rotate(radians(360/branches))
        s.endShape(CLOSE)
        shape(s, -25, -25)
                    
        popMatrix()
        
    display(-400,-400,info)
    
