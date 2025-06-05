import platform
import sys
import os

print("Ambiente Python configurado com sucesso!")
print("Essa vai pro linkedin!!!")
print(f"Python: {platform.python_version()}")
print(f"Pasta atual: {os.getcwd()}")
print(f"VS Code no PATH: {'code' in os.environ.get('PATH', '')}")
print("Pacotes importados no momento:")
print(", ".join(sorted([pkg for pkg in sys.modules if not pkg.startswith('_')])))
