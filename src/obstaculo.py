#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
obstaculo.py - Classe que representa os obstáculos do jogo COLLECTOR
"""

import pygame
import random
import math
from config import *


class Obstaculo:
    """Classe que representa um obstáculo no jogo."""
    
    def __init__(self, velocidade=VELOCIDADE_OBSTACULO_INICIAL):
        """
        Inicializa um obstáculo em posição aleatória.
        
        Args:
            velocidade: Velocidade inicial do obstáculo
        """
        self.x = random.randint(TAMANHO_OBSTACULO, LARGURA_TELA - TAMANHO_OBSTACULO)
        self.y = random.randint(50, ALTURA_TELA - TAMANHO_OBSTACULO)
        
        self.largura = TAMANHO_OBSTACULO
        self.altura = TAMANHO_OBSTACULO
        self.velocidade = velocidade
        
        # Direção do movimento (aleatória)
        angulo = random.uniform(0, 2 * math.pi)
        self.dx = velocidade * math.cos(angulo)
        self.dy = velocidade * math.sin(angulo)
        
        # Rect para colisões
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
    
    def atualizar(self):
        """Atualiza a posição do obstáculo com rebound nas bordas."""
        # Mover obstáculo
        self.x += self.dx
        self.y += self.dy
        
        # Rebound nas bordas (inverter direção)
        if self.x <= 0 or self.x + self.largura >= LARGURA_TELA:
            self.dx = -self.dx
            self.x = max(0, min(self.x, LARGURA_TELA - self.largura))
        
        if self.y <= 0 or self.y + self.altura >= ALTURA_TELA:
            self.dy = -self.dy
            self.y = max(0, min(self.y, ALTURA_TELA - self.altura))
        
        # Atualizar rect
        self.rect.x = self.x
        self.rect.y = self.y
    
    def desenhar(self, tela):
        """Desenha o obstáculo na tela."""
        pygame.draw.rect(tela, COR_OBSTACULO, self.rect)
        # Desenhar borda para melhor visibilidade
        pygame.draw.rect(tela, (200, 0, 0), self.rect, 2)
    
    def aumentar_dificuldade(self):
        """Aumenta a velocidade do obstáculo."""
        if self.velocidade < VELOCIDADE_OBSTACULO_MAX:
            aumento = 0.5
            self.velocidade = min(self.velocidade + aumento, VELOCIDADE_OBSTACULO_MAX)
            
            # Manter a direção, apenas aumentar velocidade
            magnitude = math.sqrt(self.dx**2 + self.dy**2)
            if magnitude > 0:
                self.dx = (self.dx / magnitude) * self.velocidade
                self.dy = (self.dy / magnitude) * self.velocidade
    
    def get_rect(self):
        """Retorna o retângulo de colisão do obstáculo."""
        return self.rect
