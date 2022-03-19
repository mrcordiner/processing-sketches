def half_sin_wave(amp,w,wave_len):
    noFill()
    stroke(255)
    strokeWeight(1.3)
    l=180*wave_len
    dx = w/float(l)
     
    px,py = 0,0

    for i in range(l):
        h = sin(radians(i))*amp
        line(dx*i, py-h,px,py-h)
        line(dx*i, -py+h,px,-py+h)
        
        px,py = (dx * i, py)    
    

        
size(1350,1350)
#size(675,675)
background(20)
smooth()
scale(2)
translate(270/2,30)

fill(0)
rect(0,0,420,630)

fill(255)
f_title = createFont('Playfair_Display/static/PlayfairDisplay-Bold.ttf',48)
f_subtitle = createFont('Inter/static/Inter-Black.ttf', 14)

textFont(f_title)
text("Music by", 35,50)
text("the Numbers", 35, 105)

textSize(32)
text("Eli Maor", 240, 590)

textFont(f_subtitle)
text("FROM  PYTHAGORAS",40,573)
text("TO SCHOENBERG",40,593)

translate(40,130)
rotate(radians(90))

scale(1)
for n in range(1,17): # 17
    #def half_sin_wave(amp,w,wave_len,py):
    # amplitude, length (height), freq
    half_sin_wave( 5,400,n)
    translate(0,-600/28)
    # (600 / 16 * n) + 10
    
save("music.png")
