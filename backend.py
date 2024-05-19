from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

def run_backend(username, password, contest, question):
    driver_path = r'C:\Users\manasakavya\Downloads\chromedriver-win64\chromedriver.exe'  # Ensure the full path to chromedriver.exe
    service = Service(driver_path)  # Create a Service object with the driver path
    options = webdriver.ChromeOptions()  # Create ChromeOptions if needed

    driver = webdriver.Chrome(service=service, options=options)  # Pass the service and options to the Chrome driver

    try:
        driver.get('https://www.hackerrank.com/auth/login')
        
        driver.find_element_by_id('input-1').send_keys(username)
        driver.find_element_by_id('input-2').send_keys(password)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        
        time.sleep(5)  # Wait for the page to load

        driver.get(f'https://www.hackerrank.com/contests/{contest}/challenges')
        
        time.sleep(5)  # Wait for the page to load

        search_box = driver.find_element_by_xpath('//input[@placeholder="Search a problem"]')
        search_box.send_keys(question)
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(5)  # Wait for the results to load
        
        question_link = driver.find_element_by_xpath('//a[contains(@href, "/challenges/")]')
        question_link.click()
        
        time.sleep(5)  # Wait for the page to load

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
