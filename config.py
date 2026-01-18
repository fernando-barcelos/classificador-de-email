from shlex import join
import PyPDF2
import requests, os
from openai import OpenAI as DEEPSEEK
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("HF_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

#classe para tratamento do texto e email.
#vai  retornar se o email é produtivo ou inprodutivo
#vai gerar a resposta
class IaTratament:       
    #classifica os emails
    def classify_email(text):
        payload = {
            "inputs": text,
            "parameters":  {"candidate_labels": [
                "Produtivo: Emails que requerem uma ação ou resposta específica"
                "(ex.: solicitações de suporte técnico, atualização sobre casos"
                " em aberto, dúvidas sobre o sistema).", "Improdutivo: Emails que"
                " não necessitam de uma ação imediata (ex.: mensagens de felicitações, agradecimentos)."]},
            }

        response = (requests.post(os.getenv("URL_MODEL_CLASSIFY"), headers=HEADERS, json=payload)).json()
        response = max(response, key=lambda x: x['score'])
        return response
        
    #gera resposta automatica 
    def generate_response(text, classify):
        client = DEEPSEEK(base_url=os.getenv("URL_DEEPSEEK"), api_key=os.getenv("HF_TOKEN"),)

        if "Produtivo" in classify['label']:
            classify = "Gere uma breve resposta em escopo profissional" \
            " e amigavel para responder o email a seguir, a resposta deve " \
            "começar com rotulo 'Produtivo' seguido de ':' e resposta: "

        elif "Improdutivo" in classify['label']:
            classify = "Gere uma breve resposta em escopo amigavel para" \
            " respoder o email a seguir, a resposta deve começar com o " \
            "rotulo 'Improdutivo' seguido de ':' e resposta: "

        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct:novita",
            messages=[
                {
                    "role": "user",
                    "content": f"{classify}{text}"
                }
            ],
        )
        return completion.choices[0].message.content
class DocumentRead:
    #le o arquivo e retorna para tratamento para IA
    def pdf(document):
        pdf = PyPDF2.PdfReader(document)

        text = []

        for page in pdf.pages:
            text.append(page.extract_text())
        
        return " " + join(text)
    #abre o arquivo txt retornando uma string com o conteudo
    def txt(document):
        txt = document.stream.read().decode('utf-8')
        document.stream.close()
        return txt