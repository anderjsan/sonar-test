import os
import subprocess
import sys

def git_init_commit_push(username, repo_name):
    try:
        # Inicializa um repositório Git
        subprocess.run(["git", "init"])

        # Remove o repositorio de origem
        subprocess.run(["git", "remote", "remove", "origin"])

        # Adiciona o repositório remoto do GitHub
        github_url = f"https://github.com/{username}/{repo_name}.git"
        subprocess.run(["git", "remote", "add", "origin", github_url])

        # Adiciona todos os arquivos ao repositório
        subprocess.run(["git", "add", "."])

        # Faz o primeiro commit
        subprocess.run(["git", "commit", "-m", "[INIT] Very First Commit"])

        # Faz um pull inicial
        subprocess.run(["git", "pull", "--set-upstream", "origin", "master", "--force"])
        
        # Faz o push inicial
        subprocess.run(["git", "push", "--set-upstream", "origin", "master", "--force"])
        print
        print("Repositório criado no GitHub e arquivos enviados!")
        print
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    # Verifica se os argumentos estão corretos
    if len(sys.argv) != 3:
        print("Uso: python3 giterize.py [User Name] [Repo Name]")
        sys.exit(1)

    # Obtém os argumentos da linha de comando
    username = sys.argv[1]
    repo_name = sys.argv[2]
    

    # Chama a função para inicializar o repositório
    git_init_commit_push(username, repo_name)