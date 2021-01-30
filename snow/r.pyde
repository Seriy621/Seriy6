y = [10,9,20,48,59,28,32]
x = [14,35,20,8,57,90,150]
s = [10,9,20,48,59,28,32]
def setup():
    size(300,300)
    frameRate(10)
def draw():
    background(0)

    for i in range(7):
        stroke(255)
        strokeWeight(10)
        point(x[i],y[i])
        y[i] = y[i] + s[i]
