import os
import logging
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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

    # Clicca il pulsante Servizi 
    logging.info("Cliccando sul pulsante 'Servizi'...")
    services_button = driver.find_element(By.LINK_TEXT, 'Servizi')
    services_button.click()

    # Clicca il tariffario
    logging.info("Cliccando sul link 'Tariffario'...")
    tariffario_link = driver.find_element(By.LINK_TEXT, 'Tariffario')
    tariffario_link.click()

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
