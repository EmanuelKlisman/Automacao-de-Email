import pyautogui
import subprocess
import time

def abrir_windows_update():
    # Abrir o menu iniciar e procurar Windows Update
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('windows update')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

def verificar_atualizacoes():
    # Verifica o status das atualizações com PowerShell 
    try:
        # Comando para verificar atualizações pendentes
        command = 'powershell "Get-WindowsUpdateLog"'
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        output = result.stdout

        # Procura por uma indicação de que o Windows está atualizado ou não
        if "instalado" in output.lower():
            return "O Windows está atualizado."
        else:
            return "Há atualizações pendentes no Windows."
    except Exception as e:
        return f"Erro ao verificar atualizações: {e}"

def atualizar_windows():
    # Atualiza o sistema operacional automaticamente via PowerShell
    try:
        # Comando para buscar e instalar atualizações
        command = 'powershell "Install-Module PSWindowsUpdate -Force; Install-WindowsUpdate -AcceptAll -AutoReboot"'
        subprocess.run(command, shell=True)
        return "Atualizações aplicadas com sucesso. O sistema será reiniciado se necessário."
    except Exception as e:
        return f"Erro ao atualizar o sistema: {e}"

if __name__ == "__main__":
    # Abrir a interface gráfica do Windows Update (opcional)
    abrir_windows_update()

    # Verificar o status das atualizações
    status = verificar_atualizacoes()
    print(status)

    # Se o sistema estiver desatualizado, atualizar automaticamente
    if "atualizado" not in status.lower():
        print("Atualizando o sistema...")
        resultado_atualizacao = atualizar_windows()
        print(resultado_atualizacao)
