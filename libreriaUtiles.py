__author__ = "mjdp"
__version__ = "1.0.0"
__email__ = "martin.delpercio@neoris.com"
__name__ = "Libreía de Funciones"

import datetime

def screenShot(driver,nombre):
    # SCREEN SHOT
    fechahora = datetime.datetime.now().strftime("%d%m%y%H%M%S")
    locacion = "C:\\Capturas\\"
    captura = locacion + nombre + fechahora + ".png"
    driver.get_screenshot_as_file(captura)