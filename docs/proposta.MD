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

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

> Escreva aqui.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> Escreva aqui.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> Escreva aqui.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> Escreva aqui.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando:
- Tecla/comando:
- Tecla/comando:

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

> Escreva aqui.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

> Escreva aqui.

Caso não pretenda utilizar recursos externos, escreva:

> Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1:
- Dificuldade 2:
- Dificuldade 3:

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> Escreva aqui.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1:
- Melhoria 2:
- Melhoria 3: