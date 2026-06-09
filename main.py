#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COLLECTOR - Jogo de Coleta de Moedas
main.py - Arquivo principal que inicia o jogo

Desenvolvido para a disciplina Introdução a Algoritmos - PUC Minas
"""

import pygame
import sys
import os

# Adicionar o diretório src ao path para importações
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from config import *
from jogo import Jogo


def main():
    """Função principal que executa o jogo."""
    # Inicializar Pygame
    pygame.init()
    
    # Criar a janela do jogo
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    
    # Criar relógio para controlar FPS
    relogio = pygame.time.Clock()
    
    # Criar instância do jogo
    jogo = Jogo(tela, relogio)
    
    # Loop principal do jogo
    while jogo.rodando:
        # Controlar FPS
        relogio.tick(FPS)
        
        # Processar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo.rodando = False
            else:
                jogo.processar_evento(evento)
        
        # Atualizar lógica do jogo
        jogo.atualizar()
        
        # Desenhar tudo
        jogo.desenhar(tela)
        
        # Atualizar display
        pygame.display.flip()
    
    # Encerrar
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
