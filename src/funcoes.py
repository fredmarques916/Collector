#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
funcoes.py - Funções utilitárias usadas nos testes
"""

def calcular_pontos(pontos_atual, pontos_ganhos):
    """Retorna a soma dos pontos atuais com os ganhos."""
    return pontos_atual + pontos_ganhos


def jogador_perdeu(vidas):
    """Retorna True se o jogador perdeu (vidas <= 0)."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Limita `valor` ao intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor
