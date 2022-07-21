import pygame, sys

# General Stuff
pygame.init()
clock = pygame.time.Clock()

screenWidth, screenHeight = 640, 480
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tile Movement")

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)

# Classes
class Tile:
    tile_size = 32
    objs = []
    
    def __init__(self, x, y):
        self.rect = pygame.Rect(x+1, y+1, Tile.tile_size-2, Tile.tile_size-2)
        Tile.objs.append(self)
    
    @classmethod
    def Update(cls, color):
        for obj in cls.objs:
            pygame.draw.rect(screen, color, obj)

class Player:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        
        self.move_delay = 0.1 * 1000 # How much seconds of delay before the player can move again
        self.last_moved = pygame.time.get_ticks()
    
    def Update(self):
        # Stops the player from going outside the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screenWidth:
            self.rect.right = screenWidth
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screenHeight:
            self.rect.bottom = screenHeight
            
        # Draws the instance
        pygame.draw.rect(screen, blue, self)
    
    def Input(self):
        if curTicks - self.last_moved > self.move_delay:
            if event.type == pygame.KEYDOWN:
                self.last_moved = curTicks
                # Moves player left and right
                if event.key == pygame.K_DOWN:
                    self.rect.y += Tile.tile_size
                    print(f"Tile Pos: {int(self.rect.x / Tile.tile_size), int(self.rect.y / Tile.tile_size)}") # Debug
                if event.key == pygame.K_UP:
                    self.rect.y -= Tile.tile_size
                    print(f"Tile Pos: {int(self.rect.x / Tile.tile_size), int(self.rect.y / Tile.tile_size)}")
                # Moves player up and down
                if event.key == pygame.K_RIGHT:
                    self.rect.x += Tile.tile_size
                    print(f"Tile Pos: {int(self.rect.x / Tile.tile_size), int(self.rect.y / Tile.tile_size)}")
                if event.key == pygame.K_LEFT:
                    self.rect.x -= Tile.tile_size
                    print(f"Tile Pos: {int(self.rect.x / Tile.tile_size), int(self.rect.y / Tile.tile_size)}")

# Variables
tile_list = []

player = Player(0, 0, 32, 32)

rows = 15
columns = 20

# Prepares the grid
for row_index in range(columns):
    for col_index in range(rows):
        x = row_index * Tile.tile_size
        y = col_index * Tile.tile_size
        
        tile_list.append(Tile(x, y))

# Game loop
while True:
    # Gets the amount of ingame ticks that have passed
    curTicks = pygame.time.get_ticks()
    # Checks for events like quiting and player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        player.Input()
    
    # This draws everything        
    screen.fill(white)
    
    Tile.Update(black)
    player.Update()
    
    # Updates the screen
    pygame.display.flip()
    clock.tick(60)