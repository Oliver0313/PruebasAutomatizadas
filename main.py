from datetime import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from configuraciones.Amazon import Amazon_test
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging

                #Reporte de las pruebas en HTML
logging.basicConfig(filename='Reporte_de_los_Test.html', level=logging.INFO,
                    format=' %(levelname)s- %(asctime)s - %(message)s')

class HTMLFormatter(logging.Formatter):
    def format(self, record):
        level_name = record.levelname
        message = record.msg
        timestamp = self.formatTime(record, self.datefmt)
        return f'<p>{timestamp} - {level_name}: {message}</p>'

html_formatter = HTMLFormatter()

for handler in logging.root.handlers:
    handler.setFormatter(html_formatter)

with Amazon_test() as test:

                #Inicio del Test
    test.open()
    
try:
                #Aceptar las cookies del sitio
    time.sleep(5)
    test.hacer_click(path_name="sp-cc-accept")
    test.implicitly_wait(10)

                #Primer Test de navegar al carrito
    time.sleep(5)
    test.hacer_click(path_name="nav-cart")
    test.implicitly_wait(10)
    logging.info("Primer Test: navegar hacia carrito: Hecho")
    time.sleep(5)
    test.save_screenshot("Captura_1.png")


                #Segundo Test: navegar hacia la pagina principal de nuevo
    time.sleep(5)
    test.hacer_click(path_name="nav-logo-sprites")
    test.implicitly_wait(10)
    logging.info("Segundo Test: navegar hacia la pagina principal de nuevo: Hecho")
    time.sleep(5)
    test.save_screenshot("Captura_2.png")


                    #Tercer Test: Poner direccion del Envio a Estados Unidos
    time.sleep(5)
    test.hacer_click(path_name="nav-global-location-popover-link")
    test.implicitly_wait(10)
    test.escribir(By.ID,"GLUXZipUpdateInput", "")
    time.sleep(10)
    test.hacer_click(path_name="GLUXCountryValue")
    test.implicitly_wait(20)
    test.hacer_click(path_name="GLUXCountryList_2")
    test.implicitly_wait(10)
    logging.info("Tercer Test: Poner direccion del Envio a Estados Unidos: Hecho")
    time.sleep(5)
    test.save_screenshot("Captura_3.png")
 

                #Cuarto Test: buscar Audifonos en Amazon
    time.sleep(3)
    test.escribir(By.ID,"twotabsearchtextbox", "Audifonos")
    time.sleep(1)
    test.clicar_en(path_name="nav-search-submit-button")
    logging.info("Cuarto Test: buscar Audifonos en Amazon: Hecho")
    time.sleep(5)
    test.save_screenshot("Captura_4.png")


                #Quinto Test: Busqueda de Audifonos más recientes
    time.sleep(3)
    test.hacer_click(path_name="a-autoid-0-announce")
    time.sleep(3)
    test.clicar_en(path_name="s-result-sort-select_4")
    logging.info("Quinto Test: Busqueda de Audifonos más recientes: Hecho")
    time.sleep(5)
    test.save_screenshot("Captura_5.png")
    time.sleep(5)

except Exception as e:
    logging.error(f" Error en las pruebas: {e}")
finally:

    test.close()

