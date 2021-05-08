x = 0
y = 0
xf = random(0,300)
yf = random(0,300)
napravlenije = "вправо"
napravlenije = "влево"
napravlenije = "вверх"
napravlenije = "вниз"
gamemode = 1
def setup():
    size(300,300)
    frameRate(5)
def draw():
    global x, y, napravlenije, xf, yf, gamemode
    if gamemode == 1:
        background(100)
        fill(255,158,181)
        rect(x,y,5,5)
        fill(0,255,0)
        ellipse(xf,yf,5,5)
    
        if napravlenije == "вправо":
            x = x + 5
        elif napravlenije == "влево":
            x = x - 5
        elif napravlenije == "вверх":
            y = y - 5
        elif napravlenije == "вниз":
            y = y + 5
        if keyPressed:
            if key == "d":
                napravlenije = "вправо"
            elif key == "a":
                napravlenije = "влево"
            elif key == "w":
                napravlenije = "вверх"
            elif key == "s":
                napravlenije = "вниз"
        if abs(x-xf) <= 5 and abs(y-yf) <= 5:
            xf = random(0,300)
            yf = random(0,300)
        
        if x < -1 or x > 300 or y < -1 or y > 300:
            gamemode = 0
            
    else:
        text("game over",150,150)   
        
    
    
    
            
            
                
        
    
            
    
    
