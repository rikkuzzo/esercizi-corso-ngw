import os
import logging
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Configurazione logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Scarica documenti
def download_file(url, folder):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            filename = os.path.join(folder, os.path.basename(url))
            with open(filename, 'wb') as f:
                f.write(response.content)
            logging.info(f'Scaricato: {filename}')
        else:
            logging.error(f'Errore durante il download di {url}: {response.status_code}')
    except Exception as e:
        logging.error(f'Errore durante il download di {url}: {e}')

# Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Si collega al sito
    logging.info("Apertura della pagina principale di ARPA Lazio...")
    driver.get('https://www.arpalazio.it/')

    # Chiudere o accettare l'avviso sui cookie se presente
    try:
        # Aspetta fino a 15 secondi per il popup dei cookie
        cookie_alert = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.cookiealert-container'))
        )
        accept_button = cookie_alert.find_element(By.XPATH, ".//a[contains(text(), 'Accetta') or contains(text(), 'Accetto')]")  # Modifica se il testo del pulsante è diverso
        accept_button.click()
        logging.info("Avviso sui cookie accettato.")
    except TimeoutException:
        logging.warning("Nessun avviso sui cookie trovato.")

    # Clicca il pulsante Servizi 
    logging.info("Cliccando sul pulsante 'Servizi'...")
    try:
        services_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'Servizi'))
        )
        services_button.click()
    except TimeoutException:
        logging.error("Timeout: Il pulsante 'Servizi' non è stato trovato o non è cliccabile.")

    # Clicca il tariffario
    logging.info("Cliccando sul link 'Tariffario'...")
    try:
        tariffario_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Tariffario'))
        )
        tariffario_link.click()
    except TimeoutException:
        logging.error("Timeout: Il link 'Tariffario' non è stato trovato o non è cliccabile.")

    # Crea una cartella
    download_folder = 'Documenti_Tariffario'
    os.makedirs(download_folder, exist_ok=True)

    # Scarica documenti
    logging.info("Scaricando i documenti presenti nella pagina...")
    links = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf') or contains(@href, '.doc')]")
    
    if not links:
        logging.warning("Nessun documento trovato per il download.")

    for link in links:
        document_url = link.get_attribute('href')
        if document_url: 
            download_file(document_url, download_folder)

except NoSuchElementException as e:
    logging.error(f'Elemento non trovato: {e}')
except Exception as e:
    logging.error(f'Si è verificato un errore: {e}')
finally:
    # Chiusura Chrome
    logging.info("Chiusura del browser...")
    driver.quit()
