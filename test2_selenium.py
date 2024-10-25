
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

logging.basicConfig(level=logging.INFO)


options = Options()
options.add_argument("--start-maximized") 


driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("https://www.amazon.it")


time.sleep(2)


try:
    cookies_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "sp-cc-accept"))
    )
    cookies_button.click()
    logging.info("Cookies accettati con successo.")
except (NoSuchElementException, TimeoutException):
    logging.warning("Il bottone dei cookies non è stato trovato o non è cliccabile.")

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
product_to_search = "laptop"  # Puoi cambiare il prodotto da cercare
search_box.send_keys(product_to_search)
search_box.send_keys(Keys.RETURN)


try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".s-main-slot"))
    )


    products = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")
    
    for product in products[:10]: 
        try:
            title = product.find_element(By.CSS_SELECTOR, "h2 a span").text
            price = product.find_element(By.CSS_SELECTOR, ".a-price-whole").text
            print(f"Prodotto: {title}, Prezzo: {price}€")
        except NoSuchElementException:
           
            continue
except TimeoutException:
    logging.warning("La ricerca dei prodotti ha impiegato troppo tempo.")


driver.quit()
