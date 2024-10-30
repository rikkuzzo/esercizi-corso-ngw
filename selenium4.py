import os
import re
import time
import logging
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json

# Configurazione del logger
logging.basicConfig(level=logging.INFO)

# Inizializzo le opzioni del browser Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# DIRECTORY DI DESTINAZIONE DEI FILE (sostituisci con il tuo percorso)
PATH = r"C:\Users\Terranova\Desktop\doc_albo_campania"

# Avvio del driver di Chrome con webdriver_manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def click_button_by_id(driver, button_id):
    """Funzione per cliccare su un pulsante identificato da un ID."""
    try:
        # Attendere che il pulsante sia cliccabile
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, button_id)))
        button.click()
        logging.info(f"Pulsante con ID '{button_id}' cliccato con successo.")
    except NoSuchElementException:
        logging.error(f"Pulsante con ID '{button_id}' non trovato.")
    except ElementClickInterceptedException:
        logging.error(f"Il clic sul pulsante con ID '{button_id}' è stato intercettato.")
    except Exception as e:
        logging.error(f"Errore sconosciuto: {e}")

# Apertura del sito
url = "https://www.albopretorionline.it/campania/alboente.aspx"
driver.get(url)

# Utilizzo della funzione per cliccare il pulsante 'cerca'
click_button_by_id(driver, "btCerca")
time.sleep(5)

def refresh_li_elements():
    """Funzione per recuperare tutti gli elementi <li> contenenti i documenti."""
    return driver.find_elements(By.XPATH, "//li[.//a[contains(@href,'download.aspx')]]")

def extract_dates(text):
    """Funzione per estrarre le date dal testo."""
    pattern = re.compile(r"dal (\d{2}-\d{2}-\d{4}) al (\d{2}-\d{2}-\d{4})")
    match = pattern.search(text)
    if match:
        return match.group(1), match.group(2)
    return None, None

# Recupero degli elementi contenenti i documenti
documents = refresh_li_elements()
document_data = []

# Creazione della directory per salvare i documenti
os.makedirs(PATH, exist_ok=True)

# Estrazione delle informazioni e download dei documenti
for doc in documents:
    text = doc.text
    start_date, end_date = extract_dates(text)
    act_number = doc.find_element(By.CSS_SELECTOR, ".doc-number").text
    doc_name = doc.find_element(By.CSS_SELECTOR, ".doc-name").text
    download_link = doc.find_element(By.TAG_NAME, "a").get_attribute("href")
    today_date = datetime.today().strftime("%Y-%m-%d")

    try:
        doc_response = requests.get(download_link)
        local_filename = os.path.join(PATH, f"{doc_name}.pdf")
        with open(local_filename, 'wb') as file:
            file.write(doc_response.content)
    except Exception as e:
        logging.error(f"Errore durante il download di {download_link}: {e}")
        continue

    document_data.append({
        "Data di inizio pubblicazione": start_date,
        "Data di fine pubblicazione": end_date,
        "Numero di atto": act_number,
        "Nome del documento": doc_name,
        "Link per scaricare il documento": download_link,
        "Data odierna": today_date,
        "Percorso MinIO": f"REGIONE_CAMPANIA/ALBO_PRETORIO/{doc_name}.pdf"
    })

    time.sleep(1)

# Chiusura del driver
driver.quit()

# Salvataggio dei dati in un file JSON
with open(os.path.join(PATH, 'documenti.json'), 'w') as f:
    json.dump(document_data, f, indent=4)

# Stampa delle informazioni raccolte
for data in document_data:
    print(data)
