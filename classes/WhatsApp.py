import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import qrcode


    
class WhatsApp:
    url_base = 'http://web.whatsapp.com/'
    url_msg = url_base + 'send?phone='
    

    def login(self, driver):
        try:
            driver.get(self.url_base)
            wait = WebDriverWait(driver, timeout=45)
            qr = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@data-ref]')))
            result = qr.get_attribute('data-ref')

            if result:
                print("\n📟 QR escaneable desde consola:")
                qr = qrcode.QRCode(border=1)
                qr.add_data(result)
                qr.make()
                qr.print_ascii(invert=True)
            else:
                print("❌ No se detectó un QR válido en la imagen.")
                return
            
            try:
                bnt_continuar = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Continuar')]")))
                bnt_continuar.click()
            except Exception as e:
                print("Continuar no encontrado...")
            
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Lista de chats"]')))
            return True
        except Exception as e:
            print(e)

    def send_message(self, driver, nro, message):
        driver.get(self.url_msg + nro)
        txt = WebDriverWait(driver, timeout=45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Escribe un mensaje"] p.selectable-text.copyable-text')))
        txt.click()
        message_splited = message.split('\n')
        for message in message_splited:
            txt.send_keys(message)
            actions = ActionChains(driver)
            actions.key_down(Keys.ALT).send_keys(Keys.ENTER).key_up(Keys.ALT).perform()
        txt.send_keys('.\n')
        time.sleep(3)
        return True
    

