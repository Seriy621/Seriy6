x = 0
y = 0
rore = 0
def setup():
    size(200,200)
    
def draw():
    global x, y, rore
    ellipseMode(CORNER)
    if key == '7':
        rore = 1
    if key == '8':
        rore = 0
    if rore == 0:
        rect(x,y,10,10)
    else:
        ellipse(x,y,10,10)
    
def keyPressed():
    global x, y, rore
    if key == CODED:
        if keyCode == UP:
            y = y - 10
        if keyCode == DOWN:
            y = y + 10
        if keyCode == RIGHT:
            x = x + 10
        if keyCode == LEFT:
            x = x - 10
    if key == '1':
        fill(255,0,0)
    if key == '2':
        fill(0,255,0)
    if key == '3':
        fill(0,0,255)
    if key == '4':
        fill(0)
    if key == '5':
        fill(255)
    if key == '6':
        fill(random(0,255),random(0,255),random(0,255))


    
    
    
        
        


        
        
    
    
