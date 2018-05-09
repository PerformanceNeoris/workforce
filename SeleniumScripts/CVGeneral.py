
__author__ = "mjdp"
__version__ = "1.0.0"
__email__ = "mdelpercio@teco.com.ar"

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def selectElement(driver, nombre, valor):
    wait = WebDriverWait(driver, 5)
    # Selecciona un Elemento
    element = wait.until(EC.presence_of_element_located((By.NAME, nombre)))
    select = Select(driver.find_element_by_name(nombre))
    select.select_by_visible_text(valor)

def inputElement(driver, nombre, valor):
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.presence_of_element_located((By.NAME, nombre)))
    inputElement = driver.find_element_by_name(nombre)
    inputElement.send_keys(valor)

def clickElement(driver, nombre):
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.presence_of_element_located((By.NAME, nombre)))
    driver.find_element_by_name(nombre).click()

def clickXPATH(driver, nombre):
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.presence_of_element_located((By.XPATH, nombre)))
    driver.find_element_by_xpath(nombre).click()

def clickID(driver, nombre):
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.presence_of_element_located((By.ID, nombre)))
    driver.find_element_by_id(nombre).click()
