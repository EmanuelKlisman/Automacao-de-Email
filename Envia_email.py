import pyautogui  # Biblioteca para automação
import time  # Biblioteca para dar pausas no código
import re  # Biblioteca para expressões regulares

'''O objetivo do código é bem simples. Consiste em 2 passos:
1. Perguntar ao usuário qual email ele deseja enviar e validar o formato do email.
2. Iniciar a automação do envio de email (abrir o navegador, escrever e enviar o email).'''

# Função para validar o email
def valida_email(email): 
    padrao = r'^[\w\.-]+@gmail\.com\.br$'  # Expressão regular para validar o formato do e-mail
    return re.match(padrao, email) is not None

# Loop para validar o email
while True:
    email_teste = input("Para qual email voce deseja enviar?").strip()  # Solicita ao usuário o email
    if not valida_email(email_teste):  # Verifica se o e-mail é válido
        print("Email inválido! Certifique-se de que é um endereço @gmail.com.br válido e tente novamente!")
    else:
        print("Email válido!")
        break  # Sai do loop quando o e-mail for válido

# Configurações do PyAutoGUI
pyautogui.PAUSE = 0.5  # Pausa de 0.5 segundos entre cada comando

# Abertura do navegador
pyautogui.press("win")  # Pressiona a tecla 'win'
pyautogui.write("edge")  # Digita "edge"
pyautogui.press("Enter")  # Pressiona 'Enter'
time.sleep(2)  # Espera 2 segundos para o navegador abrir

# Acesso ao Gmail
pyautogui.write("https://mail.google.com")  # Digita a URL do Gmail
pyautogui.press("Enter")  # Pressiona 'Enter'
time.sleep(5)  # Espera 5 segundos para a página carregar

# Ação para escrever o e-mail
# Ajuste as coordenadas conforme necessário
pyautogui.click(x=62, y=210)  # Clica no botão de compor e-mail (verifique se essas coordenadas estão corretas)
time.sleep(2)  # Aguarda 2 segundos para abrir o campo de composição do e-mail
pyautogui.click(x=829, y=302)  # Clica na área de destinatário (verifique as coordenadas)
time.sleep(2)  # Aguarda 2 segundos

# Preenchendo os campos de e-mail
pyautogui.write(email_teste)  # Digita o e-mail fornecido pelo usuário
pyautogui.press("Enter")
pyautogui.press("Tab")  # Vai para o campo de assunto
pyautogui.write("Email teste para o Github")  # Assunto do e-mail
pyautogui.press("Tab")  # Vai para o corpo do e-mail
pyautogui.write("Este é um teste de automação com Python e PyAutoGUI para fins de aprendizado.")  # Corpo do e-mail

# Envia o e-mail
pyautogui.hotkey("ctrl", "enter")  # Pressiona 'Ctrl + Enter' para enviar o e-mail
print("Email enviado com sucesso!")
  