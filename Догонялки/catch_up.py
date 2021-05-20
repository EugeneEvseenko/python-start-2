from pygame import *
 
window = display.set_mode((700, 500))
display.set_caption("Догонялки")
background = image.load("background.png")
 
#данные о спрайте-картинке
x1 = 100
y1 = 300
 
x2 = 300
y2 = 300
 
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
 
#игровой цикл
run = True
 
while run:
    window.blit(background,(0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    display.update()
