# image of cover
w=907
h=1360


def setup():
    
    loadFont('static/FiraSans-Light.ttf')
    
    global message, slider

    createP()
    createSpan("Hidden Message: ")
    message = createInput()
    message.attribute('value','Your Message Here')
    
    
    createP()
    createSpan("Refresh Rate: ")
    slider = createSlider(0.1,30,1)
    slider.style('width','100px')
    
    createCanvas(450, 675)
    
def draw():
    frameRate(slider.value())
    
    background(160)
    pushMatrix()
    
    #translate(width-(w/2)-50,40)
    

    fill(255)
    strokeWeight(0)
    rect(0, 0, 973-523, 718-44)
    #(973, 718)
    

    grid(fill_grid())
    
    # title
    fill("#3AF072")
    translate(4,-87)
    textFont('FiraSans-Light')
    textSize(30)
    text("PERMUTATION CITY",0,0)

    textSize(22)
    #textFont(author_font,22)
    text("GREG EGAN",0,25)#30
    
    #textFont(author_font,18)
    textSize(18)
    text("A NOVEL",0,550)#30
    
    popMatrix()
    
   
    
    



def grid(letter_grid):
    #print(letter_grid)
    translate(25,150)
    fill(255)
    strokeWeight(1)
    cell_w = ((w/2)-40)/16
    cell_h = ((w/2)-40)/16 * 0.95
    
    #textFont(author_font,16)
    
    # grid
    x,y = 0,0
    for row in range(16):
        x=0
        for col in range(16):
    
            if type(letter_grid[row][col]) != type(42): # aka int - but p5 has reused that name
                fill(50,50,250)
                rect(x,y,cell_w,cell_h)
                fill(0)
                text(letter_grid[row][col], x+cell_w/2-4, y+cell_h/2+6)
            else:
                fill(255)                
                rect(x,y,cell_w,cell_h)    
                fill(0)        
                text(chr(letter_grid[row][col]), x+cell_w/2-4, y+cell_h/2+6)
                
            x+=cell_w
        y+=cell_h

    

def fill_grid():
    
    
    title = message.value().upper()
    
    
    i = 0
    r,c = 0,0
    
    grid = [ [0]*16 for n in range(16)]
    
    while True:
        if i<len(title) and int(random(1,16**2/len(title))) == 1:
            grid[r][c] = title[i]
            i+=1
        else:
            if int(random(0,26))==0:
                grid[r][c] = 32
            else:
                grid[r][c] = 64+int(random(1,26))
                
        c+=1
        
        # move through grid
        if c==16:
            c=0
            r+=1
            if r==16:
                break
    return(grid)
    # 
    
    