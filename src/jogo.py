#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
jogo.py - Classe principal que gerencia o loop e a lógica do jogo COLLECTOR
"""

import pygame
import random
import os
from config import *
from jogador import Jogador
from recorde import carregar_recorde, salvar_recorde
from moeda import Moeda
from obstaculo import Obstaculo


class Jogo:
    """Classe principal do jogo que gerencia todos os componentes."""
    
    def __init__(self, tela, relogio):
        """
        Inicializa o jogo.
        
        Args:
            tela: Superfície Pygame da janela
            relogio: Objeto Clock do Pygame para controlar FPS
        """
        self.tela = tela
        self.relogio = relogio
        self.rodando = True
        
        # Inicializar fonte
        self.fonte_grande = pygame.font.Font(None, 48)
        self.fonte_media = pygame.font.Font(None, 36)
        self.fonte_pequena = pygame.font.Font(None, 24)
        
        # Criar jogador no centro da tela
        self.jogador = Jogador(
            LARGURA_TELA // 2 - TAMANHO_JOGADOR // 2,
            ALTURA_TELA - 100
        )
        
        # Listas de elementos
        self.obstaculos = []
        self.moedas = []
        
        # Inicializar obstáculos
        for _ in range(NUM_OBSTACULOS_INICIAL):
            self.obstaculos.append(Obstaculo())
        
        # Gerar primeira moeda
        self.moedas.append(Moeda())
        
        # Estado do jogo
        self.pontuacao = 0
        self.vidas = VIDAS_INICIAIS
        # Carregar recorde salvo
        self.recorde = carregar_recorde()
        self.tempo_decorrido = 0  # em ms
        self.tempo_inicio = pygame.time.get_ticks()
        self.pausado = False
        self.game_over = False
        
        # Controle de spawn
        self.ultimo_spawn_moeda = pygame.time.get_ticks()
        self.ultimo_aumento_dificuldade = pygame.time.get_ticks()
    
    def processar_evento(self, evento):
        """Processa eventos do Pygame."""
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # Pausar/retomar
                self.pausado = not self.pausado
            elif evento.key == pygame.K_ESCAPE or evento.key == pygame.K_q:
                # Sair
                self.rodando = False
            elif evento.key == pygame.K_r and self.game_over:
                # Reiniciar quando game over
                self.__init__(self.tela, self.relogio)
    
    def atualizar(self):
        """Atualiza a lógica do jogo a cada frame."""
        if self.pausado or self.game_over:
            return
        
        # Atualizar tempo decorrido
        tempo_atual = pygame.time.get_ticks()
        self.tempo_decorrido = tempo_atual - self.tempo_inicio
        
        # Processar entrada do jogador
        self.jogador.processar_entrada()
        
        # Atualizar jogador
        self.jogador.atualizar()
        
        # Atualizar obstáculos
        for obstaculo in self.obstaculos:
            obstaculo.atualizar()
        
        # Atualizar moedas
        moedas_para_remover = []
        for moeda in self.moedas:
            moeda.atualizar()
            if moeda.esta_expirada():
                moedas_para_remover.append(moeda)
        
        for moeda in moedas_para_remover:
            self.moedas.remove(moeda)
        
        # Detectar colisão: jogador com moedas
        for moeda in self.moedas[:]:
            if self.jogador.get_rect().colliderect(moeda.get_rect()):
                self.pontuacao += moeda.get_pontos()
                self.moedas.remove(moeda)
        
        # Detectar colisão: jogador com obstáculos
        for obstaculo in self.obstaculos:
            if self.jogador.get_rect().colliderect(obstaculo.get_rect()):
                if not self.jogador.invulneravel:
                    self.vidas -= 1
                    self.jogador.colidir_com_obstaculo()
                    
                    if self.vidas <= 0:
                        self.game_over = True
                        # Se houve novo recorde, salvar imediatamente
                        try:
                            if self.pontuacao > self.recorde:
                                self.recorde = self.pontuacao
                                salvar_recorde(self.recorde)
                        except Exception:
                            # Não interrompe a lógica do jogo se falhar ao salvar
                            pass
        
        # Gerar novas moedas periodicamente
        tempo_atual_ms = pygame.time.get_ticks()
        if tempo_atual_ms - self.ultimo_spawn_moeda > INTERVALO_SPAWN_MOEDA:
            if len(self.moedas) < 5:  # Máximo de 5 moedas
                self.moedas.append(Moeda())
            self.ultimo_spawn_moeda = tempo_atual_ms
        
        # Aumentar dificuldade periodicamente
        if tempo_atual_ms - self.ultimo_aumento_dificuldade > AUMENTO_DIFICULDADE_INTERVALO:
            for obstaculo in self.obstaculos:
                obstaculo.aumentar_dificuldade()
            
            # Adicionar novo obstáculo se não temos o máximo
            if len(self.obstaculos) < NUM_OBSTACULOS_MAX:
                self.obstaculos.append(Obstaculo(VELOCIDADE_OBSTACULO_INICIAL))
            
            self.ultimo_aumento_dificuldade = tempo_atual_ms
    
    def desenhar(self, tela):
        """Desenha todos os elementos do jogo na tela."""
        # Limpar tela com cor de fundo
        tela.fill(COR_FUNDO)
        
        # Desenhar jogador
        self.jogador.desenhar(tela)
        
        # Desenhar moedas
        for moeda in self.moedas:
            moeda.desenhar(tela)
        
        # Desenhar obstáculos
        for obstaculo in self.obstaculos:
            obstaculo.desenhar(tela)
        
        # Desenhar UI (pontuação, vidas, tempo)
        self._desenhar_ui(tela)
        
        # Desenhar game over se necessário
        if self.game_over:
            self._desenhar_game_over(tela)
        
        # Desenhar pausa se necessário
        if self.pausado:
            self._desenhar_pausa(tela)
    
    def _desenhar_ui(self, tela):
        """Desenha a interface do usuário (placar, vidas, tempo)."""
        # Placar
        texto_pontos = self.fonte_pequena.render(
            f"Pontos: {self.pontuacao}", True, COR_TEXTO
        )
        tela.blit(texto_pontos, (10, 10))
        
        # Vidas
        texto_vidas = self.fonte_pequena.render(
            f"Vidas: {self.vidas}", True, COR_TEXTO
        )
        tela.blit(texto_vidas, (10, 40))

        # Recorde
        try:
            texto_recorde = self.fonte_pequena.render(
                f"Recorde: {self.recorde}", True, COR_TEXTO
            )
            tela.blit(texto_recorde, (10, 70))
        except Exception:
            # Se algo falhar (ex.: recorde não definido), não quebrar a UI
            pass
        
        # Tempo
        segundos = self.tempo_decorrido // 1000
        minutos = segundos // 60
        segundos = segundos % 60
        texto_tempo = self.fonte_pequena.render(
            f"Tempo: {minutos:02d}:{segundos:02d}", True, COR_TEXTO
        )
        tela.blit(texto_tempo, (LARGURA_TELA - 200, 10))
        
        # Dificuldade (número de obstáculos)
        texto_dif = self.fonte_pequena.render(
            f"Obstáculos: {len(self.obstaculos)}", True, COR_TEXTO
        )
        tela.blit(texto_dif, (LARGURA_TELA - 200, 40))
    
    def _desenhar_game_over(self, tela):
        """Desenha a tela de game over."""
        # Fundo semi-transparente
        overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        tela.blit(overlay, (0, 0))
        
        # Texto "GAME OVER"
        texto_game_over = self.fonte_grande.render(
            "GAME OVER", True, (255, 0, 0)
        )
        rect_game_over = texto_game_over.get_rect(
            center=(LARGURA_TELA // 2, ALTURA_TELA // 2 - 80)
        )
        tela.blit(texto_game_over, rect_game_over)
        
        # Pontuação final
        texto_final = self.fonte_media.render(
            f"Pontuação Final: {self.pontuacao}", True, COR_TEXTO
        )
        rect_final = texto_final.get_rect(
            center=(LARGURA_TELA // 2, ALTURA_TELA // 2)
        )
        tela.blit(texto_final, rect_final)
        
        # Instruções
        texto_restart = self.fonte_pequena.render(
            "Pressione R para reiniciar ou ESC para sair", True, COR_TEXTO_SECUNDARIO
        )
        rect_restart = texto_restart.get_rect(
            center=(LARGURA_TELA // 2, ALTURA_TELA // 2 + 100)
        )
        tela.blit(texto_restart, rect_restart)
    
    def _desenhar_pausa(self, tela):
        """Desenha a tela de pausa."""
        # Fundo semi-transparente
        overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))
        tela.blit(overlay, (0, 0))
        
        # Texto "PAUSA"
        texto_pausa = self.fonte_grande.render(
            "PAUSA", True, COR_TEXTO
        )
        rect_pausa = texto_pausa.get_rect(
            center=(LARGURA_TELA // 2, ALTURA_TELA // 2 - 50)
        )
        tela.blit(texto_pausa, rect_pausa)
        
        # Instruções
        texto_continuar = self.fonte_pequena.render(
            "Pressione ESPAÇO para continuar", True, COR_TEXTO_SECUNDARIO
        )
        rect_continuar = texto_continuar.get_rect(
            center=(LARGURA_TELA // 2, ALTURA_TELA // 2 + 50)
        )
        tela.blit(texto_continuar, rect_continuar)
