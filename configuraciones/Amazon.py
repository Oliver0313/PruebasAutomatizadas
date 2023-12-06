from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from configuraciones.chrome_config import Configuracion

class Amazon_test(Configuracion):
    def __init__(self, path_driver=r"C:\Users\mende\Desktop\Mis cosas\Prueba Automatizada\chromedriver.exe"):
        super(Amazon_test, self).__init__(path_driver, base_url="https://amazon.es/",
                                                 class_name=Amazon_test)
    #Metodos
    def hacer_click(self, by=By.ID, path_name=""):
        id_selected = self.find_element(by, path_name)
        id_selected.click()

    def escribir(self, by=By.ID, path_name="", value=""):
        element_by = self.find_element(by, path_name)
        element_by.clear()
        element_by.send_keys(value)  

    def seleccionar_css(self, by=By.CSS_SELECTOR, css=''):
        btn = self.find_element(by, css)
        btn.click()

