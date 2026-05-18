# 📖 Guia Completo: Git e GitHub do Zero

> Este guia foi feito para quem **nunca usou Git**. Vai te levar do zero até ter o repositório PortfolioHUB publicado, versionado e online.

---

## 🎯 O que você vai conseguir ao final

✅ Conta criada no GitHub
✅ Git instalado e configurado na sua máquina
✅ Repositório PortfolioHUB publicado online
✅ Versão 1.0 marcada (tag)
✅ Site funcionando no GitHub Pages
✅ Link pronto para colocar no LinkedIn

---

## 📋 ETAPA 1 — Criar conta no GitHub

1. Acesse: [https://github.com/signup](https://github.com/signup)
2. Cadastre-se com seu e-mail (use um que vai usar profissionalmente)
3. Escolha um username **profissional** (ex: `joao-silva`, `joaosilva-ds`) — esse vai aparecer na URL do seu portfólio
4. Confirme o e-mail

> 💡 **Dica:** O username vai aparecer em `github.com/gabrielsabatino`. Escolha algo que você usaria num currículo.

---

## 📋 ETAPA 2 — Instalar o Git

### Windows
1. Baixe em: [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Execute o instalador (pode deixar as opções padrão clicando "Next" em tudo)
3. Abra o **Git Bash** (vai aparecer no menu iniciar)

### Mac
Abra o Terminal e digite:
```bash
git --version
```
Se não tiver instalado, o Mac vai oferecer pra instalar automaticamente.

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install git
```

### Verificar instalação
Em qualquer sistema, abra o terminal e digite:
```bash
git --version
```
Deve aparecer algo como: `git version 2.40.0`

---

## 📋 ETAPA 3 — Configurar o Git

Abra o terminal (Git Bash no Windows) e rode estes 2 comandos, **trocando pelos seus dados**:

```bash
git config --global user.name "Gabriel Queiroz de Souza Sabatino"
git config --global user.email "gabrielqsabatino@gmail.com"
```

> ⚠️ Use o **mesmo e-mail** cadastrado no GitHub.

Verifique se ficou certo:
```bash
git config --global user.name
git config --global user.email
```

---

## 📋 ETAPA 4 — Criar o repositório no GitHub

1. Logado no GitHub, clique no botão **`+`** no canto superior direito → **New repository**
2. Preencha:
   - **Repository name:** `portfolio-hub`
   - **Description:** `Portfólio profissional de projetos em Ciência de Dados e IA`
   - **Public** ✅ (precisa ser público pro GitHub Pages funcionar de graça)
   - **NÃO** marque "Add a README file" (já temos um)
   - **NÃO** marque ".gitignore" nem "license"
3. Clique em **Create repository**

Anote a URL que vai aparecer, será algo como:
```
https://github.com/gabrielsabatino/portfolio-hub.git
```

---

## 📋 ETAPA 5 — Subir os arquivos pra o GitHub

### 5.1. Baixe a pasta `portfolio-hub` que eu te entreguei

Descompacte em um local fácil de achar, por exemplo: `C:\Users\SeuNome\Documents\portfolio-hub` (Windows) ou `~/Documents/portfolio-hub` (Mac/Linux).

### 5.2. Personalize os arquivos

Antes de subir, abra os arquivos abaixo num editor de texto (Bloco de Notas, VS Code, etc.) e troque:

- **`Gabriel Sabatino`** → seu nome verdadeiro
- **`gabrielsabatino`** → seu username do GitHub
- **`gabrielsabatino`** → seu username do LinkedIn
- **`gabrielqsabatino@gmail.com`** → seu e-mail

Arquivos a personalizar:
- `README.md`
- `LICENSE`
- `site-portfolio/index.html`
- `projetos/analise-vendas/README.md`
- `projetos/classificador-iris/README.md`

> 💡 **Dica:** Use a função "Localizar e substituir" (Ctrl+H) do editor.

### 5.3. Abra o terminal **dentro da pasta** do projeto

**Windows:** dentro da pasta `portfolio-hub`, clique com botão direito → "Git Bash Here"
**Mac/Linux:** abra o terminal e digite `cd ~/Documents/portfolio-hub`

### 5.4. Rode os comandos abaixo, **um por um**:

```bash
# Inicializa o repositório Git local
git init

# Define o branch principal como 'main'
git branch -M main

# Adiciona TODOS os arquivos ao "stage" (área de preparação)
git add .

# Faz o primeiro commit (a primeira "fotografia" do projeto)
git commit -m "Primeira versão do PortfolioHUB (v1.0)"

# Conecta o repositório local ao GitHub (TROQUE gabrielsabatino!)
git remote add origin https://github.com/gabrielsabatino/portfolio-hub.git

# Envia tudo para o GitHub
git push -u origin main
```

> ⚠️ **No último passo**, o GitHub vai pedir seu usuário e senha. A senha não é mais a do site — você precisa criar um **Personal Access Token**:
> 1. No GitHub: Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token
> 2. Marque a opção **`repo`**
> 3. Copie o token gerado e cole no terminal quando pedir senha

---

## 📋 ETAPA 6 — Criar a tag de versão 1.0

A tag marca oficialmente a "versão 1.0" do projeto (requisito do desafio):

```bash
# Cria a tag
git tag -a v1.0 -m "Versão 1.0 - Primeira entrega do PortfolioHUB"

# Envia a tag pro GitHub
git push origin v1.0
```

Vá no GitHub e na lateral direita você verá a tag **v1.0** aparecer em "Releases".

---

## 📋 ETAPA 7 — Ativar o GitHub Pages

1. No GitHub, abra seu repositório `portfolio-hub`
2. Clique em **Settings** (no menu de cima do repositório)
3. No menu lateral esquerdo, clique em **Pages**
4. Em **"Source"**, selecione:
   - **Branch:** `main`
   - **Folder:** `/site-portfolio`
5. Clique em **Save**
6. Aguarde 1-2 minutos

Atualize a página e aparecerá o link:
```
✅ Your site is live at https://gabrielsabatino.github.io/portfolio-hub/
```

🎉 **Seu portfólio está no ar!**

---

## 📋 ETAPA 8 — Adicionar no LinkedIn

### 8.1. No seu perfil do LinkedIn:

1. Acesse seu perfil → clique em **"Adicionar seção de perfil"**
2. Em **"Em destaque"** → **"+ Adicionar destaque"** → **"Link"**
3. Cole a URL do GitHub Pages: `https://gabrielsabatino.github.io/portfolio-hub/`
4. Título: **"PortfolioHUB - Portfólio de Ciência de Dados"**
5. Descrição: **"Portfólio com projetos de análise de dados e machine learning em Python"**
6. Salve

### 8.2. Adicione também na seção "Projetos":

1. **"Adicionar seção de perfil"** → **"Adicional"** → **"Adicionar projetos"**
2. Nome: **PortfolioHUB**
3. Descrição: descreva os 2 projetos
4. Link: cole a URL do GitHub: `https://github.com/gabrielsabatino/portfolio-hub`
5. Salve

---

## 🔄 Fluxo Git no dia a dia (resumo)

Sempre que mudar algo no projeto:

```bash
git add .                          # adiciona mudanças
git commit -m "descrição clara"    # registra com mensagem
git push                           # envia pro GitHub
```

---

## ❓ Problemas comuns

### "fatal: not a git repository"
Você está na pasta errada. Use `cd` pra entrar na pasta `portfolio-hub` antes dos comandos.

### Pediu usuário e senha mas senha não funciona
Use o Personal Access Token (Etapa 5.4). Senha de login do site não funciona mais.

### "rejected — non-fast-forward"
Alguém (ou você no GitHub) editou o repositório online. Rode:
```bash
git pull --rebase
git push
```

### GitHub Pages não aparece
- Verifique se selecionou a pasta `/site-portfolio` corretamente
- Aguarde uns minutos
- Confira se o arquivo se chama exatamente `index.html`

---

## 📚 Comandos úteis para o futuro

| Comando | O que faz |
|---------|-----------|
| `git status` | Mostra o que mudou |
| `git log` | Mostra histórico de commits |
| `git diff` | Mostra diferenças nos arquivos |
| `git branch` | Lista branches |
| `git checkout -b nome` | Cria e muda pra um novo branch |
| `git pull` | Baixa mudanças do GitHub |

---

✅ **Pronto!** Agora você tem um portfólio online versionado e profissional.
