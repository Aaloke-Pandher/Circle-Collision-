# Circle Collision game  
import pygame 
import random  

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
        pygame.draw.ellipse(screen, Blue, [self.x, self.y, self.w, self.h], 2) 

class Food: 
    def __init__(self, x, y, w, h): 
        self.x = x 
        self.y = y 
        self.w = w 
        self.h = h  
    def drawFood(self, screen):   
        randColor = random.randrange(0, 255)
        pygame.draw.ellipse(screen, [randColor, randColor, randColor], [self.x, self.y, self.w, self.h], 2) 
# List of Food 
food = [] 

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
        for i in range(len(food)): 
            if frameCount % 60 == 0:
                wHRan = random.randrange(10, 15)
                food.append(Food(random.randrange(0, 800), random.randrange(0, 600), wHRan, wHRan))
            food[i].drawFood(screen)
        pygame.display.flip()
 
        # --- Limit frames
        clock.tick(60) 
        frameCount += 1

    # Close window
    pygame.quit()  

main()