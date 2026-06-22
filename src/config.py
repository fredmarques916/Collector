#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
config.py - Configurações e constantes do jogo COLLECTOR
Centraliza todas as configurações gerais para facilitar manutenção e customização.
"""

# ==================== CONFIGURAÇÕES DA TELA ====================
LARGURA_TELA = 800
ALTURA_TELA = 600
TITULO_JOGO = "COLLECTOR - O Coletor de Moedas"
FPS = 60  # Frames por segundo

# ==================== CORES (RGB) ====================
COR_FUNDO = (20, 20, 40)           # Azul escuro
COR_JOGADOR = (0, 255, 0)          # Verde
COR_OBSTACULO = (255, 0, 0)        # Vermelho
COR_MOEDA = (255, 255, 0)          # Amarelo
COR_TEXTO = (255, 255, 255)        # Branco
COR_TEXTO_SECUNDARIO = (200, 200, 200)  # Cinza claro

# ==================== DIMENSÕES DOS OBJETOS ====================
TAMANHO_JOGADOR = 30
TAMANHO_OBSTACULO = 30
TAMANHO_MOEDA = 15

# ==================== VELOCIDADES ====================
VELOCIDADE_JOGADOR = 5             # Pixels por frame
VELOCIDADE_OBSTACULO_INICIAL = 2   # Pixels por frame
VELOCIDADE_OBSTACULO_MAX = 6       # Velocidade máxima dos obstáculos

# ==================== MECÂNICAS DO JOGO ====================
VIDAS_INICIAIS = 3
PONTOS_POR_MOEDA = 10
TEMPO_MOEDA_VISIVEL = 5000         # Tempo em ms que moeda fica visível
INTERVALO_SPAWN_MOEDA = 2000       # Intervalo entre aparecimento de moedas
TEMPO_INVULNERABILIDADE = 1000     # Tempo em ms de invulnerabilidade após colisão
AUMENTO_DIFICULDADE_INTERVALO = 20000  # Aumentar dificuldade a cada 20 segundos

# ==================== CONFIGURAÇÕES DE OBSTÁCULOS ====================
NUM_OBSTACULOS_INICIAL = 2         # Número inicial de obstáculos (reduzido para protótipo)
NUM_OBSTACULOS_MAX = 5             # Número máximo de obstáculos simultâneos

# ==================== ARQUIVO DE DADOS ====================
CAMINHO_ARQUIVO_RECORDE = "data/recorde.txt"
RECORDE_PADRAO = 0
