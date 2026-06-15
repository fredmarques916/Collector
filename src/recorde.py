#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
recorde.py - Funções para carregar e salvar o recorde do jogo

Funções expostas:
 - carregar_recorde() -> int
 - salvar_recorde(recorde: int) -> None
"""

import os


def _caminho_arquivo_recorde():
    raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    dados_dir = os.path.join(raiz, 'data')
    if not os.path.isdir(dados_dir):
        os.makedirs(dados_dir, exist_ok=True)
    return os.path.join(dados_dir, 'recorde.txt')


def carregar_recorde():
    """Carrega o recorde do arquivo `data/recorde.txt`.

    Retorna 0 se o arquivo não existir ou estiver vazio/conter dados inválidos.
    """
    caminho = _caminho_arquivo_recorde()
    try:
        if not os.path.exists(caminho):
            return 0

        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read().strip()
            if not conteudo:
                return 0
            try:
                return int(conteudo)
            except ValueError:
                return 0
    except Exception:
        return 0


def salvar_recorde(recorde):
    """Salva o `recorde` (inteiro) em `data/recorde.txt`.

    Substitui o conteúdo anterior. Garante que o diretório `data/` exista.
    """
    caminho = _caminho_arquivo_recorde()
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(str(int(recorde)))
