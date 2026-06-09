#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
moeda.py - Classe que representa as moedas coletáveis no jogo COLLECTOR
"""

import pygame
import random
from config import *


class Moeda:
    """Classe que representa uma moeda no jogo."""
    
    def __init__(self, x=None, y=None):
        """
        Inicializa uma moeda.
        
        Args:
            x: Posição X (aleatória se None)
            y: Posição Y (aleatória se None)
        """
        if x is None:
            self.x = random.randint(TAMANHO_MOEDA, LARGURA_TELA - TAMANHO_MOEDA * 2)
        else:
            self.x = x
            
        if y is None:
            self.y = random.randint(50, ALTURA_TELA - TAMANHO_MOEDA * 2)
        else:
            self.y = y
        
        self.largura = TAMANHO_MOEDA * 2
        self.altura = TAMANHO_MOEDA * 2
        self.raio = TAMANHO_MOEDA
        
        # Rect para colisões
        self.rect = pygame.Rect(self.x - self.raio, self.y - self.raio, 
                                self.largura, self.altura)
        
        # Tempo de criação
        self.tempo_criacao = pygame.time.get_ticks()
    
    def atualizar(self):
        """Atualiza o estado da moeda."""
        self.rect.x = self.x - self.raio
        self.rect.y = self.y - self.raio
    
    def desenhar(self, tela):
        """Desenha a moeda na tela."""
        pygame.draw.circle(tela, COR_MOEDA, (int(self.x), int(self.y)), self.raio)
        # Desenhar borda
        pygame.draw.circle(tela, (200, 200, 0), (int(self.x), int(self.y)), self.raio, 2)
    
    def esta_expirada(self):
        """Verifica se a moeda expirou."""
        tempo_passado = pygame.time.get_ticks() - self.tempo_criacao
        return tempo_passado > TEMPO_MOEDA_VISIVEL
    
    def get_rect(self):
        """Retorna o retângulo de colisão da moeda."""
        return self.rect
    
    def get_pontos(self):
        """Retorna os pontos que a moeda vale."""
        return PONTOS_POR_MOEDA
