import pygame as p
import pygame.freetype as pf
from ChessBoard import ChessBoard

class Menu:
    WIDTH = 712
    HEIGHT = 512
    DIMENSION = 8
    SQ_SIZE = WIDTH // 3
    MAX_FPS = 15
    screen = p.display.set_mode((WIDTH, HEIGHT))

    def main(self):
        p.init()
        self.screen.fill(p.Color("white"))
        p.display.set_caption("Chess!")
        clock = p.time.Clock()
        running = True
        while running:
            self.screen.fill("white")
            event = p.event.poll()
            if event.type == p.QUIT:
                running = False
            elif event.type == p.KEYDOWN:
                if event.key == p.K_e:
                    obj = ChessBoard("unlimited")
                    obj.main()
            elif p.mouse.get_pos()[0] <= self.SQ_SIZE:
                self.drawScreen(0)
                if event.type == p.MOUSEBUTTONDOWN:
                    obj = ChessBoard("unlimited")
                    obj.main()
            elif p.mouse.get_pos()[0] >= 2*self.SQ_SIZE:
                self.drawScreen(2)
                pass
            else:
                self.drawScreen(1)
                pass
            clock.tick(self.MAX_FPS)
            p.display.flip()
            # Timed, unlimited
        
    def drawScreen(self, pos):
        color0 = color1 = color2 = "white"
        if pos == 0:
            color0 = "#f0f3f5"
        elif pos == 1:
            color1 = "#f0f3f5"
        elif pos == 2:
            color2 = "#f0f3f5"
        p.draw.rect(self.screen, color0, p.Rect(0,0,self.SQ_SIZE,self.HEIGHT))
        p.draw.rect(self.screen, color1, p.Rect(self.SQ_SIZE,0,self.SQ_SIZE,self.HEIGHT))
        p.draw.rect(self.screen, color2, p.Rect(self.SQ_SIZE*2,0,self.SQ_SIZE,self.HEIGHT))
        p.draw.line(self.screen, "#d0d4d6", (self.SQ_SIZE, 20), (self.SQ_SIZE, self.HEIGHT-20))
        p.draw.line(self.screen, "#d0d4d6", (2*self.SQ_SIZE, 20), (2*self.SQ_SIZE, self.HEIGHT-20))
        font = pf.SysFont('Sans', 20)
        font.render_to(self.screen, (self.SQ_SIZE-150, 50), "Unlimited", "black", color0)
        font.render_to(self.screen, (2*self.SQ_SIZE-150, 50), "Timed", "black", color1)
        font.render_to(self.screen, (3*self.SQ_SIZE-150, 50), "text goes here", "black", color2)
        pass

if __name__ == "__main__":
    obj = Menu()
    obj.main()