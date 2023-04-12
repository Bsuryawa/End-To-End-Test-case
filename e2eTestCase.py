from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
service_obj = Service (r"C:\Users\BHAGYASHRI\Downloads\chromedriver_win32 (1)\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[text()='Shop']").click()
driver.execute_script("window.scrollBy(0,400);")
phones = driver.find_elements(By.CLASS_NAME, "card h-100")
for phone in phones:
    phoneName = phone.find_elements(By.CLASS_NAME,"card-title").text()
    if phoneName == "Blackberry":
        phone.find_element(By.CSS_SELECTOR, "button[class*='btn-info']").click()
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message= driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
print(message)
assert message == "Success! Thank you! Your order will be delivered in next few weeks :-)."

driver.close()
