__author__ = "mjdp"
__version__ = "1.0.0"
__email__ = "martin.delpercio@neoris.com"
__name__ = "Libreía de Funciones"

import datetime
import os

def screenShot(driver,caso,nombre):

    # SCREEN SHOT

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
