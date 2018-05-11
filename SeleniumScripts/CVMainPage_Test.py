__author__ = "mjdp"
__version__ = "1.0.0"
__email__ = "mdelpercio@teco.com.ar"

import time
import pyautogui
from SeleniumScripts.CVLoginPage import CVLoginPage
from SeleniumScripts.CVMainPage import CVMainPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#DEFINICIONES
global URL
URL="http://www.cablevisionfibertel.com.ar"
driver = webdriver.Chrome('C:\\Webdrivers\\chromedriver.exe')
#driver.set_page_load_timeout(10)
driver.get(URL)
print(driver.title)
time.sleep(5)
driver.maximize_window()
wait = WebDriverWait(driver, 5)

usuario = "martinjavierd@gmail.com"
clave = "CrudSec2"

CVMain = CVMainPage(driver)
CVMain.clickIngresar()

pyautogui.moveTo(5, 505)
time.sleep(1)
pyautogui.click(5, 505,3)

CVLogin = CVLoginPage(driver)
CVLogin.ingresar(usuario, clave)

#SALIDA
time.sleep(5)
driver.quit()









