import telebot
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

# Configurazione del logging
logging.basicConfig(level=logging.INFO)

# Inserisci qui il token del bot Telegram
API_TOKEN = '7954433263:AAFjwI7-kNReRU-CvX5zu4xaOgzHky2ieok'

# Crea un'istanza del bot
bot = telebot.TeleBot(API_TOKEN)

# Funzione per cercare prodotti su Amazon
def cerca_prodotti_su_amazon(prodotto_da_cercare):
    options = Options()
    options.add_argument("--headless")  # Modalità headless, non apre il browser visivamente
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Vai alla pagina di Amazon
        driver.get("https://www.amazon.it")
        time.sleep(2)  # Attendi il caricamento della pagina

        # Accetta i cookies, se necessario
        try:
            cookies_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "sp-cc-accept"))
            )
            cookies_button.click()
            logging.info("Cookies accettati con successo.")
        except (NoSuchElementException, TimeoutException):
            logging.warning("Il bottone dei cookies non è stato trovato o non è cliccabile.")

        # Cerca il prodotto
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(prodotto_da_cercare)
        search_box.send_keys(Keys.RETURN)

        # Attendi il caricamento della pagina dei risultati
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".s-main-slot"))
        )

        # Estrai i prodotti con titolo e prezzo
        prodotti = []
        products = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")

        for product in products[:5]:  # Limitiamo a 5 risultati
            try:
                title = product.find_element(By.CSS_SELECTOR, "h2 a span").text
                price = product.find_element(By.CSS_SELECTOR, ".a-price-whole").text
                prodotti.append(f"Prodotto: {title}, Prezzo: {price}€")
            except NoSuchElementException:
                continue

        return prodotti

    finally:
        driver.quit()

# Gestore del comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ciao! Inviami il nome di un prodotto da cercare su Amazon.")

# Gestore dei messaggi (prodotti da cercare)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prodotto_da_cercare = message.text
    bot.reply_to(message, f"Sto cercando {prodotto_da_cercare} su Amazon, attendi un attimo...")

    # Effettua la ricerca su Amazon
    risultati = cerca_prodotti_su_amazon(prodotto_da_cercare)

    if risultati:
        for prodotto in risultati:
            bot.send_message(message.chat.id, prodotto)
    else:
        bot.send_message(message.chat.id, "Non ho trovato nessun prodotto con questo nome.")

# Avvia il bot
bot.polling()
