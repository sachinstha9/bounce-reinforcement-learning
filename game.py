import pygame 

WIDTH = 1000
HEIGHT = 1000

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.paddleWidth = 100
        self.paddleHeight = 10
        self.paddlePosition = [(WIDTH / 2)- (self.paddleWidth / 2), 800]
        self.paddleColor = WHITE
        self.paddleSpeed = 10

        self.ballSizeRadius = 20
        self.ballPosition = [0, 0]
        self.ballColor = WHITE
        self.ballSpeed = [10, 8]

        self.reset()

    def reset(self):
        self.ballPosition = [0, 0]
        self.paddlePosition = [(WIDTH / 2)- (self.paddleWidth / 2), 700]
    
    def draw(self):
        self.screen.fill(BLACK)

        pygame.draw.rect(self.screen, WHITE, (self.paddlePosition[0], self.paddlePosition[1], self.paddleWidth, self.paddleHeight))

        pygame.display.update()
        self.clock.tick(FPS)

