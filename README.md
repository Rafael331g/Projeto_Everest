# Projeto_Everest
🏔️ Everest

Everest é um jogo 2D desenvolvido em Python com Pygame, no qual o jogador deve sobreviver aos inimigos, desviar de disparos e acumular pontos até atingir a condição de vitória.

🎮 Funcionalidades
Modo para 1 jogador
Modo para 2 jogadores cooperativo
Modo para 2 jogadores competitivo
Três fases
Sistema de vida e dano
Disparos de jogadores e inimigos
Sistema de colisões
Pontuação
Placar
Tela de vitória e derrota
Tela de controles
Música e backgrounds animados
🏆 Objetivo

Cada jogador inicia com:

100 pontos de vida

O objetivo é atingir:

500 pontos

Ao alcançar 500 pontos, o jogador vence.

Se perder toda a vida antes disso, a partida termina em derrota.

🕹️ Controles
Player 1
Setas direcionais → Movimento
CTRL Direito      → Atirar
Player 2
W / A / S / D     → Movimento
CTRL Esquerdo     → Atirar

No menu principal, pressione:

C

para visualizar a tela de controles.

👾 Inimigos

O jogo possui três tipos de inimigos:

Enemy1
Enemy2
Enemy3

Cada um possui características próprias de vida, dano, velocidade, disparo e pontuação.

🛠️ Tecnologias
Python 3.14
pygame-ce 2.5.8
Visual Studio Code
Git
GitHub
⚙️ Instalação

Crie e ative o ambiente virtual:

py -3.14 -m venv .venv
.venv\Scripts\activate

Instale as dependências:

pip install -r requirements.txt

Ou diretamente:

pip install pygame-ce==2.5.8
▶️ Executar o jogo

Com o ambiente virtual ativo:

python main.py
