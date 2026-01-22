from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://chulo-solutions.github.io/qa-internship/")
driver.maximize_window()
wait = WebDriverWait(driver, 3)

# Enter Username
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("user123")

# Enter Password
driver.find_element(By.ID, "password").send_keys("Test@1234")

# Enter Credit Card
driver.find_element(By.ID, "creditCard").send_keys("4111111111111111")

# Enter Phone
driver.find_element(By.ID, "phone").send_keys("(123) 456-7890")

# Submit
driver.find_element(By.ID, "submit").click()

# Verify Success Message
success_msg = wait.until(
    EC.visibility_of_element_located((By.ID, "successMessage"))
)

assert "success" in success_msg.text.lower()
print("✅ Test Passed: Registration successful")

driver.quit()

