import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Racer: Velocity Cars")

# Colors
BLACK = (0, 0, 0)
NEON_BLUE = (0, 255, 255)
NEON_PINK = (255, 20, 147)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)

# Font
font = pygame.font.Font(None, 36)


class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(NEON_PINK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)
        self.speed = 5

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed
        if direction == "right" and self.rect.right < WIDTH:
            self.rect.x += self.speed


class EnemyCar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(NEON_BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()


class Road:
    def __init__(self):
        self.y = 0
        self.speed = 5
        self.lane_width = 10

    def update(self):
        self.y += self.speed
        if self.y >= HEIGHT:
            self.y = 0

    def draw(self, surface):
        # Draw road
        pygame.draw.rect(surface, GRAY, (0, 0, WIDTH, HEIGHT))

        # Draw lanes
        lane_spacing = WIDTH // 4
        for i in range(1, 4):
            start_pos = (i * lane_spacing, self.y)
            end_pos = (i * lane_spacing, self.y - HEIGHT)
            pygame.draw.line(surface, WHITE, start_pos, end_pos, self.lane_width)

            start_pos = (i * lane_spacing, self.y + HEIGHT)
            end_pos = (i * lane_spacing, self.y)
            pygame.draw.line(surface, WHITE, start_pos, end_pos, self.lane_width)


# Game objects
player = PlayerCar()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
enemy_cars = pygame.sprite.Group()
road = Road()

# Game variables
score = 0
spawn_timer = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")

    # Spawn new enemy cars
    spawn_timer += 1
    if spawn_timer >= 60:
        spawn_timer = 0
        lane = random.randint(0, 3)
        x_pos = (lane * WIDTH // 4) + (WIDTH // 8) - 20
        new_car = EnemyCar(x_pos, -60)
        enemy_cars.add(new_car)
        all_sprites.add(new_car)

    # Update
    all_sprites.update()
    road.update()

    # Collision detection
    if pygame.sprite.spritecollide(player, enemy_cars, False):
        running = False

    # Update score
    score += 1

    # Draw
    road.draw(screen)
    all_sprites.draw(screen)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Refresh display
    pygame.display.flip()

    # Control game speed
    clock.tick(60)

# Quit the game
pygame.quit()