import os
import sys

# Inserir o diretório raiz do projeto no início de sys.path para permitir
# imports absolutos como `from src import ...` quando os testes forem executados.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
