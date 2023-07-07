import pygame as p
import pygame.freetype as pf
import SquareGenerator as gen

class ChessBoard:
    MODE = None
    screen = None
    def __init__(self, mode):
        self.MODE = mode
    
    WIDTH = HEIGHT = 512
    DIMENSION = 8
    SQ_SIZE = HEIGHT // DIMENSION
    MAX_FPS = 15
    screen = p.display.set_mode((WIDTH + 200, HEIGHT))

    specialSquare0 = None
    specialSquare1 = None
    specialSquare2 = None
    generator = gen.RandomSquare()

    squaresRight = 0
    totalSquares = 0

    def main(self):
        last = p.time.get_ticks()
        cooldown = 300
        ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
        rowsToRanks = {v: k for k, v in ranksToRows.items()}
        filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
        colsToFiles = {v: k for k, v in filesToCols.items()}
        backwards = {0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, 7:0}

        p.init()
        self.screen = p.display.set_mode((self.WIDTH + 200, self.HEIGHT))
        p.display.set_caption("Chess! Chess! Chess!!!!")
        clock = p.time.Clock()
        self.screen.fill(p.Color("white"))

        running = True
        sqSelected = ()
        playerClicks = []
        self.specialSquare0 = " "
        self.specialSquare1 = self.generator.generateSquare()
        self.specialSquare2 = self.generator.generateSquare()
        self.drawBoard(self.screen, self.specialSquare1, None, None) 
        while running:
            ticks = p.time.get_ticks()
            for e in p.event.get():
                self.displaySquare(self.screen, self.specialSquare0, self.specialSquare1, self.specialSquare2)
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.KEYDOWN:
                    if e.key == p.K_ESCAPE:
                        running = False
                elif e.type == p.MOUSEBUTTONDOWN and p.mouse.get_pos()[0] <= self.HEIGHT:
                    location = p.mouse.get_pos()
                    col = location[0]//self.SQ_SIZE
                    row = location[1]//self.SQ_SIZE
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                    if ((colsToFiles[col] + rowsToRanks[row]) == self.specialSquare1):
                        self.drawBoard(self.screen, self.specialSquare1, (row, col), None) 
                        self.rotateSquares()
                        self.squaresRight+=1 #increment score
                        self.totalSquares+=1
                    else:
                        self.drawBoard(self.screen, self.specialSquare1, (row, col), (backwards[int(self.specialSquare1[1])-1], filesToCols[self.specialSquare1[0]])) 
                        self.rotateSquares()
                        self.totalSquares+=1 #increment score
            now = p.time.get_ticks()
            if now - last >= cooldown:
                last = now
                self.drawBlankBoard(self.screen) 
            clock.tick(self.MAX_FPS)
            self.displayScore(self.screen)
            p.display.flip()


    def drawBoard(self, screen, specialSquare, location1, location2):
        colors = [p.Color("white"), p.Color("gray")]
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                color = colors[((r+c) % 2)]
                if (location1 != None) and (r == location1[0] and c == location1[1]):
                    if (location2 == None):
                        color = p.Color("#a5f0a5") # green
                    else:
                        color = p.Color("#ff928c") # red
                elif (location2 != None) and (r == location2[0] and c == location2[1]):
                    color = p.Color("#a5f0a5") # green
                p.draw.rect(screen, color, p.Rect(c*self.SQ_SIZE, r*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))                                    
        
    def displaySquare(self, screen, oldSpecialSquare, currSpecialSquare, newSpecialSquare):
        font = pf.SysFont('Sans', 50)
        font2 = pf.SysFont('Sans', 35)
        p.draw.rect(screen, "white", p.Rect(520,25,63,76))
        p.draw.rect(screen, "white", p.Rect(585,10,63,63))
        p.draw.rect(screen, "white", p.Rect(650,22,63,76))
        font2.render_to(screen, (525, 50), oldSpecialSquare, "gray", "white")
        font.render_to(screen, (585, 25), currSpecialSquare, "black", "white")
        font2.render_to(screen, (655, 50), newSpecialSquare, "gray", "white")

    def drawBlankBoard(self, screen):
        colors = [p.Color("white"), p.Color("gray")]
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                color = colors[((r+c) % 2)]
                p.draw.rect(screen, color, p.Rect(c*self.SQ_SIZE, r*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def rotateSquares(self):
        curr = self.specialSquare1
        two = self.specialSquare2
        self.specialSquare0 = curr
        self.specialSquare1 = two
        self.specialSquare2 = self.generator.generateSquare()

    def displayScore(self, screen):
        font = pf.SysFont('Sans', 50)
        p.draw.rect(screen, "white", p.Rect(545,340,110,65))
        font.render_to(screen, (555, 350), str(self.squaresRight) + " / " + str(self.totalSquares), "black", "white")

if __name__ == "__main__":
    obj = ChessBoard("unlimited")
    obj.main()