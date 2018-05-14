import pyautogui
import time
import xlrd
from selenium.webdriver.support import expected_conditions as EC
from libreriaUtiles import screenShotGUI
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

__name__ = "Práctica Selenium GUI con Python"
__version__ = '0.1'
__author__ = "Martín Javier Del Percio"
__email__ = "martin.delpercio@neoris.com, mdelpercio@teco.com.ar"
__status__ = "Testing"

caso = "WRACaso32"
nombre = "Error"
usuario = ""
proveedor = ""
clave = ""
webpage = ""

# Pausa de rigor
pyautogui.PAUSE = 1.00

def clickID(driver, nombre):
    element = wait.until(EC.presence_of_element_located((By.ID, nombre)))
    driver.find_element_by_id(nombre).click()

# Carga los parámetross de un EXCEL determinado
def open_file(path, registro):

    book = xlrd.open_workbook(path)

    # get the first worksheet
    first_sheet = book.sheet_by_index(0)

    # read a row
    print (first_sheet.row_values(0))

    cell = first_sheet.cell(registro, 0)
    usuario = (cell.value)
    print ("Usuario: " + usuario)

    cell = first_sheet.cell(registro, 1)
    proveedor = (cell.value)
    print ("Proveedor: " + proveedor)

    cell = first_sheet.cell(registro, 2)
    clave = (cell.value)
    print("Clave: " + clave)

    cell = first_sheet.cell(registro, 3)
    webpage = (cell.value)
    print("Webpage: " + webpage)

    book.release_resources()

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

def insertarMail(usuario,proveedor):
    pulsarBoton("USUARIO")
    pyautogui.typewrite(usuario)
    pyautogui.keyDown('altright')
    pyautogui.keyDown('q')
    pyautogui.keyUp('altright')
    pyautogui.keyUp('q')
    pyautogui.typewrite(proveedor)
    pyautogui.typewrite(".com")

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
open_file("params\\PARAMS.xlsx",1)

pyautogui.moveTo(5, 505)
time.sleep(1)
pyautogui.click(5, 505,3)

# Valida que esté abierta la página principal
assert (esperarCarga("MAINPAGE", 10000))

assert (esperarCarga("INGRESAR", 10000))

'''''
ObjName = "images\\INGRESAR.PNG"
SiExiste = pyautogui.locateOnScreen(ObjName)
button7x, button7y = pyautogui.center(SiExiste)
pyautogui.click(button7x, button7y)
'''''

pulsarBoton("INGRESAR")

pyautogui.moveTo(5, 505)
time.sleep(1)
pyautogui.click(5, 505,3)

# Valida que esté abierta la página Login
assert (esperarCarga("LOGINPAGE", 10000))

pyautogui.moveTo(5, 505)
time.sleep(1)
pyautogui.click(5, 505,3)

# Ingresa Usuario

'''''
pulsarBoton("USUARIO")

email = usuario + "@" + proveedor
element = wait.until(EC.presence_of_element_located((By.NAME, email)))
driver.find_element_by_name("userName").send_keys(usuario)

pulsarBoton("CLAVE")

# Ingresa Contraseeña
element = wait.until(EC.presence_of_element_located((By.NAME, clave)))
driver.find_element_by_name("password").send_keys(clave)

# Hace click en el botón Login
clickID(driver,"ingresar-button")

insertarMail("martinjavierd","gmail")
'''''

# Realizza la operación LOGIN
pulsarBoton("USUARIO")

pyautogui.typewrite("martinjavierd")
pyautogui.keyDown('altright')
pyautogui.keyDown('q')
pyautogui.keyUp('altright')
pyautogui.keyUp('q')
pyautogui.typewrite("gmail.com")

pulsarBoton("CLAVE")

time.sleep(1)

pyautogui.typewrite("CrudSec2")

pyautogui.moveTo(5, 505)
time.sleep(1)
pyautogui.click(5, 505,3)

pulsarBoton("BTNLOGIN")

# Valida el Resultado esperado

pyautogui.moveTo(5, 505)
time.sleep(1)
pyautogui.click(5, 505,3)

assert (esperarCarga("VALIDALOG", 10000))

#screenShotGUI(caso, nombre)

# Termina el proceso
driver.close()