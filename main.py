# Circle Collision game  
import pygame 
import random  
import math

# Define colors 
Grey = [128, 128, 128] 
White = [255, 255, 255] 
Blue = [0, 0, 255]  
Red = [255, 0, 0] 
Green = [0, 255, 0] 

# Player class 
class Player:
    def __init__(self, x, y, w, h):
        self.x = x 
        self.y = y 
        self.w = w 
        self.h = h 
        self.xspeed = 5 
        self.yspeed = 5  
    def drawPlayer(self, screen): 
        pygame.draw.ellipse(screen, Blue, [self.x, self.y, self.w, self.h]) 
        

class Food: 
    def __init__(self, x, y, w, h, c): 
        self.x = x 
        self.y = y 
        self.w = w 
        self.h = h   
        self.c = c
    def drawFood(self, screen):   
        pygame.draw.ellipse(screen, self.c, [self.x, self.y, self.w, self.h], 2) 
# List of Food 
food = []   

# Find mouse 
def mouse_position():
    pos = pygame.mouse.get_pos() 
    mouse_x = pos[0]
    mouse_y = pos[1]
    return mouse_x, mouse_y   

# Player follow mouse 
def follow_object(ob2, speed):  
    run = (mouse_position()[0] - ob2.x) 
    rise = (mouse_position()[1] - ob2.y) 
    d = math.sqrt(rise**2 + run**2)
    dy = (speed * rise) / d 
    dx = (speed * run) / d 
    ob2.x += dx 
    ob2.y += dy
    return dx, dy 



# Collision Function 
def rectCollision(rect1, rect2): 
   if rect1.x < rect2.x + rect2.w and rect1.y < rect2.y + rect2.h and rect1.x + rect1.w > rect2.x and rect1.y + rect1.h > rect2.y:
        return 1
player = Player(400, 300, 20, 20)
# Main function 
def main():
    pygame.init() 
    # Canvas
    size = (800, 600)
    screen = pygame.display.set_mode(size) 
    frameCount = 1
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # Main Program Loop 
    while not done:
        # Main event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True  
    
        # Draw 
        screen.fill(White) 
        player.drawPlayer(screen)  
        follow_object(player, 2)  
        if frameCount % 60 == 0: 
            randColor = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]
            wHRan = random.randrange(10, 15)
            food.append(Food(random.randrange(0, 800), random.randrange(0, 600), wHRan, wHRan, randColor)) 
        for i in range(len(food)): 
            food[i].drawFood(screen) 
            if rectCollision(food[i], player) == 1:
                player.w = 1/8 * food[i].w + player.w
                player.h = 1/8 * food[i].h + player.h 
                food.pop(i)
                break 
        pygame.display.flip()
 
        # --- Limit frames
        clock.tick(60) 
        frameCount += 1

    # Close window
    pygame.quit()  

main()