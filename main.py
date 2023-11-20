from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

MESSAGE = 'Bom dia!'

class WhatsappGoodMorning:

	def __init__(self, options):
		self.driver = webdriver.Chrome(options=options)
		self.driver.get(f"https://web.whatsapp.com/")
		self.logged = False

	def login(self):
		input('Pressione ENTER após escanear o QR code')
		self.logged = True

	def send_message(self):
		target = self.driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[2]/div/div/div[11]/div/div/div/div[2]/div[1]/div[1]/div/span')
		target.click()

		target = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
		target.click()
		target.send_keys(MESSAGE)
		target.send_keys(Keys.ENTER)


bot = WhatsappGoodMorning(chrome_options)
bot.login()
bot.send_message()
