import requests
import json

with open('config.json', 'r') as file:
    config = json.load(file)
TYPEFORM_API_KEY = config["TYPEFORM_API_KEY"]

with open('questions.json', 'r', encoding='utf-8') as file:
    QUESTIONS = json.load(file)

def create_typeform():
    CREATE_FORM_URL = "https://api.typeform.com/forms"

    form_data = {
        "title": "Formulário de Pesquisa - Estratégia 1MiO para Municípios sem Selo UNICEF",
        "settings": {
            "language": "pt"
        },
        "fields": QUESTIONS
    }

    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(CREATE_FORM_URL, headers=headers, data=json.dumps(form_data))

    if response.status_code == 201:
        print("Formulário criado com sucesso!")
        print("Resposta completa da API:", response.json())
    else:
        print("Erro ao criar o formulário:", response.text)

create_typeform()
