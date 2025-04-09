import subprocess
import ctypes
import sys
import os

def is_admin():
    """Verifica se o script está sendo executado como administrador."""
    try:
        admin_status = ctypes.windll.shell32.IsUserAnAdmin()
        print("Admin Status:", admin_status)  # Para depuração
        return admin_status == 1  # Retorna True se for admin, False caso contrário
    except Exception as e:
        print(f"Erro ao verificar permissões de admin: {e}")  # Para capturar erros
        return False

def check_updates():
    """Verifica por atualizações do Windows usando o PowerShell."""
    check_updates_command = "Get-WindowsUpdate -AcceptAll"
    try:
        result = subprocess.run(['powershell', '-Command', check_updates_command], capture_output=True, text=True)
        print("Saída do PowerShell:", result.stdout)  # Para depuração
        print("Erros do PowerShell:", result.stderr)  # Para depuração

        # Verifica o código de retorno
        if result.returncode == 0:
            if "No updates available" in result.stdout:
                print("O Windows já está atualizado.")
            else:
                print("Há atualizações disponíveis.")
                user_choice = input("Deseja instalar as atualizações? (s/n): ").strip().lower()
                if user_choice == 's':
                    install_updates()
        else:
            print("Erro ao verificar atualizações:", result.stderr)
    except Exception as e:
        print(f"Erro ao executar o comando PowerShell: {e}")

def install_updates():
    """Instala as atualizações do Windows usando o PowerShell."""
    install_command = "Install-WindowsUpdate -AcceptAll -IgnoreReboot"
    try:
        result = subprocess.run(['powershell', '-Command', install_command], capture_output=True, text=True)
        print("Saída do PowerShell (instalação):", result.stdout)  # Para depuração
        print("Erros do PowerShell (instalação):", result.stderr)  # Para depuração

        if result.returncode == 0:
            print("Instalando atualizações...")
        else:
            print("Erro ao instalar atualizações:", result.stderr)
    except Exception as e:
        print(f"Erro ao executar o comando PowerShell: {e}")

if __name__ == "__main__":
    if is_admin():
        check_updates()
    else:
        print("Este script precisa ser executado com permissões de administrador.")
        script_path = os.path.abspath(sys.argv[0])
        try:
            # Tenta reexecutar o script como administrador
            subprocess.run([
                'powershell', 
                '-Command', 
                f'Start-Process powershell -ArgumentList \'-ExecutionPolicy Bypass -File "{script_path}"\' -Verb RunAs'
            ])
        except Exception as e:
            print(f"Erro ao tentar reiniciar o script com privilégios de administrador: {e}")
        sys.exit(0)
