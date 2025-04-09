import subprocess
import ctypes
import sys
import os

def is_admin():
    # Verifica se o script está sendo executado como administrador
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def check_updates():
    # Executa o comando do PowerShell para verificar atualizações
    check_updates_command = "Get-WindowsUpdate -Install -AcceptAll | Out-Null"
    result = subprocess.run(['powershell', '-Command', check_updates_command], capture_output=True, text=True)

    # Verifica se há atualizações
    if "No updates available" in result.stdout:
        print("O Windows já está atualizado.")
    else:
        print("Há atualizações disponíveis.")
        user_choice = input("Deseja instalar as atualizações? (s/n): ").strip().lower()
        
        if user_choice == 's':
            install_updates()

def install_updates():
    # Executa o comando do PowerShell para instalar atualizações
    install_command = "Install-WindowsUpdate -AcceptAll -IgnoreReboot"
    subprocess.run(['powershell', '-Command', install_command])
    print("Instalando atualizações...")

if __name__ == "__main__":
    if is_admin():
        # Se o script está sendo executado como administrador, verificamos atualizações
        check_updates()
    else:
        # Se o script não está sendo executado como administrador, relançamos com privilégios elevados
        print("Este script precisa ser executado com permissões de administrador.")
        
        # Caminho absoluto do script
        script_path = os.path.abspath(sys.argv[0])
        
        # Reexecuta o script com privilégios elevados
        subprocess.run([
            'powershell', 
            '-Command', 
            f'Start-Process powershell -ArgumentList \'-ExecutionPolicy Bypass -File "{script_path}"\' -Verb RunAs'
        ])
        
        # Após tentar elevação, finaliza a execução da instância sem privilégios
        sys.exit(0)
