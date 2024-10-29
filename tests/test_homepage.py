from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def test_homepage():
    # Set up the Chrome WebDriver (ensure ChromeDriver is installed)
    service = Service('/path/to/chromedriver')  # Update path as needed
    driver = webdriver.Chrome(service=service)
    driver.get("http://localhost:8080")  # Test the running website on port 8080

    # Check for "Welcome" text in the homepage
    assert "Welcome" in driver.find_element(By.TAG_NAME, "h1").text
    print("Homepage test passed.")

    driver.quit()

if __name__ == "__main__":
    test_homepage()
