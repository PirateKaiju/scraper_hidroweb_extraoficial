from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "http://www.snirh.gov.br/hidroweb/publico/medicoes_historicas_abas.jsf"

options = webdriver.FirefoxOptions()  # Opcoes do driver
options.set_preference("browser.download.dir", "\\home\\antonio")
options.set_preference("browser.download.useDownloadDir", "true")
options.set_preference(
    "browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
# options.add_argument('--headless')  # Inicia em modo headless
# options.add_argument('window-size=1920x1080')

driver = webdriver.Firefox(firefox_options=options)
driver.get(URL)

driver.maximize_window()

# btnConsultar = driver.find_element_by_id("form:fsListaEstacoes:bt")
btnConsultar = driver.find_element_by_xpath(
    "//*[@id='form:fsListaEstacoes:bt']")  # Equivalente ao anterior

textBoxCodigo = driver.find_element_by_id("form:fsListaEstacoes:codigoEstacao")
textBoxCodigo.send_keys("42440000")
# Necessario esperar texto existir no formulario
try:
    btnPresser = WebDriverWait(driver, 4).until(
        EC.text_to_be_present_in_element(
            (By.ID, "form:fsListaEstacoes:codigoEstacao"))  # Altera
        # len(str(textBoxCodigo.get_attribute('value'))) != 0
    )
finally:
    btnConsultar.click()
    time.sleep(3)  # ARRUMAR
    # TEM QUE CLICAR NO DADOS CONVENCIONAIS, ELE NAO FAZ SOZINHO
    driver.find_element_by_partial_link_text("Convencionais").click()
    time.sleep(2)
    # TALVEZ OUTRO JEITO
    '''btnDados = driver.find_element_by_xpath(
        "//*[@name='Dados Convencionais']")
    btnDados.click()'''

    chkboxSelect = driver.find_element_by_id(
        "form:fsListaEstacoes:fsListaEstacoesC:j_idt179:table:0:ckbSelecionada"
    )
    chkboxSelect.click()
    # radioTipoArquivo = driver.find_element_by_id(
    #    "form:fsListaEstacoes:fsListaEstacoesC:radTipoArquivo:1")
    time.sleep(2)
    radioTipoArquivo = driver.find_element_by_xpath(
        "//*[@id='form:fsListaEstacoes:fsListaEstacoesC:radTipoArquivo:1']")
    driver.execute_script("arguments[0].click();", radioTipoArquivo)  # Operacional
    # radioTipoArquivo.click()
    # driver.find_element_by_partial_link_text("(.TXT)").click()
    # driver.find_element_by_css_selector(
    #    "input[type='radio'][value='2']/..").click()
    time.sleep(2)
    btnDownload = driver.find_element_by_id(
        "form:fsListaEstacoes:fsListaEstacoesC:btBaixar")
    btnDownload.click()
    # print(btnDownload.get_attribute('href'))

# print(textBoxCodigo.get_attribute('value')) #Teste


# TEM QUE CLICAR NO DADOS CONVENCIONAIS, ELE NAO FAZ SOZINHO
# time.sleep(5)  # Funciona, mas nao eh ideal

# driver.get("http://www.snirh.gov.br/hidroweb/publico/medicoes_historicas_abas.jsf#dadosConvencionais")
# tab = driver.find_element_by_name('Dados Convencionais')
# tab.click()

# btnConsultar.click()

'''btnConsultar = driver.find_element_by_id("form:fsListaEstacoes:bt")
textBoxCodigo = driver.find_element_by_id("form:fsListaEstacoes:codigoEstacao")

textBoxCodigo.send_keys("42440000")
btnConsultar.click()'''
