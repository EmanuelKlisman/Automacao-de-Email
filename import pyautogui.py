import pyautogui #  Biblioteca para automação
import time # Bivlioteca para dar pausas no código

email_teste = input("Para qual email voce deseja enviar?") # Solicta ao usuário o email que ele quer enviar
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