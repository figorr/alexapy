import os
import subprocess

# Define las variables necesarias
GITHUB_REPO = 'git@github.com:figorr/alexapy.git'
BRANCH = 'master'

# Función para hacer el sync de GitLab a GitHub
def sync_to_github():
    # Añadir el repositorio remoto de GitHub
    subprocess.run(['git', 'remote', 'add', 'github', GITHUB_REPO], check=True)
    
    # Hacer el push a la rama master de GitHub
    subprocess.run(['git', 'push', 'github', BRANCH], check=True)

if __name__ == '__main__':
    sync_to_github()
