import pyautogui
import pyautogui as escolha

opcao = pyautogui.confirm('Escolha no botão desejado', buttons= ['Excel', 'Word', 'Notepad'])

if opcao == 'Excel':

   escolha.hotkey('win', 'r')
   escolha.sleep(2)
   escolha.typewrite('Excel')
   escolha.sleep(1)
   escolha.press('enter')
   escolha.sleep(2)
   escolha.click(x=1252, y=248)

elif opcao == 'Word':

    escolha.hotkey('win', 'r')
    escolha.sleep(2)
    escolha.typewrite('winword')
    escolha.sleep(1)
    escolha.press('enter')
    escolha.sleep(2)
    escolha.click(x=1366, y=373)

elif opcao == 'Notepad':
    escolha.hotkey('win', 'r')
    escolha.sleep(2)
    escolha.typewrite('Notepad')
    escolha.sleep(1)
    escolha.press('enter')
    #escolha.sleep(2)
    #escolha.click(x=1366, y=373)