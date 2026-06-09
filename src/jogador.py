#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
jogador.py - Classe que representa o jogador no jogo COLLECTOR
"""

import pygame
from config import *


class Jogador:
    """Classe que representa o personagem controlável do jogador."""
    
    def __init__(self, x, y):
        """
        Inicializa o jogador.
        
        Args:
            x: Posição inicial X
            y: Posição inicial Y
        """
        self.x = x
        self.y = y
        self.largura = TAMANHO_JOGADOR
        self.altura = TAMANHO_JOGADOR
        self.velocidade = VELOCIDADE_JOGADOR
        
        # Rect para colisões
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        
        # Estado de invulnerabilidade
        self.invulneravel = False
        self.tempo_invulnerabilidade = 0
        self.piscar_contador = 0
        
    def processar_entrada(self):
        """Processa entrada do teclado para movimento."""
        teclas = pygame.key.get_pressed()
        
        # Movimento para cima (Seta ou W)
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.y -= self.velocidade
        
        # Movimento para baixo (Seta ou S)
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.y += self.velocidade
        
        # Movimento para esquerda (Seta ou A)
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.x -= self.velocidade
        
        # Movimento para direita (Seta ou D)
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.x += self.velocidade
    
    def atualizar(self):
        """Atualiza a posição e estado do jogador."""
        # Limitar movimento dentro da tela
        if self.x < 0:
            self.x = 0
        if self.x + self.largura > LARGURA_TELA:
            self.x = LARGURA_TELA - self.largura
        if self.y < 0:
            self.y = 0
        if self.y + self.altura > ALTURA_TELA:
            self.y = ALTURA_TELA - self.altura
        
        # Atualizar rect de colisão
        self.rect.x = self.x
        self.rect.y = self.y
        
        # Gerenciar invulnerabilidade
        if self.invulneravel:
            self.tempo_invulnerabilidade -= 1000 / FPS  # Converter para ms
            self.piscar_contador += 1
            if self.tempo_invulnerabilidade <= 0:
                self.invulneravel = False
                self.piscar_contador = 0
    
    def desenhar(self, tela):
        """Desenha o jogador na tela."""
        # Piscar quando invulnerável
        if self.invulneravel and (self.piscar_contador // 5) % 2 == 0:
            return  # Não desenha (fica invisível)
        
        pygame.draw.rect(tela, COR_JOGADOR, self.rect)
    
    def colidir_com_obstaculo(self):
        """Marca o jogador como atingido por um obstáculo."""
        if not self.invulneravel:
            self.invulneravel = True
            self.tempo_invulnerabilidade = TEMPO_INVULNERABILIDADE
    
    def get_rect(self):
        """Retorna o retângulo de colisão do jogador."""
        return self.rect
