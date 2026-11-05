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
        self.bg_surf=pygame.image.load(os.path.join('imagen','images.png'))
        self.font = pygame.font.Font('./images/Starjedi.ttf', 50)

        self.inicio_sound = pygame.mixer.Sound(os.path.join('sonidos','star-wars.mp3'))
        self.disparo_sound = pygame.mixer.Sound(os.path.join('sonidos', 'disparo.mp3'))
        self.disparomil_sound = pygame.mixer.Sound(os.path.join('sonidos', 'disparos_miltiples.mp3'))
        self.inicio_partida_sound = pygame.mixer.Sound(os.path.join('sonidos', 'inicio_partida.mp3'))
        self.muerte_sound = pygame.mixer.Sound(os.path.join('sonidos', 'muerte.mp3'))
        self.viene_enemigo_sound = pygame.mixer.Sound(os.path.join('sonidos', 'viene_enemigo.mp3'))