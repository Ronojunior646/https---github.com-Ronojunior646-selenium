from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def send_message_to_user(user_id, message, username, password):
    driver = webdriver.Chrome()

    try:
        driver.get("https://betting.co.zw/authentication/login")
        time.sleep(5)  # Adding a delay to ensure page loading

        # Entering username
        username_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/div[3]/ng-component/idb-ath-login/idb-ath/au-form/form/fieldset[1]/div[1]/div[2]/input"))
        )
        username_input.clear()
        username_input.send_keys(username)

        # Entering password
        password_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='password']"))
        )
        password_input.send_keys(password)

        # Clicking login button
        login_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='buttonLoginSubmitLabel']"))
        )
        login_button.click()

        # Waiting for page to load after login
        time.sleep(3)

        # Clicking another login button (if needed)
        # login_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        # )
        # login_button.click()

        # Adding a delay after login to ensure page loading
        time.sleep(3)

        # Clicking on chat button
        chat_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Chat')]"))
        )
        chat_button.click()

        # Entering user ID
        user_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user_id']"))
        )
        user_input.send_keys(user_id)

        # Entering message
        message_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))
        )
        message_input.send_keys(message)

        # Clicking send button
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Send')]"))
        )
        send_button.click()

        print("Message sent successfully.")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # driver.quit()
        pass

# User ID and message
user_id = "542884"
message = "💰✅ HERE WE GO TOGETHER WHATSAPP 2️⃣5️⃣4️⃣1️⃣0️⃣4️⃣5️⃣2️⃣0️⃣3️⃣3️⃣7️⃣ LET'S KEEP ON WINNING IF YOU HAVE BEING LOSING/share_bet:3655967717💰"
username = "718361410"
password = "kevin1"

# Send the message to the user
send_message_to_user(user_id, message, username, password)
