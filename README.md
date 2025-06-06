Ambiente Python com Warp + SnippetsLab + VS Code (macOS)
Este projeto contém a configuração de um ambiente de desenvolvimento leve, moderno e produtivo para estudar Python com foco na certificação PCEP (Certified Entry-Level Python Programmer).

Estrutura do Projeto
Terminal: Warp (https://www.warp.dev)

Editor: Visual Studio Code (https://code.visualstudio.com/)

Gerenciador de snippets: SnippetsLab (via Setapp)

Python: v3.13 (instalado diretamente, sem Anaconda)

Ambiente virtual: .venv

Passos executados
1. Criar o ambiente virtual
bash
Copiar
Editar
python3 -m venv .venv
source .venv/bin/activate
2. Estrutura de pastas para o curso
bash
Copiar
Editar
mkdir curso-python-pcep
cd curso-python-pcep
3. Instalar pacotes essenciais
css
Copiar
Editar
pip install --upgrade pip
pip install jupyter pandas numpy
4. Criar aliases no .zshrc
bash
Copiar
Editar
alias pcep='cd ~/curso-python-pcep && source .venv/bin/activate'
alias startlab='cd ~/curso-python-pcep && source .venv/bin/activate && jupyter notebook'
Organização com o SnippetsLab
Todos os comandos e fluxos utilizados no terminal foram salvos e organizados em uma coleção personalizada chamada "Warp + Python", com comentários e agrupamentos por categoria.

Exemplo de script
python
Copiar
Editar
import platform
import os

print("Ambiente configurado com sucesso!")
print(f"Python: {platform.python_version()}")
print(f"Pasta atual: {os.getcwd()}")
Por que não usar Anaconda?
Foi escolhida uma configuração manual e leve para entender melhor a estrutura de ambientes virtuais e a instalação de pacotes em Python. O uso de Anaconda foi evitado para manter total controle do ambiente via terminal.

Sobre
Este repositório é parte do meu processo de estudo para a certificação PCEP. Nele compartilho o setup usado e minha rotina de aprendizado com Python no macOS.

📄 Consulte também a [documentação completa de snippets com explicações](snippets_completo.md)




