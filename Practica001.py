import pyautogui
import subprocess
import time
from libreriaUtiles import screenShotGUI

__name__ = "Práctica Selenium GUI con Python"
__version__ = '0.1'
__author__ = "Martín Javier Del Percio"
__email__ = "martin.delpercio@neoris.com, mdelpercio@teco.com.ar"
__status__ = "Testing"
caso = "WRACaso32"
nombre = "Error"

# Abre la Calculadora
cmd = "C:/Windows/System32/calc.exe"
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, creationflags=0x08000000)

# Pausa de rigor
pyautogui.PAUSE = 0.00

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
    ObjName = "images\\" + objeto + '.PNG'
    SiExiste = pyautogui.locateOnScreen(ObjName)
    button7x, button7y = pyautogui.center(SiExiste)
    pyautogui.click(button7x, button7y)
    pyautogui.moveTo(10, 20)
    return

# Funcion <validarValor>
# Verifica si existe una imagen en pantalla
def validarValor(resultado):
    ObjName = "images\\" + resultado + '.PNG'
    SiExiste = pyautogui.locateOnScreen(ObjName)
    if (SiExiste == None):
        resultado = False
    else:
        resultado = True
    return resultado

# Posiciona el cursor en el ángulo superior izquierdo
pyautogui.moveTo(5, 5)

# Valida que esté abierta la Calculadora
assert (esperarCarga("CALCULADORA", 10000))

# Borra el valor
pulsarBoton("BOTON CE")

# Realizza la operación
pulsarBoton("NUEVE")
pulsarBoton("OCHO")
pulsarBoton("SUMA")
pulsarBoton("DOS")
pulsarBoton("TRES")
pulsarBoton("IGUAL")

# Valida el Resultado esperado
assert (esperarCarga("RESULTADO", 10000))

screenShotGUI(caso, nombre)

# Termina el proceso de la Calculadora
process.kill()