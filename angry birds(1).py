from cmath import rect

def rect():
    rect(0,350,400,150,fill='green')
    rect(0,0,400,350,fill=gradient('lightSkyBlue','deepSkyBlue',start='top'))
#clouds
def circle():
    circle(33,60,20,fill='white',border='gainsboro')
    circle(50,40,20,fill='white',border='gainsboro')
    circle(67,60,30,fill='white',border='gainsboro')
    rect(30,45,50,30,fill='white')
    circle(183,100,30,fill='white',border='gainsboro')
    circle(200,80,20,fill='white',border='gainsboro')
    circle(217,100,30,fill='white',border='gainsboro')
    rect(180,75,40,40,fill='white')

#birds
def bird(x,y):
    circle(x,y,20,fill='red')
    circle(x+5,y-5,5,fill='white',border='black')
    circle(x+8,y-5,2,fill='black')
bird(100,90)
def target(x,y):
    circle(x,y,20,fill="lightgreen")
target(200,330)
def check(birds,targets):
    for target in targets:
        if target.active:
            dx=bird.X-target.X
            dy=bird.Y-target.Y
            distance=math.sqrt(dx^2+dy^2)
            if distance<bird.radius+target.radius:
                target.active=False
                return True
    return False
slingshot_pos=(100,height-100)
bird=Bird()



while running:
    for event in pygame.event.get():
        if event.type==pygame.quit:
            running=False
        elif event.type==pygame.mousebuttondown:
            if not bird.fired:
                mouse_pos=pygame.mouse.get_pos()
                distance=math.hypot(mouse_pos[0]-bird.X,mouse_pos[1]-bird.Y)
                if distance<bird.radius:
                    dragging=True
        elif event.type==pygame.mousebuttonup:
            if dragging and not bird.fired:
                dragging=False
                bird.fired=True
                dx=slingshot_pos[0]-bird.X
                dy=slingshot_pos[1]-bird.Y
                bird.vel_X=dx*0.2
                bird.vel_Y=dy*0.2
                
                
if bird.fired:
    bird.vel_X+=GRAVITY
    bird.X+=bird.vel_X
    bird.Y+=bird.vel_Y
    if bird.X>400 or bird.Y<0:
        bird.reset()