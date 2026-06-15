# Collector

## Integrantes

* Lucas Dutra
* Fred Marques


---

## Sobre o jogo

**Collector** é um jogo desenvolvido em Python utilizando a biblioteca Pygame.

O objetivo do jogador é coletar o maior número possível de moedas enquanto evita obstáculos que aparecem na tela. Conforme a partida avança, a dificuldade aumenta, exigindo maior atenção e reflexos do jogador.

O jogo possui sistema de pontuação, vidas, obstáculos dinâmicos e registro de recordes.

---

## Objetivo

Coletar moedas para aumentar a pontuação e sobreviver o máximo de tempo possível, evitando colisões com obstáculos.

---

## Regras

* O jogador controla um personagem na tela.
* Moedas aparecem aleatoriamente e podem ser coletadas.
* Cada moeda coletada aumenta a pontuação.
* Obstáculos aparecem durante a partida.
* Colidir com um obstáculo reduz uma vida.
* Quando todas as vidas acabam, a partida termina.
* O jogo registra o melhor desempenho obtido.

---

## Controles

| Tecla | Ação                  |
| ----- | --------------------- |
| ←     | Mover para a esquerda |
| →     | Mover para a direita  |
| ↑     | Mover para cima       |
| ↓     | Mover para baixo      |
| ESC   | Sair do jogo          |

---

## Estrutura do Projeto

```text
Collector/
│
├── assets/
│   ├── images/
│   └── sounds/
│
├── data/
│   ├── ranking.txt
│   └── recorde.txt
│
├── docs/
│   └── proposta.md
│
├── src/
│   ├── config.py
│   ├── jogador.py
│   ├── jogo.py
│   ├── moeda.py
│   └── obstaculo.py
│
├── tests/
│   └── test_logica.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Tecnologias Utilizadas

* Python
* Pygame
* Pytest

---

## Como Executar

### 1. Clonar o repositório

```bash
git clone <link-do-repositorio>
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Executar o jogo

```bash
python main.py
```

---

## Testes

Para executar os testes automatizados:

```bash
pytest
```

ou

```bash
python -m pytest
```

---

## Conceitos da Disciplina Utilizados

* Variáveis
* Estruturas condicionais
* Laços de repetição
* Funções
* Modularização
* Listas
* Manipulação de arquivos
* Programação orientada a objetos
* Testes automatizados
* Biblioteca Pygame

---

## Melhorias Futuras

* Sistema de ranking completo
* Novos tipos de obstáculos
* Diferentes níveis de dificuldade
* Efeitos sonoros
* Tela inicial e tela de vitória
* Sistema de fases

---

## Licença

Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina de Introdução a Algoritmos e Programação.
