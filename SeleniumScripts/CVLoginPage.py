__author__ = "mjdp"
__version__ = "1.0.0"
__email__ = "mdelpercio@teco.com.ar"

import datetime
import pyautogui
import subprocess
import time
from libreriaUtiles import screenShotGUI
from libreriaUtiles import screenShotWeb
from SeleniumScripts.CVGeneral import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class CVLoginPage:
    userName = "//*[@id='username']"
    password = "password"
    ingresar = "ingresar-button"
    controlador = webdriver

    def __init__(self,controlador):
        self.controlador = controlador

    def ingresar(self,usuario,clave):
        wait = WebDriverWait(self.controlador, 15)

        # Ingresa Usuario
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='username']")))
        clickXPATH(self.controlador, "//*[@id='username']")
        inputElement(self.controlador, "username", usuario)

        clickXPATH(self.controlador, "//*[@id='password']")
        inputElement(self.controlador, "password", clave)

        clickXPATH(self.controlador, "//*[@id='ingresar-button']")
