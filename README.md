# Desafio Pygame

Pequeno projeto em Pygame com dois textos ("PY" e "DVD") que se movem pela tela, batem nas bordas e mudam de cor/velocidade. Quando os textos colidem entre si, os dois ficam aleatorios (cor e velocidade).

## Instalacao

```bash
python -m venv venv
# Windows
venv\Scripts\activate
pip install pygame
```

## Como executar

```bash
python desafio.py
```

## Comportamento

- Os textos se movem continuamente na tela.
- Ao tocar nas bordas, a velocidade muda de direcao e a cor muda.
- Quando os textos colidem, ambos recebem nova cor e nova velocidade aleatoria.

## Estrutura

- desafio.py: codigo principal do jogo.
