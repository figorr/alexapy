import os
import requests

# Configura tu token de acceso
GH_TOKEN = os.getenv('GH_TOKEN')
REPO_OWNER = 'figorr'
REPO_NAME = 'alexapy'
TAG_NAME = 'v1.29.7'  # Cambia esto según la versión
RELEASE_NAME = 'Release v1.29.7'  # Cambia esto según lo que desees

# Crear un nuevo Release
def create_release():
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases'
    headers = {'Authorization': f'token {GH_TOKEN}'}
    data = {
        'tag_name': TAG_NAME,
        'name': RELEASE_NAME,
        'draft': False,
        'prerelease': False
    }
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()  # Levanta un error si la solicitud falla
    return response.json()

# Subir un archivo al Release
def upload_asset(release_id, file_path):
    url = f'https://uploads.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/{release_id}/assets?name={os.path.basename(file_path)}'
    headers = {'Authorization': f'token {GH_TOKEN}', 'Content-Type': 'application/octet-stream'}
    
    with open(file_path, 'rb') as f:
        response = requests.post(url, headers=headers, data=f)
        response.raise_for_status()  # Levanta un error si la solicitud falla

if __name__ == '__main__':
    release = create_release()
    release_id = release['id']

    for file_name in os.listdir('dist'):
        file_path = os.path.join('dist', file_name)
        upload_asset(release_id, file_path)
