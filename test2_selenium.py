from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Configurazione del logger
logging.basicConfig(level=logging.INFO)

# Inizializzo le opzioni del browser Chrome
options = Options()
options.add_argument("--start-maximized")  # Apre il browser in modalità massimizzata

# Utilizza ChromeDriverManager per gestire automaticamente il driver di Chrome
driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Vai alla pagina di Amazon
driver.get("https://www.amazon.it")

# Aspetta qualche secondo per il caricamento della pagina
time.sleep(2)

# Accetta i cookies
try:
    cookies_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "sp-cc-accept"))
    )
    cookies_button.click()
    logging.info("Cookies accettati con successo.")
except (NoSuchElementException, TimeoutException):
    logging.warning("Il bottone dei cookies non è stato trovato o non è cliccabile.")

# Inserisci il testo nella barra di ricerca
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
product_to_search = "laptop"  # Puoi cambiare il prodotto da cercare
search_box.send_keys(product_to_search)
search_box.send_keys(Keys.RETURN)

# Estrai le informazioni sui prodotti
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".s-main-slot"))
    )

    # Estrazione di titoli e prezzi dei prodotti dalla prima pagina
    products = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")
    
    for product in products[:10]:  # Limitiamo a 10 prodotti
        try:
            title = product.find_element(By.CSS_SELECTOR, "h2 a span").text
            price = product.find_element(By.CSS_SELECTOR, ".a-price-whole").text
            print(f"Prodotto: {title}, Prezzo: {price}€")
        except NoSuchElementException:
            # Gestione del caso in cui il prodotto non abbia prezzo o titolo
            continue
except TimeoutException:
    logging.warning("La ricerca dei prodotti ha impiegato troppo tempo.")

# Chiudi il browser
driver.quit()
