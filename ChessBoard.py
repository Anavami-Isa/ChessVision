
import pygame as p

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def main():
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption("Chess! Chess! Chess!!!!")
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    running = True
    sqSelected = ()
    playerClicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                sqSelected = (row, col)
                playerClicks.append(sqSelected)
                print(colsToFiles[col] + "  " + rowsToRanks[row])

            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    pass

        drawBoard(screen) 
        clock.tick(MAX_FPS)
        p.display.flip()


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()