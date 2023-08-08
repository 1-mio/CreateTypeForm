import requests
import json

with open("config.json", "r") as file:
    config = json.load(file)
    API_KEY = config["TYPEFORM_API_KEY"]

THEMES_ENDPOINT = "https://api.typeform.com/themes"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def get_themes(page_token=None):
    params = {}
    if page_token:
        params["page_token"] = page_token

    response = requests.get(THEMES_ENDPOINT, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar os temas: {response.text}")
        return None

themes_data = get_themes()

while themes_data:
    themes = themes_data["items"]
    for theme in themes:
        print(f"Nome do Tema: {theme['name']} - ID do Tema: {theme['id']}")

    if "page_token" in themes_data:
        themes_data = get_themes(themes_data["page_token"])
    else:
        themes_data = None
