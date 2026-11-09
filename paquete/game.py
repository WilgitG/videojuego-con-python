import pygame, sys, os 

class Game:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH=1280
        self.WINDOW_HEIGHT=720

        self.dispplay_surface=pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        ) 

        pygame.display.set_caption('Este no es un juego de STAR WARS')
        self.clock = pygame.time.Clock()
        self.dt=0
        self.load_assets()

    def load_assets(self):
        self.start_bg_surf=pygame.image.load(os.path.join('imagenes','images.png'))
        self.bg_surf=pygame.image.load(os.path.join('imagenes','fondo.png'))
        self.font = pygame.font.Font('./imagenes/Starjedi.ttf', 50)

        self.inicio_sound = pygame.mixer.Sound(os.path.join('sonidos','star-wars.wav'))
        self.disparo_sound = pygame.mixer.Sound(os.path.join('sonidos', 'disparo.mp3'))
        self.disparomil_sound = pygame.mixer.Sound(os.path.join('sonidos', 'disparos_miltiples.mp3'))
        self.inicio_partida_sound = pygame.mixer.Sound(os.path.join('sonidos', 'inicio_partida.mp3'))
        self.muerte_sound = pygame.mixer.Sound(os.path.join('sonidos', 'muerte.mp3'))
        self.viene_enemigo_sound = pygame.mixer.Sound(os.path.join('sonidos', 'viene_enemigo.mp3'))

    def run (self):
        self.show_start_screen()

    def show_start_screen (self):
        title_font = pygame.font.Font ('imagenes/Starjedi.ttf', 60)
        start_font = pygame.font.Font('imagenes/Starjedi.ttf', 40)

        title_text=title_font.render('WARS TAR', True, (255,255,255))
        start_text=start_font.render('Presiona ESPACIO o CLICK DERECHO para inicar el juego', True, (255,255,255))
        
        title_react=title_text.get_rect(midtop=(self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT/4))
        start_react=start_text.get_rect(midbottom=(self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT*3/4))

        waiting=True

        while waiting:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==3:
                    waiting==False
                if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    waiting==False

            self.dispplay_surface.fill((0,0,0))
            self.dispplay_surface.blit(self.start_bg_surf, (0,0))

            self.dispplay_surface.blit(title_text, title_react)
            self.dispplay_surface.blit(start_text, start_react)

         
            self.inicio_sound.play(loops=-1)

            pygame.display.update()
            self.clock.tick(60)