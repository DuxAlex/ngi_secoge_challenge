import subprocess
import os

# Função para executar um arquivo Python
def executar_script(script):
    try:
        script_path = os.path.join("scripts", script)  # Caminho relativo correto
        print(f"Executando o script {script}...")
        subprocess.run(["python3", script_path], check=True)
        print(f"Script {script} executado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script {script}: {e}")

# Executando os scripts extracao.py e transformar_salvar.py
executar_script("extracao.py")
executar_script("transformar_salvar.py")
