__author__ = "mjdp"
__version__ = "1.0.0"
__email__ = "mdelpercio@teco.com.ar"

import time
from SeleniumScripts.CVLoginPage import CVLoginPage
from SeleniumScripts.CVMainPage import CVMainPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#DEFINICIONES
global URL
URL="http://www.cablevisionfibertel.com.ar"
#URL="https://auth.cablevision.com.ar/saml/authenticationendpoint/login.do?sessionDataKey=1ed31b8f-db5d-465c-bdc3-3b331ccb7f15&relyingParty=CablevisionDigital&type=samlsso&sp=CablevisionDigital&isSaaSApp=false&authenticators=BasicAuthenticator:LOCAL#"
driver = webdriver.Chrome('C:\\Webdrivers\\chromedriver.exe')
#driver.set_page_load_timeout(10)
driver.get(URL)
print(driver.title)
time.sleep(5)
driver.maximize_window()
wait = WebDriverWait(driver, 5)

usuario = "federicomarilungo@gmail.com"
clave = "cable12"

#Crea el archivo
file = open("URL.txt","w")
file.close()

CVMain = CVMainPage(driver)
CVMain.clickIngresar()

driver.quit()

file = open("URL.txt", "r")
textURL = file.read()
print(textURL)

driver = webdriver.Chrome('C:\\Webdrivers\\chromedriver.exe')
driver.get(textURL)
time.sleep(5)
file.close()
driver.maximize_window()
wait = WebDriverWait(driver, 5)

CVLogin = CVLoginPage(driver)
CVLogin.ingresar(usuario, clave)

#SALIDA
time.sleep(5)
driver.quit()









