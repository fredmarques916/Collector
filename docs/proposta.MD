# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Collector

## 2. Integrantes do grupo

- Frederico Marcos de Paula Marques
- Lucas Dutra Figueredo

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> Jogo de coleta de itens com obstáculos

## 4. Descrição geral do jogo

Descrição:

> O jogo é uma experiência arcade simples onde:
> 
> - Na tela: Um personagem controlável, moedas espalhadas, obstáculos/inimigos em movimento, placar de pontos, contador de vidas e tempo decorrido.
> - O jogador controla: Um personagem (quadrado ou círculo colorido) que se move em 4 direções.
> - O que precisa fazer: Coletar o máximo possível de moedas enquanto evita colidir com obstáculos que se movem pela tela.
> - Desafios: Obstáculos aparecem aleatoriamente e aumentam em velocidade conforme o tempo passa; moedas surgem em posições aleatórias com tempo limitado de permanência.

## 5. Objetivo do jogador

Objetivo:

> O objetivo principal é coletar a maior quantidade possível de moedas antes de perder todas as vidas, acumulando pontos e estabelecendo um recorde pessoal. O jogo premia tanto a eficiência na coleta quanto a habilidade em evitar obstáculos.

## 6. Regras principais

Regras do grupo:

- O jogador começa com 3 vidas e pode ganhar uma vida adicional a cada 50 moedas coletadas.
- Cada moeda coletada adiciona 10 pontos ao placar.
- Cada colisão com um obstáculo remove 1 vida e congela o jogador por 1 segundo (período de invulnerabilidade).
- As moedas desaparecem automaticamente após 5 segundos se não coletadas.
- Os obstáculos aumentam sua velocidade a cada 20 segundos de jogo (dificuldade progressiva).
- A partida termina imediatamente quando as vidas chegam a zero.
- O recorde máximo é salvo em arquivo para persistência de dados.

## 7. Condição de vitória

Condição de vitória:

> O jogo não possui uma condição de vitória tradicional (final com "você venceu"). O objetivo é sobreviver o máximo possível e acumular a maior pontuação. O jogador "vence" pessoalmente quando supera seu próprio recorde, que é exibido na tela inicial e salvo em arquivo.

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

> A partida termina quando o jogador perde todas as 3 vidas após colisões com obstáculos. Ao encerrar, o jogo exibe a pontuação final, o tempo de jogo e compara com o recorde anterior. O jogador pode reiniciar uma nova partida ou sair do jogo.

## 9. Elementos previstos no jogo

## Jogador ou elemento principal

Descrição:

> Um quadrado verde de 30x30 pixels, controlado pelas setas do teclado ou WASD. O personagem pisca (fica invisível brevemente) após colidir com obstáculos para indicar invulnerabilidade temporária.

## Obstáculos, inimigos ou desafios

Descrição:

> Obstáculos vermelhos (30x30 pixels) que se movem em padrões aleatórios (horizontal, vertical ou diagonal) pela tela. Iniciam com velocidade moderada e aumentam de velocidade gradualmente. Cerca de 3-5 obstáculos ativos simultaneamente, com novos aparecendo conforme o tempo passa.

## Itens, alvos ou objetos de interação

Descrição:

> Moedas amarelas (15x15 pixels) que aparecem em posições aleatórias. Cada moeda fica visível por 5 segundos e desaparece se não coletada. O jogador ganha 10 pontos por moeda coletada. Novas moedas aparecem a cada 2 segundos.

## Pontuação, vidas, tempo ou progresso

Descrição:

> - Vidas: Começam em 3, exibidas como corações na parte superior esquerda.
> - Pontuação: Atual e recorde, exibidos no topo da tela.
> - Tempo: Tempo decorrido da partida atual, atualizado a cada segundo.
> - Nível de dificuldade: Indicado indiretamente pela velocidade dos obstáculos (aumenta a cada 20 segundos).

## 10. Controles previstos

Controles do grupo:

- Seta para cima ou W: mover o personagem para cima
- Seta para baixo ou S: mover o personagem para baixo
- Seta para esquerda ou A: mover o personagem para esquerda
- Seta para direita ou D: mover o personagem para direita
- Espaço: pausar/retomar o jogo
- P: voltar ao menu principal (durante a pausa)
- ESC ou Q: sair do jogo

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

- `main.py`: inicia o jogo;
- `src/jogo.py`: Classe principal do jogo (Game)
- `src/config.py`: Configurações (tamanho da tela, cores,constantes)
- `src/jogador.py`: Classe do personagem jogador
- `src/obstaculo.py`: Classe dos obstáculos/inimigos
- `src/moeda.py`: Classe das moedas
- `src/gerenciador.py`: Gerenciador de colisões, spawning e eventos
- `src/dados.py`: Funções de leitura/escrita de arquivo

## 12. Recursos externos previstos

> Não pretendemos utilizar recursos externos. O jogo será desenvolvido apenas com formas geométricas básicas (quadrados e círculos) usando a biblioteca Pygame, sem imagens, sons ou fontes personalizadas. Textos serão exibidos com a fonte padrão do Pygame.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Detecção de colisões: Implementar corretamente a detecção de colisão entre o jogador e os obstáculos/moedas.
- Sincronização de tempo: Controlar corretamente o timer de desaparecimento das moedas e o aumento progressivo de dificuldade.
- Movimento dos obstáculos: Programar movimentos variados (diagonal, padrão aleatório) sem que saiam da tela.
- Gerenciamento de estado: Manter controle dos estados de pausa, game over, menu principal e jogo ativo.
- Persistência de dados: Implementar corretamente a leitura e escrita do recorde em arquivo de forma segura.
- Organização modular: Dividir o código em classes e funções bem definidas, mantendo responsabilidades claras.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima aceitável do jogo COLLECTOR conterá:
> 
> - Uma janela Pygame funcional (800x600 pixels)
> - Um personagem controlável pelas setas do teclado ou WASD
> - 3-5 obstáculos em movimento aleatório
> - Sistema de coleta de moedas (aparecimento aleatório e coleta detectada)
> - Sistema de vidas (começa com 3, diminui com colisões)
> - Sistema de pontuação (incrementa com coleta de moedas)
> - Detecção de colisão entre jogador e obstáculos
> - Tela de game over com exibição da pontuação final
> - Capacidade de reiniciar o jogo após game over
> - Leitura e escrita do recorde em arquivo
> - Código organizado em pelo menos 4-5 funções ou classes principais
> - Documentação básica no README.md
> - Testes unitários simples para funções críticas (colisão, pontuação)

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Menu principal: Tela inicial com opções de jogar, ver recorde e sair.
- Pausa: Implementar sistema de pausa (tecla Espaço) com menu de pausa.
- Efeitos visuais: Animação de explosão quando o jogador colide, efeito de piscar durante invulnerabilidade.
- Sons: Adicionar sons para coleta de moedas, colisão e game over (usando arquivos WAV simples).
- Níveis/Fases: Diferentes níveis com padrões de obstáculos mais complexos.
- Ranking: Manter histórico dos 5 maiores recordes com nomes.
- Power-ups: Items especiais que concedem invulnerabilidade temporária ou dobram pontos.
- Temas visuais: Diferentes temas de cores ou modos claros/escuro.
- Controles gamepad: Suporte para joystick/controle Xbox.
- Leaderboard visual: Tabela de recordes exibida na tela inicial.