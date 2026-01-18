
# Email Classifier with AI

## 📋 Descrição

Projeto de classificação de emails desenvolvido com padrão **MVC** que utiliza inteligência artificial para classificar e gerar respostas automatizadas para emails.

## 🤖 Modelos IA Utilizados

- **BART Large MNLI** (Hugging Face): Classificação de emails
- **Meta Llama 3.1 8B Instruct** (Novita): Geração de respostas automáticas

## 🏗️ Arquitetura

- **Backend**: Flask (Python)
- **Frontend**: Página renderizada para upload de informações
- **Padrão**: MVC (Model-View-Controller)
- **Ambiente**: Python venv

## 🚀 Instalação (Ubuntu 22+)

```bash
#instalar dependencias necessarias
sudo apt update && sudo apt upgrade -y

sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

sudo apt install python3.11 -y

sudo apt install python3-pip -y

apt install python3.13-venv -y

# Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

#instalar o git
sudo apt install git -y

# Clonar repositório
git clone https://github.com/fernando-barcelos/classificador-de-email.git
cd classificador-de-email

# Instalar dependências
pip install -r requirements.txt

# Edite o .env com suas credenciais das APIs
nano .env
    HF_TOKEN = seu token aqui

	URL_MODEL_CLASSIFY = https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli

	URL_DEEPSEEK = https://router.huggingface.co/v1

#instalar o waitress para produção
 pip install waitress

# Executar aplicação
waitress-serve --host=0.0.0.0 --port=80 app:app
```

## 📦 Dependências Principais

- Flask
- Requests (para APIs Hugging Face)
- Python-dotenv

## ⚙️ Variáveis de Ambiente

Configure no arquivo `.env`:

```
HUGGINGFACE_API_KEY=seu_token
BART_MODEL=facebook/bart-large-mnli
LLAMA_MODEL=meta-llama/Llama-3.1-8B-Instruct
```
## 📝 Uso
1. Acesse a aplicação via navegador.
2. Faça upload do email a ser classificado.
3. Aguarde a classificação e a geração da resposta automática.