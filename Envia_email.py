import pyautogui #  Biblioteca para automação
import time # Bivlioteca para dar pausas no código
import re # Biblioeteca para expressöes regulares

'''O objetivo do código é bem simples. Consiste em 2 passos, o primeiro é perguntar ao usuário qual email ele deseja enviar, mas antes o código valida o formato do email
e se for válido envia, caso contrário ele pede um email válido. O segundo passo é inicar a automação do envio de email, ele busca o navegador, cola o link do email 
envia para o email informado com corpo  e assunto'''


email_teste = input("Para qual email voce deseja enviar?") # Solicta ao usuário o email que ele quer enviar
def valida_email(email): # Valida se o email possui o formato @gmail, se sim ele segue o código
    padrao = r'^[\w\.-]+@gmail\.com.br$'
    return re.match(padrao, email) is not None
if not valida_email(email_teste): # se não ele diga o texto abaixo
    print("Email inválido! Certifique-se de que é um endereço @gmail.com válido.")
    exit()  # Encerra o programa se o email for inválido
pyautogui.PAUSE = 0.5 # pausa 5 sgeundos para em cada linha de código
pyautogui.press("win") # aperta a tecla 
pyautogui.write("edge") # Digita o nome do navegador
pyautogui.press("Enter") #automação para tecla "enter
pyautogui.write("https://mail.google.com") # Digita a url do email
pyautogui.press("Enter") # Passa a tecla "Enter"
time.sleep(6) # Espera 5 segundos par a página carregar
pyautogui.click(62, 210) # clica na posicao para enviar o email
pyautogui.click(x=829, y=302) # clica na posiçao para escrever o email
time.sleep(2) # espera 2 segundos
pyautogui.write(email_teste) # chama a variável email_teste
pyautogui.press("Enter") # Pressiona enter
pyautogui.press("Tab") # Pressiona o tab
pyautogui.write("Email teste para o Github") # preenche as informaçõesdo corpo do email
pyautogui.press("Tab") # Pressiona o tab
pyautogui.write("Este é um teste de automação com Python e PyAutoGUI para fins de aprendizado.") # preenche as informaçõesdo corpo do email
pyautogui.hotkey("ctrl", "enter") # envia o email ao destinatário