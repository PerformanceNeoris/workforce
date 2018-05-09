
import datetime
from SeleniumScripts.CVMainPage import *
from libreriaUtiles import screenShotWeb
from SeleniumScripts.CVGeneral import *
from SeleniumScripts.CVMainPage import *
from SeleniumScripts.CVLoginPage import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#DEFINICIONES
driver = webdriver.Chrome("C:\\Webdrivers\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://www.cablevisionfibertel.com.ar/")
driver.maximize_window()
driver.implicitly_wait(1)
wait = WebDriverWait(driver, 5)
usuario = "federicomarilungo@gmail.com"
clave = "Cable12"

Main = CVMainPage(driver)
Main.clickIngresar()
'''''
Login = CVLoginPage(driver)
Login.ingresar(driver, usuario, clave)
'''''








