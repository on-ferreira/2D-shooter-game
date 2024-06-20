import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
ENEMY_SIZE = 50
BULLET_SIZE = 5
PLAYER_COLOR = (0, 0, 255) #RGB code for BLUE
ENEMY_COLOR = (255, 0, 0) #RGB code for RED
BULLET_COLOR = (0, 255, 0) #RGB code for GREEN
BACKGROUND_COLOR = (0, 0, 0)  #RGB code for BLACK
FPS = 60

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Shooter Game")
clock = pygame.time.Clock()

# Font setup
font = pygame.font.SysFont(None, 36)

# Classes
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2, HEIGHT-PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = 5

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.rect.x = max(0, min(WIDTH - PLAYER_SIZE, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - PLAYER_SIZE, self.rect.y))

    def draw(self):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BULLET_SIZE, BULLET_SIZE)
        self.speed = 7

    def update(self):
        self.rect.y -= self.speed

    def draw(self):
        pygame.draw.rect(screen, BULLET_COLOR, self.rect)

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH-ENEMY_SIZE), 0, ENEMY_SIZE, ENEMY_SIZE)
        self.speed = 3

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, ENEMY_COLOR, self.rect)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Game setup
player = Player()
bullets = []
enemies = []
score = 0
running = True

# Game loop
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Bullet(player.rect.centerx, player.rect.top)
            bullets.append(bullet)

    # Player movement
    keys = pygame.key.get_pressed()
    dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
    player.move(dx, dy)

    # Update bullets
    for bullet in bullets[:]:
        bullet.update()
        if bullet.rect.y < 0:
            bullets.remove(bullet)

    # Update enemies
    if random.random() < 0.02:
        enemies.append(Enemy())
    for enemy in enemies[:]:
        enemy.update()
        if enemy.rect.y > HEIGHT:
            enemies.remove(enemy)

    # Check collisions
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.rect.colliderect(enemy.rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break
    for enemy in enemies[:]:
        if enemy.rect.colliderect(player.rect):
            running = False

    # Draw everything
    screen.fill(BACKGROUND_COLOR)
    player.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()

    # Draw score
    draw_text(f'Score: {score}', font, (255, 255, 255), screen, 10, 10)

    pygame.display.flip()

pygame.quit()
