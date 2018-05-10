__author__ = "mjdp"
__version__ = "1.0.0"
__email__ = "martin.delpercio@neoris.com"

import datetime
from libreriaUtiles import screenShotWeb

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#DEFINICIONES
driver = webdriver.Chrome("C:\\Webdrivers\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://newtours.demoaut.com")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 5)

screenShotWeb(driver,"Login","Login")

def selectElement(driver, nombre, valor):
    # Selecciona un Elemento
    element = wait.until(EC.presence_of_element_located((By.NAME, nombre)))
    select = Select(driver.find_element_by_name(nombre))
    select.select_by_visible_text(valor)

def inputElement(driver, nombre, valor):
    element = wait.until(EC.presence_of_element_located((By.NAME, nombre)))
    inputElement = driver.find_element_by_name(nombre)
    inputElement.send_keys(valor)

def clickElement(driver, nombre):
    element = wait.until(EC.presence_of_element_located((By.NAME, nombre)))
    driver.find_element_by_name(nombre).click()

# Ingresa Usuario
element = wait.until(EC.presence_of_element_located((By.NAME, "userName")))
driver.find_element_by_name("userName").clear()
driver.find_element_by_name("userName").send_keys("mercury")

# Ingresa Contraseeña
element = wait.until(EC.presence_of_element_located((By.NAME, "password")))
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("mercury")

# Hace click en el botón Login
clickElement(driver, "login")

driver.implicitly_wait(3)

# Verifica la ventana Flight Finder
assert (EC.presence_of_element_located((By.NAME, "findFlights")))

# Selecciona el Tipo <One Way>
inputElement(driver, "tripType", Keys.ARROW_RIGHT)

# Selecciona Dos Pasajeros
selectElement(driver, "passCount", "2")

# Selecciona Ciudad de Origen
selectElement(driver, "fromPort", "New York")

# Selecciona Mes del viaje
selectElement(driver, "fromMonth", "September")

# Selecciona Día del viaje
selectElement(driver, "fromDay", "16")

# Selecciona Ciudad de Destino
selectElement(driver, "toPort", "San Francisco")

# Selecciona Mes de regreso
selectElement(driver, "toMonth", "October")

# Selecciona Dia del regreso
selectElement(driver, "toDay", "23")

# Selecciona el Service Class
inputElement(driver, "servClass", Keys.ARROW_DOWN)

# Selecciona la Aerolinea
selectElement(driver, "airline", "Unified Airlines")

# Hace click en Find Flights
clickElement(driver, "findFlights")

driver.implicitly_wait(3)

# Verifica la ventana Select Flight
assert (EC.presence_of_element_located((By.NAME, "reserveFlights")))

# Selecciona el  vuelo de Salida
inputElement(driver, "outFlight", Keys.ARROW_DOWN)

#flightName = driver.findElement(By.xpath("//div[contains(@class, 'data_left'"))

#flightName = driver.find_element_by_xpath("//input[@name='outFlight']").text()

#print (flightName)

#SALIDA
driver.implicitly_wait(1)
driver.quit()

