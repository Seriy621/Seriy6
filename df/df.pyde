x = 5
y = 5
xf = random(0,200)
yf = random(0,200)
score = 0
napravlenije = "вправо"
napravlenije = "влево"
napravlenije = "вверх"
napravlenije = "вниз"
gamemode = 1
def setup():
    size(200,200)
    frameRate(10)
    rectMode(CENTER)
def draw():
    global x, y, napravlenije, xf, yf, gamemode, score
    if gamemode == 1:
        background(100)
        fill(255,168,181)
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
            xf = random(0,200)
            yf = random(0,200)
            score = score + 1
        if x < -1 or x > 200 or y < -1 or y > 200:
            gamemode = 0
            
    else:
        text("game over",100,100)   
        text(score,100,115)
        
       
