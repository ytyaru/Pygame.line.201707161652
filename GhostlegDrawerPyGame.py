import sys, pygame
import Ghostleg
# あみだくじを描画する（1Byte文字。横線はハイフン）
class GhostlegDrawerPyGame:
    class Screen:
        def __init__(self):
            self.__color = (0,0,0)
            self.__size = (320, 240)
            self.__screen = pygame.display.set_mode(self.__size)
        @property
        def Screen(self): return self.__screen
        @property
        def Size(self): return self.__size
        def Fill(self): self.__screen.fill(self.__color)

    def __init__(self, ghostleg=None):
        self.__leg = None
        self.__ghostleg = ghostleg
        pygame.init()
        pygame.display.set_caption("あみだくじ描画")
        self.__screen = GhostlegDrawerPyGame.Screen()
        self.__clock = pygame.time.Clock()
        self.__width = 8
        self.__color = (255,255,255)
#        print(pygame.font.get_fonts()) # 使えるフォント名
    
    # あみだくじを描画する
    def Draw(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit();
            self.__screen.Fill()
            self.__draw_vartical_lines()
            self.__draw_horizon_lines()
            self.__draw_goals()
            pygame.display.flip()
            self.__clock.tick(60) # 60 FPS

#        pygame.draw.lines(screen, self.__color, False, self.__pointlist, self.__width)

    def __draw_vartical_lines(self):
        for xi in range(len(self.__ghostleg.Ghostleg)+1):
            start = (20 + xi * 40, 20)
            end = (20 + xi * 40, self.__screen.Size[1] - 40)
            pygame.draw.line(self.__screen.Screen, self.__color, start, end, self.__width)

    def __draw_goals(self):
#        font = pygame.font.SysFont(None, 20)
#        font = pygame.font.Font("migmix1m", 12)
#        font = pygame.font.Font("migmix1m.ttf", 12)
        font = pygame.font.Font("/usr/share/fonts/truetype/migmix/migmix-1m-regular.ttf", 12)
        for i in range(len(g.Goals)):
#            self.__screen.Screen.blit(font.render(g.GetGoal(i), False, self.__color), (20 + i * 40, self.__screen.Size[1] - 40))
            self.__screen.Screen.blit(font.render(g.Goals[i], False, self.__color), (20 + i * 40, self.__screen.Size[1] - 40))
            
    def __draw_horizon_lines(self):
        for yi in range(len(self.__ghostleg.Ghostleg[0])):
            for xi in range(len(self.__ghostleg.Ghostleg)):
                if 1 == self.__ghostleg.Ghostleg[xi][yi]:
                    start = (20 + xi * 40, 20 + (yi+1) * 25)
                    end = (20 + (xi+1) * 40, 20 + (yi+1) * 25)
                    pygame.draw.line(self.__screen.Screen, self.__color, start, end, self.__width)
        

    """
    def Redraw(self, ghostleg):
        self.__ghostleg = ghostleg
        
        
        
        self.__leg = ''
        for y in range(len(ghostleg.Ghostleg[0])):
            for x in range(len(ghostleg.Ghostleg)):
                self.__leg += '|'
                self.__leg += '-' if 1 == ghostleg.Ghostleg[x][y] else ' '
                if x == len(ghostleg.Ghostleg) - 1: self.__leg += '|'
#                if x == len(ghostleg.Ghostleg) - 1 and 0 == (x % 2): self.__leg += '|'
            self.__leg += '\n'
        self.__draw_goals(ghostleg)
        return self.__leg
    def __draw_goals(self, ghostleg):        
        max_len = max([len(g) for g in ghostleg.Goals])
        for y in range(max_len):
            for x in range(len(ghostleg.Ghostleg)+1):
                if y < len(ghostleg.Goals[x]): self.__leg += ghostleg.Goals[x][y] # 文字インデックスyと行数を対応させる
                else: self.__leg += '　'
            self.__leg += '\n'
    """            

g = Ghostleg.Ghostleg()
g.Create()
drawer = GhostlegDrawerPyGame(g)
for i in range(len(g.Goals)): print(i, g.GetGoal(i))
drawer.Draw()


