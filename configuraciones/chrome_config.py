import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

            #Configuracion del navegador
class Configuracion(webdriver.Chrome):
    def __init__(self, path_user="",
                 teardowm=False, base_url="", class_name=None):
        self.teardowm = teardowm
        self.base_url = base_url
        self.PathUser = path_user
        os.environ['PATH'] = self.PathUser
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        super(Configuracion, self).__init__(options=chr_options)
        self.implicitly_wait(20)

        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardowm:
            self.quit()
    def open(self):
        self.get(self.base_url)
        
            #Metodo de clicar
    def clicar_en(self, by=By.ID, path_name=""):
        id_selected = self.find_element(by, path_name)
        id_selected.click()

            #Metodo de escribir
    def escribir_en(self, by=By.ID, path_name="", value=""):
        element_by = self.find_element(by, path_name)
        element_by.clear()
        element_by.send_keys(value)

            #Metodo de añadir por teclado
    def texto_por_teclado(self,by=By.ID,path="",Key= Keys.ENTER):
        element_by = self.find_element(by, path)
        element_by.send_keys(Key)