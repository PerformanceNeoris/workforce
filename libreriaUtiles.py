__author__ = "mjdp"
__version__ = "1.0.0"
__email__ = "martin.delpercio@neoris.com"
__name__ = "Librería de Funciones"

import datetime
import os
import pyautogui

def screenShotWeb(driver,caso,nombre):

    # SCREEN SHOT para Web Page

    # Arma la Fecha y Hora
    fechahora = datetime.datetime.now().strftime("%d%m%y%H%M%S")

    # Verifica si existe la carpeta de la Fecha, sino la crea
    file_path = "C:\\Capturas\\" + fechahora
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Verifica si existe la carpeta del caso, sino la crea
    file_path = "C:\\Capturas\\" + fechahora + nombre
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Define la carpeta de Capturas
    captura = "C:\\Capturas\\" + fechahora + "\\" + nombre + ".png"
    driver.get_screenshot_as_file(captura)

def screenShotGUI(caso,nombre):

    # SCREEN SHOT

    localFolder = "C:\\Evidencia"

    # Verifica si existe la carpeta Evidencia, sino la crea
    file_path = localFolder
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Arma las variables
    fechahora = datetime.datetime.now().strftime("%d%m%y%H%M%S")
    fecha = datetime.datetime.now().strftime("%d%m%y")
    hora = datetime.datetime.now().strftime("%H%M%S")

    # Verifica si existe la carpeta de la Fecha, sino la crea
    file_path = localFolder + "\\" + fecha
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    # Verifica si existe la carpeta del caso, sino la crea
    file_path = localFolder + "\\" + fecha + "\\" + caso
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    # Define la carpeta de Capturas
    nombre = nombre + hora
    captura = localFolder + "\\" + fecha + "\\" + caso + "\\" + nombre + ".png"
    pyautogui.screenshot(captura)
