# 📦 Snippets WARP + Python PCEP — com comentários e explicações

Este arquivo contém os principais comandos usados no terminal Warp para configurar um ambiente Python leve no macOS.  
Os caminhos são exemplos — **substitua `curso-python-pcep` pelo nome da sua pasta de projeto**, se desejar.

---

## 📁 Entrar no projeto e ativar o ambiente virtual

```bash
# Acessa a pasta do projeto
cd ~/curso-python-pcep

# Ativa o ambiente virtual (.venv)
source .venv/bin/activate
```

---

## 💻 Criar novo script Python com conteúdo inicial

```bash
# Cria um novo arquivo com um print básico
echo 'print("Hello, Warp + Python!")' > main.py

# Abre o arquivo (macOS) ou substitua por `code main.py` se usar VS Code
open main.py
```

---

## 📦 Instalar pacotes essenciais para o curso

```bash
# Atualiza o pip
pip install --upgrade pip

# Instala pacotes comuns em cursos de Python
pip install pandas numpy jupyter
```

---

## 🚀 Iniciar Jupyter Notebook

```bash
# Garante que está na pasta do projeto com o ambiente ativo
cd ~/curso-python-pcep
source .venv/bin/activate

# Inicia o Jupyter no navegador
jupyter notebook
```

---

## 🔁 Rodar script Python no terminal

```bash
# Roda o script atual
python main.py
```

---

## 🔍 Ver pacotes instalados

```bash
# Lista pacotes Python instalados
pip list
```

---

## ❌ Desativar o ambiente virtual

```bash
# Sai do ambiente virtual
deactivate
```

---

## 📑 Ver arquivos com detalhes

```bash
# Lista arquivos (incluindo ocultos como .venv)
ls -la
```

---

## 🔄 Ativar ambiente direto ao abrir o terminal

```bash
# Entra no projeto e ativa o ambiente em uma linha
cd ~/curso-python-pcep && source .venv/bin/activate
```

---

## 📁 Criar novo projeto com ambiente virtual

```bash
# Cria nova pasta e entra nela
mkdir novo-projeto && cd novo-projeto

# Cria ambiente virtual
python3 -m venv .venv

# Ativa o ambiente virtual
source .venv/bin/activate

# Cria arquivo Python vazio
touch main.py

# Abre o arquivo para editar
open main.py
```

---

## 🧩 Aliases configurados no `.zshrc`

```bash
# Abre o arquivo .zshrc no editor nano
nano ~/.zshrc
```

Adicione estas linhas no final do arquivo:

```bash
alias pcep='cd ~/curso-python-pcep && source .venv/bin/activate'
alias startlab='cd ~/curso-python-pcep && source .venv/bin/activate && jupyter notebook'
alias codepcep='cd ~/curso-python-pcep && code .'
alias mkpy='echo "print(\"Hello, PCEP!\")" > main.py && code main.py'
alias installpcep='cd ~/curso-python-pcep && source .venv/bin/activate && pip install -r requirements.txt'
```

Atalhos do `nano`:
- `CTRL + O` → salvar o arquivo
- `Enter` → confirmar o nome
- `CTRL + X` → sair do editor