import pygame
import random

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('car.png')  # Load the car image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_UP]:  # Drive up
            self.rect.y -= 5
        if keys_pressed[pygame.K_DOWN]:  # Drive down
            self.rect.y += 5
        if keys_pressed[pygame.K_LEFT]:  # Drive left
            self.rect.x -= 5
        if keys_pressed[pygame.K_RIGHT]:  # Drive right
            self.rect.x += 5

        # Boundary detection
        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        # self.image = pygame.image.load('ball.png')  # Load the ball image
        self.image = pygame.image.load('ball.png')  # Load the ball image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed

        # Boundary detection and "bounce" back
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed = -self.speed


WIDTH, HEIGHT = 800, 600  # Set the dimensions as per your needs
FPS = 60  # Set frames per second as per your needs

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.sprites = pygame.sprite.Group()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys_pressed = pygame.key.get_pressed()
        self.car.update(keys_pressed)
        
        for sprite in self.sprites:
            if sprite is not self.car:  # For all other sprites, don't pass any extra arguments
                sprite.update()

        # Collision detection
        if pygame.sprite.spritecollideany(self.car, self.sprites):
            print('Collision detected!')

    def render(self):
        self.screen.fill((0, 0, 0))
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def add_sprite(self, sprite):
        self.sprites.add(sprite)

    def set_car(self, car):
        self.car = car


game = Game()

# Add the car
car = Car(100, 100)
game.set_car(car)
game.add_sprite(car)

# Add some balls
for i in range(10):
    ball = Ball(random.randint(0, WIDTH), random.randint(
        0, HEIGHT), random.choice([-5, 5]))
    game.add_sprite(ball)

game.run()

pygame.quit()
