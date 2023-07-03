
import pygame as p
import pygame.freetype as pf
import SquareGenerator as gen
import time as t

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def main():
    last = p.time.get_ticks()
    cooldown = 300
    generator = gen.RandomSquare()
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}
    backwards = {0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, 7:0}

    p.init()
    screen = p.display.set_mode((WIDTH + 200, HEIGHT))
    p.display.set_caption("Chess! Chess! Chess!!!!")
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    running = True
    sqSelected = ()
    playerClicks = []
    currTime = t.time()
    specialSquare = generator.generateSquare()
    drawBoard(screen, specialSquare, None, None) 
    while running:
        ticks = p.time.get_ticks()
        for e in p.event.get():
            displaySquare(screen, specialSquare)
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN and p.mouse.get_pos()[0] <= HEIGHT:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                sqSelected = (row, col)
                playerClicks.append(sqSelected)
                if ((colsToFiles[col] + rowsToRanks[row]) == specialSquare):
                    drawBoard(screen, specialSquare, (row, col), None) 
                    specialSquare = generator.generateSquare() 
                else:
                    drawBoard(screen, specialSquare, (row, col), (backwards[int(specialSquare[1])-1], filesToCols[specialSquare[0]])) 
                    specialSquare = generator.generateSquare()
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    pass
        now = p.time.get_ticks()
        if now - last >= cooldown:
            last = now
            drawBlankBoard(screen) 
        clock.tick(MAX_FPS)
        p.display.flip()


def drawBoard(screen, specialSquare, location1, location2):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            if (location1 != None) and (r == location1[0] and c == location1[1]):
                if (location2 == None):
                    color = p.Color("#a5f0a5") # green
                else:
                    color = p.Color("#ff928c") # red
            elif (location2 != None) and (r == location2[0] and c == location2[1]):
                color = p.Color("#a5f0a5") # green
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))                                    
    
def displaySquare(screen, specialSquare):
    font = pf.SysFont('Sans', 50)
    font.render_to(screen, (550, 10), specialSquare, "black", "white",)

def drawBlankBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()