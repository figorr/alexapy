import os
import subprocess

# Set de necessary variables
GITHUB_REPO = 'git@github.com:figorr/alexapy.git'
BRANCH_LOCAL = 'master'   # GitLab branch
BRANCH_REMOTE = 'master'   # GitHub branch

# Function to sync from GitLab to GitHub
def sync_to_github():
    # Add the remote repository from GitHub
    subprocess.run(['git', 'remote', 'add', 'github', GITHUB_REPO], check=True)
    
    # Fetch the latest changes from the GitLab branch
    subprocess.run(['git', 'fetch', 'origin', BRANCH_LOCAL], check=True)
    
    # Push to master branch at GitHub
    subprocess.run(['git', 'push', 'github', f'origin/{BRANCH_LOCAL}:refs/heads/{BRANCH_REMOTE}'], check=True)

if __name__ == '__main__':
    sync_to_github()
