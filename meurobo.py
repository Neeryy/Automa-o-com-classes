import pyautogui
import time
import pyperclip

class MrBoot:

    def __init__(self, tempo_espera):
        self.tempo_espera = tempo_espera
        pyautogui.PAUSE = 1

    def abrir_navegador(self, navegador):
        pyautogui.press('win')
        pyautogui.write(navegador)
        pyautogui.press('enter')
        
    def entrar_site(self, site):
        self.escrever_e_entrar(site)
        self.esperar()

    def escrever_e_entrar(self, texto):
        pyperclip.copy(texto)
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')

    def esperar(self):
        time.sleep(self.tempo_espera)

    def pesquisar_campo(self, texto):
        self.escrever_e_entrar(texto)
        self.esperar()

    def clicar(self, x, y, botao='left'):
        pyautogui.click(x, y, button=botao)

    def _pegando_mouse(self):
        for i in range(5):
            print(f'Pegando a posição em {5 - i} segundos')
            time.sleep(1)

        print(pyautogui.position())

    def pegando_link(self, x, y):
        self.clicar(x, y, botao= "right")
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('enter')

        texto = pyperclip.paste()
        print(texto)


            # ------------- PROGRAMA ------------- #


robo = MrBoot(3)

robo.abrir_navegador('Chrome')
robo.entrar_site('https://www.youtube.com/')
robo.clicar(x=1386, y=147)
robo.esperar()
robo.clicar(x=1196, y=208)
robo.esperar()
robo.pegando_link(x=441, y=65)



# robo._pegando_mouse()

