import pygame
import random
import sys

# Initialize the Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_GAP = 150
PIPE_SPEED = 4
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
PIPE_WIDTH = 70
PIPE_HEIGHT = 500
GROUND_HEIGHT = 100

# Load images
BIRD_IMAGE = pygame.image.load('bird.png')
PIPE_IMAGE = pygame.image.load('pipe.png')
BACKGROUND_IMAGE = pygame.image.load('background.png')
GROUND_IMAGE = pygame.image.load('ground.png')

# Resize images
BIRD_IMAGE = pygame.transform.scale(BIRD_IMAGE, (BIRD_WIDTH, BIRD_HEIGHT))
PIPE_IMAGE = pygame.transform.scale(PIPE_IMAGE, (PIPE_WIDTH, PIPE_HEIGHT))
GROUND_IMAGE = pygame.transform.scale(GROUND_IMAGE, (SCREEN_WIDTH, GROUND_HEIGHT))

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def draw(self, screen):
        screen.blit(BIRD_IMAGE, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)

class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - GROUND_HEIGHT)
        self.top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT)
        self.scored = False  # Add this line


    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        screen.blit(PIPE_IMAGE, (self.x, self.height - PIPE_HEIGHT))
        screen.blit(pygame.transform.flip(PIPE_IMAGE, False, True), (self.x, self.height + PIPE_GAP))

    def off_screen(self):
        return self.x < -PIPE_WIDTH

def check_collision(bird, pipes):
    for pipe in pipes:
        if bird.get_rect().colliderect(pipe.top_rect) or bird.get_rect().colliderect(pipe.bottom_rect):
            return True
    if bird.y <= 0 or bird.y >= SCREEN_HEIGHT - GROUND_HEIGHT:
        return True
    return False

def main():
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    running = True

    while running:
        screen.blit(BACKGROUND_IMAGE, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        bird.update()

        if check_collision(bird, pipes):
            running = False

        if pipes[-1].x < SCREEN_WIDTH // 2:
            pipes.append(Pipe())

        pipes = [pipe for pipe in pipes if not pipe.off_screen()]

        for pipe in pipes:
            pipe.update()
            pipe.draw(screen)

            # Score increment logic
            if not pipe.scored and pipe.x + PIPE_WIDTH < bird.x:
                score += 1
                pipe.scored = True  # Mark this pipe as scored

        bird.draw(screen)

        screen.blit(GROUND_IMAGE, (0, SCREEN_HEIGHT - GROUND_HEIGHT))

        score_surface = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_surface, (10, 10))

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()
