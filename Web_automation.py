from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time




def launchBrowser(*url):
			
	driver = webdriver.Chrome(r"/Users/kartikaysingh/Desktop/Projects/Code_snippets/chromedriver")
	# opening the browser urls
	driver.get(url)
	print(driver.title)
	time.sleep(5)
	return driver

driver = launchBrowser()

# find input fields to be filled
# fill Name input
driver.find_element(By.NAME, "name").send_keys('name')
driver.find_element(By.NAME, "email").send_keys('my_email@gmail.com')
driver.find_element(By.NAME, "phone").send_keys('9810567890')
Select(driver.find_element(By.NAME, "Gender")).select_by_value('Male')
driver.find_element(By.NAME, "Date of Birth").send_keys("14/06/2001")
driver.find_element_by_xpath('//*[@id="payment"]/div[2]/div[4]/div[2]/button').click()
time.sleep(30)

# pay through easy EMI page
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/img').click()
time.sleep(20)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/ul/li[4]').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="captcha"]').click()


time.sleep(100)##