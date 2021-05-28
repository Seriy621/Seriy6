x = 10
y = 10
f = 0
xf = random(0,700)
yf = random(0,700)
score = 0
napravlenije = "вправо"
napravlenije = "влево"
napravlenije = "вверх"
napravlenije = "вниз"
gamemode = 1
def setup():
    size(700,700)
    frameRate(10)
    rectMode(CENTER)
def draw():
    global x, y, napravlenije, xf, yf, gamemode, score, f
    if gamemode == 1:
        background(100)
        fill(255,255,0)
        rect(x,y,20,20)
        fill(0,255,255)
        ellipse(xf,yf,10,10)
        if score >= 1:
            f = f + 1
        if napravlenije == "вправо":
            x = x + 10
        elif napravlenije == "влево":
            x = x - 10
        elif napravlenije == "вверх":
            y = y - 10
        elif napravlenije == "вниз":
            y = y + 10
        if keyPressed:
            if key == "d":
                napravlenije = "вправо"
            elif key == "a":
                napravlenije = "влево"
            elif key == "w":
                napravlenije = "вверх"
            elif key == "s":
                napravlenije = "вниз"
        if abs(x-xf) <= 10 and abs(y-yf) <= 10:
            xf = random(0,700)
            yf = random(0,700)
            score = score + 1
        if x < -1 or x > 700 or y < -1 or y > 700:
            gamemode = 0

    else:
        fill(255)
        text("game over",100,100)   
        text(score,100,115)
