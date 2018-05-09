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

class CVLoginPage:
    userName = "username"
    password = "password"
    ingresar = "ingresar-button"
    controlador = webdriver

    def __init__(self,controlador):
        self.controlador = controlador

    def ingresar(self,controlador,usuario,clave):
        #wait = WebDriverWait(self.controlador, 5)
        # Ingresa Usuario
        inputElement(self.controlador,self.userName,self.usuario)

     #   element = wait.until(EC.presence_of_element_located((By.NAME, self.userName)))
     #   self.controlador.find_element_by_name(self.userName).send_keys(self.usuario)

        # Ingresa Contraseeña
        inputElement(self.controlador,self.password,self.clave)

    #   element = wait.until(EC.presence_of_element_located((By.NAME, self.password)))
     #   self.controlador.find_element_by_name(self.password).send_keys(self.clave)

        # Hace click en el botón Login
        clickID(self.controlador,self.ingresar)

