import pygame
import math
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep

class BoxesGame(ConnectionListener):
    def __init__(self):
        # 1
        pygame.init()
        pygame.font.init()
        width, height = 389, 489
        self.turn = True
        self.me = 0
        self.otherplayer = 0
        self.didiwin = False
        self.Connect()

        self.gameid = None
        self.num = None

        # 2
        # initialize the screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Boxes")
        # 3
        # initialize pygame clock
        self.clock = pygame.time.Clock()
        self.boardh = [[False for x in range(6)] for y in range(7)]
        self.boardv = [[False for x in range(7)] for y in range(6)]
        self.owner = [[0 for x in range(6)] for y in range(6)]

        self.initGraphics()

    def drawBoard(self):
        for x in range(6):
            for y in range(7):
                if not self.boardh[y][x]:
                    self.screen.blit(self.normallineh, [(x) * 64 + 5, (y) * 64])
                else:
                    self.screen.blit(self.bar_doneh, [(x) * 64 + 5, (y) * 64])
        for x in range(7):
            for y in range(6):
                if not self.boardv[y][x]:
                    self.screen.blit(self.normallinev, [(x) * 64, (y) * 64 + 5])
                else:
                    self.screen.blit(self.bar_donev, [(x) * 64, (y) * 64 + 5])
        # draw separators
        for x in range(7):
            for y in range(7):
                self.screen.blit(self.separators, [x * 64, y * 64])

    def update(self):
        connection.Pump()
        self.Pump()

        # sleep to make the game 60 fps
        self.clock.tick(60)

        # clear the screen
        self.screen.fill(0)
        # draw the board
        self.drawBoard()
        self.drawHUD()
        for event in pygame.event.get():
            # quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()

        # 1
        mouse = pygame.mouse.get_pos() #拿到鼠标在绘图框的位置

        # 2
        xpos = int(math.ceil((mouse[0] - 32) / 64.0)) #观察其更靠近哪一行
        ypos = int(math.ceil((mouse[1] - 32) / 64.0)) #其更靠近哪一列

        # 观察抽出的鼠标横纵坐标,比较其各是比行近还是比列远
        is_horizontal = abs(mouse[0] - xpos * 64)> abs(mouse[1] - ypos * 64)

        # 4
        ypos = ypos - 1 if mouse[1] - ypos * 64 < 0 and not is_horizontal else ypos
        xpos = xpos - 1 if mouse[0] - xpos * 64 < 0 and is_horizontal else xpos

        # 5
        board = self.boardh if is_horizontal else self.boardv
        isoutofbounds = False

        # 6
        try:
            if not board[ypos][xpos]:
                self.screen.blit(self.hoverlineh if is_horizontal else
                                 self.hoverlinev,
                                                    [xpos * 64 + 5 if is_horizontal else xpos * 64,
                                                    ypos * 64 if is_horizontal else ypos * 64 + 5])
        except:
            isoutofbounds = True
            pass
        if not isoutofbounds:
            alreadyplaced = board[ypos][xpos]
        else:
            alreadyplaced = False
        if pygame.mouse.get_pressed()[0] and not alreadyplaced and not isoutofbounds:
            if is_horizontal:
                self.boardh[ypos][xpos] = True
                self.Send(
                    {"action": "place", "x": xpos, "y": ypos, "is_horizontal": is_horizontal, "gameid": self.gameid,
                     "num": self.num})
            else:
                self.boardv[ypos][xpos] = True
                self.Send(
                    {"action": "place", "x": xpos, "y": ypos, "is_horizontal": is_horizontal, "gameid": self.gameid,
                     "num": self.num})

        # update the screen
        pygame.display.flip()

    def initGraphics(self):
        self.normallinev = pygame.image.load("boxes/normalline.png")
        self.normallineh = pygame.transform.rotate(pygame.image.load("boxes/normalline.png"), -90)
        self.bar_donev = pygame.image.load("boxes/bar_done.png")
        self.bar_doneh = pygame.transform.rotate(pygame.image.load("boxes/bar_done.png"), -90)
        self.hoverlinev = pygame.image.load("boxes/hoverline.png")
        self.hoverlineh = pygame.transform.rotate(pygame.image.load("boxes/hoverline.png"), -90)
        self.separators = pygame.image.load("boxes/separators.png")
        self.redindicator = pygame.image.load("boxes/redindicator.png")
        self.greenindicator = pygame.image.load("boxes/greenindicator.png")
        self.greenplayer = pygame.image.load("boxes/greenplayer.png")
        self.blueplayer = pygame.image.load("boxes/blueplayer.png")
        self.winningscreen = pygame.image.load("boxes/youwin.png")
        self.gameover = pygame.image.load("boxes/gameover.png")
        self.score_panel = pygame.image.load("boxes/score_panel.png")

    def drawHUD(self):
        # draw the background for the bottom:


        # create font
        myfont = pygame.font.SysFont(None, 32)

        # create text surface
        label = myfont.render("Your Turn:", 1, (255, 255, 255))
        # same thing here
        myfont64 = pygame.font.SysFont(None, 64)
        myfont20 = pygame.font.SysFont(None, 20)

        scoreme = myfont64.render(str(self.me), 1, (255, 255, 255))
        scoreother = myfont64.render(str(self.otherplayer), 1, (255, 255, 255))
        scoretextme = myfont20.render("You", 1, (255, 255, 255))
        scoretextother = myfont20.render("Other Player", 1, (255, 255, 255))
        self.screen.blit(self.score_panel, [0, 389])
        self.screen.blit(self.greenindicator, [64 * 2, 389])
        self.screen.blit(scoretextme, (10, 425))
        self.screen.blit(scoreme, (10, 435))
        self.screen.blit(scoretextother, (280, 425))
        self.screen.blit(scoreother, (340, 435))

        # draw surface
        self.screen.blit(label, (10, 400))

    def drawOwnermap(self):
        for x in range(6):
            for y in range(6):
                if self.owner[x][y] != 0:
                    if self.owner[x][y] == "win":
                        self.screen.blit(self.marker, (x * 64 + 5, y * 64 + 5))
                    if self.owner[x][y] == "lose":
                        self.screen.blit(self.othermarker, (x * 64 + 5, y * 64 + 5))

    def finished(self):
        self.screen.blit(self.gameover if not self.didiwin else self.winningscreen, (0, 0))
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pygame.display.flip()


bg=BoxesGame() #__init__ is called right here
while 1:
    bg.update()

