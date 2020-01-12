import pygame
import random
import sys


class GAME():

    def __init__(self, windowSize=[800, 600]):
        # base
        pygame.init()
        self.__windowSize = windowSize
        self.__font = pygame.font.SysFont(None, 30)

        # player
        self.live = 3

        # bat
        self.__batSize = [150, 10]
        self.__batX = 11
        self.__batY = 570
        self.__batS = 0

        # ball
        self.__ballR = 10
        self.__ballX = int(self.__windowSize[0] / 2)
        self.__ballY = int(self.__windowSize[1] / 2)
        self.__ballXS = 1
        self.__ballYS = -1

        self.__buildWindow()
        self.__buildGame()

    def __buildWindow(self):
        self.__screen = pygame.display.set_mode(self.__windowSize)

    def __buildGame(self):
        self.textLive = self.__font.render("Lives: " + str(self.live), True, (0, 255, 255))
        self.__screen.blit(self.textLive, (50, 50))
        pygame.draw.circle(self.__screen, (3, 163, 255), (self.__ballX, self.__ballY), self.__ballR, 0)
        pygame.draw.rect(self.__screen, (255, 255, 255), (self.__batX, self.__batY, self.__batSize[0], self.__batSize[1]), 0)
        pygame.display.flip()

    def __moveBall(self):
        if self.__ballX > 10 and self.__ballX + self.__ballR < self.__windowSize[0] - 10:
            pass
        else:
            self.__ballXS *= -1

        if self.__ballY > 10:
            pass
        else:
            self.__ballYS *= -1

        if self.__ballY + self.__ballR == self.__windowSize[1] - 30 and (self.__ballX > self.__batX and self.__ballX < self.__batX + self.__batSize[0]):
            self.__ballYS = random.randint(-2, -1)
            self.__ballXS = random.randint(-2, 2)
        elif self.__ballY + self.__ballR == self.__windowSize[1] - 30 and (self.__ballX < self.__batX or self.__ballX > self.__batX + self.__batSize[0]):
            return 'reset'
        else:
            pass

        self.__ballX += self.__ballXS
        self.__ballY += self.__ballYS

    def __moveBat(self):
        if self.__batX > 10 and self.__batX + self.__batSize[0] < self.__windowSize[0] - 10:
            pass
        else:
            self.__batS *= -1

        self.__batX += self.__batS

    def __reset(self):
        self.live -= 1
        self.__ballX = int(self.__windowSize[0] / 2)
        self.__ballY = int(self.__windowSize[1] / 2)
        self.__ballXS = 1
        self.__ballYS = -1

    def gameLoop(self):
        while self.live > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.__batS = -1
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.__batS = 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.__batS *= 2

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.__batS /= 2

            self.__screen.fill((0, 0, 0))

            if self.__moveBall() == 'reset':
                self.__reset()
            self.__moveBat()

            self.textLive = self.__font.render("Lives: " + str(self.live), True, (255, 255, 255))
            self.__screen.blit(self.textLive, (10, 10))
            pygame.draw.circle(self.__screen, (3, 163, 255), (self.__ballX, self.__ballY), self.__ballR, 0)
            pygame.draw.rect(self.__screen, (255, 255, 255), (self.__batX, self.__batY, self.__batSize[0], self.__batSize[1]), 0)
            pygame.display.flip()
            pygame.time.wait(5)

        self.__screen.fill((0, 0, 0))
        self.__font = pygame.font.SysFont(None, 70)
        self.textLost = self.__font.render("Game Lost!", True, (255, 255, 255))
        self.__screen.blit(self.textLost, (
            (self.__windowSize[0] - self.textLost.get_width()) / 2,
            (self.__windowSize[1] - self.textLost.get_height()) / 2
        ))

        self.__font = pygame.font.SysFont(None, 20)
        self.textClose = self.__font.render("Press ESC", True, (255, 255, 255))
        self.__screen.blit(self.textClose, (
            (self.__windowSize[0] - self.textLost.get_width()) / 2,
            (self.__windowSize[1] - self.textLost.get_height()) / 2 + 100
        ))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()


game = GAME()

game.gameLoop()
