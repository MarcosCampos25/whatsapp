from classes.Driver import Driver
from classes.WhatsApp import WhatsApp
from classes.Portisur import Portisur

NRO = ''
MSG = Portisur()
MSG = MSG.obtener_ofertas()

driver = Driver()
driver = driver.set_up_driver(False)

whatsapp_instance = WhatsApp()
whatsapp_instance.login(driver)
whatsapp_instance.send_message(driver, NRO, MSG)