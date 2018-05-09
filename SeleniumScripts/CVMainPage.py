__author__ = "mjdp"
__version__ = "1.0.0"
__email__ = "mdelpercio@teco.com.ar"

import datetime
from libreriaUtiles import screenShotWeb
from SeleniumScripts.CVGeneral import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class CVMainPage:
    botonIngresar = "//*[@id='ingresar']"
    controlador = webdriver

    def __init__(self,controlador):
        self.controlador = controlador

    # Ingresa a la página de Login
    def clickIngresar(self):
        clickXPATH(self.controlador,self.botonIngresar)





