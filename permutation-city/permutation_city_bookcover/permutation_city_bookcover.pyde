add_library('pdf')
PDF_MODE = False

from random import randint

# image of cover
w=907
h=1360

def book_cover(msg):
    pushMatrix()
    fill(255)
    strokeWeight(2)
    rect(0, 0, 973-523, 718-44)
    #(973, 718)
    

    grid(fill_grid(msg))

    # title
    # title 177, 127,82
    fill(231,127,57)
    translate(4,-87)
    textFont(title_font,30)
    textAlign(LEFT);
    
    text("PERMUTATION CITY",0,0)

    textFont(author_font,22)
    text("GREG EGAN",0,27)#30
    
    textFont(author_font,18)
    text("A NOVEL",0,550)#30
    
    popMatrix()
        
            
            
def setup():
    size(1375,1063)
     # fit on screen
    # 8.5 x 11 at 150
    # 1063 x 1375

    
    if PDF_MODE:
        frameRate(4)
        pdf = (PGraphicsPDF)
        beginRecord(PDF, "test.pdf");
    
    # load data
    global title_font, author_font, grid_font
    title_font = createFont("Spartan/static/Spartan-Medium.ttf", 30)    
    author_font = createFont("Spartan-Regular.ttf", 22)    
    grid_font = createFont("Spartan-Regular.ttf", 14)    
    
    global cover
    cover = loadImage("permutation_cover.jpeg")
        
def draw():
    scale(0.7)
    fill(255)
    stroke(100)
    rect(0,0,1375,1063)
    
    #translate(width-(w/2)-50,40)
    #book_cover()

    translate(110,200)
    book_cover("MESSAGE HERE")
    translate(700,0)
    book_cover("TESTING 1,2,3...")
    
    if PDF_MODE:
        endRecord()
        exit()
    noLoop()

    
def mousePressed():
    print((mouseX,mouseY))



def grid(letter_grid):
    print(letter_grid)
    translate(25,150)
    fill(255)
    strokeWeight(1)
    cell_w = ((w/2)-40)/16
    cell_h = ((w/2)-40)/16 * 0.95
    
    textFont(grid_font,14)
    textAlign(CENTER)
    
    # grid
    x,y = 0,0
    for row in range(16):
        x=0
        for col in range(16):
    
            if type(letter_grid[row][col]) != int:
                fill(80,123,187)
                # filled_grid_colour = (80, 177, 187)

                rect(x,y,cell_w,cell_h)
                fill(0)
                text(letter_grid[row][col], x+cell_w/2, y+cell_h/2+6)
            else:
                fill(255)                
                rect(x,y,cell_w,cell_h)    
                fill(0)        
                text(chr(letter_grid[row][col]), x+cell_w/2, y+cell_h/2+6)
                
            x+=cell_w
        y+=cell_h

    

def fill_grid(msg):
    
    i = 0
    r,c = 0,0
    
    grid = [ [0]*16 for n in range(16)]
    
    while True:
        if i<len(msg) and randint(1,16**2/len(msg)-2) == 1:
            grid[r][c] = msg[i]
            i+=1
        else:
            if randint(1,26)==0:
                # add a space
                grid[r][c] = 32
            else:
                # add random capital letter
                grid[r][c] = 64+randint(1,26)
                
        c+=1
        
        # move through grid
        if c==16:
            
            # blank 
            while True:
                b = randint(0,15)
                if type(grid[r][b]) == int:
                    grid[r][b] = 0
                    break
        
            
            c=0
            r+=1
            if r==16:
                break
    return(grid)
    # 
    
    
    
def book_cover2():
    pushMatrix()
    # 907,1360
    scale(0.5)
    image(cover,0,0)
    popMatrix()
