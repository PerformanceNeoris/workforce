import pyautogui
import time
from libreriaUtiles import screenShotGUI
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

__name__ = "Práctica Selenium GUI con Python"
__version__ = '0.1'
__author__ = "Martín Javier Del Percio"
__email__ = "martin.delpercio@neoris.com, mdelpercio@teco.com.ar"
__status__ = "Testing"

caso = "WRACaso32"
nombre = "Error"

# Pausa de rigor
pyautogui.PAUSE = 1.00

# Function <locateObject>
# Verifica un objeto en la ventana esperando una cantidad de milisegundos
def esperarCarga(ObjName, timeout):
    counter = 0
    myTime = 0
    timeout = timeout/1000
    while ((not(validarValor(ObjName))) and (myTime < timeout)):
        counter += 1
        time.sleep(0.1)
        myTime = counter
        print (myTime)

    if (myTime == timeout):
        return False
    else:
        return True

# Funcion <pulsarBoton>
# Verifica si existe un elemento en pantalla
# Si existe, toma sus coordenadas y le hace click
def pulsarBoton(objeto):
    ObjName = "images\\" + objeto + ".PNG"
    SiExiste = pyautogui.locateOnScreen(ObjName)
    button7x, button7y = pyautogui.center(SiExiste)
    pyautogui.click(button7x, button7y)

# Funcion <validarValor>
# Verifica si existe una imagen en pantalla
def validarValor(resultado):
    ObjName = "images\\" + resultado + ".PNG"
    SiExiste = pyautogui.locateOnScreen(ObjName)
    if (SiExiste == None):
        resultado = False
    else:
        resultado = True
    return resultado

# Posiciona el cursor en el ángulo superior izquierdo
pyautogui.moveTo(5, 5)

# Abre la página
global URL
URL="http://www.cablevisionfibertel.com.ar"
driver = webdriver.Chrome('C:\\Webdrivers\\chromedriver.exe')
#driver.set_page_load_timeout(10)
driver.get(URL)
print(driver.title)
time.sleep(5)
driver.maximize_window()
wait = WebDriverWait(driver, 5)

pyautogui.moveTo(5, 505)
time.sleep(1)
pyautogui.click(5, 505,3)

# Valida que esté abierta la página principal
assert (esperarCarga("MAINPAGE", 10000))

assert (esperarCarga("INGRESAR", 10000))

ObjName = "images\\INGRESAR.PNG"
SiExiste = pyautogui.locateOnScreen(ObjName)
button7x, button7y = pyautogui.center(SiExiste)
pyautogui.click(button7x, button7y)

# Borra el valor
#pulsarBoton("INGRESAR")

pyautogui.moveTo(5, 505)
time.sleep(1)
pyautogui.click(5, 505,3)

# Valida que esté abierta la página Login
assert (esperarCarga("LOGINPAGE", 10000))

pyautogui.moveTo(5, 505)
time.sleep(1)
pyautogui.click(5, 505,3)

# Realizza la operación LOGIN
pulsarBoton("USUARIO")

pyautogui.typewrite("martinjavierd")
pyautogui.keyDown('altright')
pyautogui.keyDown('q')
pyautogui.keyUp('altright')
pyautogui.keyUp('q')
pyautogui.typewrite("gmail.com")

pulsarBoton("CLAVE")

pyautogui.typewrite("CrudSec2")

pyautogui.moveTo(5, 505)
time.sleep(1)
pyautogui.click(5, 505,3)

#pulsarBoton("BTNLOGIN")

ObjName = "images\\BTNLOGIN.PNG"
SiExiste = pyautogui.locateOnScreen(ObjName)
button7x, button7y = pyautogui.center(SiExiste)
pyautogui.click(button7x, button7y)

# Valida el Resultado esperado
#assert (esperarCarga("VALIDA_LOGIN", 10000))

ObjName = "images\\VALIDALOG.PNG"
SiExiste = pyautogui.locateOnScreen(ObjName)
print (SiExiste)

#screenShotGUI(caso, nombre)

# Termina el proceso
driver.close()