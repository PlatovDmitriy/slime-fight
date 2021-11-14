from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x_cor, y_cor,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.player_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        self.rect.x += self.player_speed
        platforms_touched = sprite.spritecollide(self, wallsg, False)
        
        if self.player_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
            
        elif self.player_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)


class Walls(sprite.Sprite):
    def __init__(self,name,cor_x, cor_y ):
        super().__init__ ()
        self.image = transform.scale(image.load(name),(65,65))
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
wallsg = sprite.Group()
wall1 = Walls('player.png',65,0)
clock = time.Clock()
finish = False
game = True
w = 1900
h = 1100
FPS = 120
n = 1
window = display.set_mode((0,0),FULLSCREEN)
background = transform.scale(image.load('background.png'),(w,h))
player = Player('player.png', 112,215,15)
player.player_speed = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_a:
                player.player_speed = -15
            elif e.key == K_d:
                player.player_speed = 15
        elif e.type == KEYUP:
            if e.key == K_a:
                player.player_speed = 0
            elif e.key == K_d:
                player.player_speed = 0
        if e.type == KEYDOWN:
            if e.key == K_n and n == 1:
                window = display.set_mode((0,0),RESIZABLE)      
                n = 0                                               
            elif e.key == K_n and n == 0:
                window = display.set_mode((0,0),FULLSCREEN)
                n = 1
    if finish != True:
        window.blit(background,(0,0))
        player.reset()
        player.update()
        display.update() 
    clock.tick(FPS)