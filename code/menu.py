#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import surface
from pygame.font import Font
from pygame.rect import Rect

from Code.const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW, C_RED


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            #Desenha Imagens
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(40, "Everest", C_RED, ((WIN_WIDTH / 2), 60))
            self.menu_text(20, "Rafael.G Ru: 4577166", C_WHITE, (300, 15))
            self.menu_text(15, "Pressione C para ver os controles", C_WHITE, ((WIN_WIDTH / 2), 310))
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 175 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 175 + 25 * i))



            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # encerra a janela 
                    quit()  # Encerra o game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.controls()
                    if event.key == pygame.K_DOWN: #Tecla para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: #Tecla para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #Tecla Enter
                        return MENU_OPTION[menu_option]


            pygame.display.flip()

    def controls(self):
     while True:
        self.window.blit(source=self.surf, dest=self.rect)
        self.menu_text(35, "CONTROLES", C_RED, ((WIN_WIDTH / 2), 60))
        self.menu_text(20, "PLAYER 1", C_YELLOW, ((WIN_WIDTH / 2), 110))
        self.menu_text(16, "Mover: SETAS", C_WHITE, ((WIN_WIDTH / 2), 140))
        self.menu_text(16, "Atirar: CTRL DIREITO", C_WHITE, ((WIN_WIDTH / 2), 165))
        self.menu_text(20, "PLAYER 2", C_YELLOW, ((WIN_WIDTH / 2), 205))
        self.menu_text(16, "Mover: W A S D", C_WHITE, ((WIN_WIDTH / 2), 235))
        self.menu_text(16, "Atirar: Barra Espaço", C_WHITE, ((WIN_WIDTH / 2), 260))
        self.menu_text(15, "ESC para voltar", C_YELLOW, ((WIN_WIDTH / 2), 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='lucida Sans Typewriter', size=text_size)
        text_surf: surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)