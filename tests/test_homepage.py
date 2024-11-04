from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_homepage():
    # Set up Chrome options to run headlessly
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")  # Good for CI environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Useful for resource-limited environments

    # Update path to ChromeDriver (make sure the chromedriver binary is accessible from Jenkins)
    service = Service('/path/to/chromedriver')  # Replace with the correct path

    # Initialize the Chrome WebDriver with options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Access the locally hosted website on port 8080
        driver.get("http://localhost:8080")

        # Check for the presence of the "Welcome" text on the homepage
        time.sleep(2)  # Optional: wait a moment for the page to load
        assert "Welcome" in driver.find_element(By.TAG_NAME, "h1").text
        print("Homepage test passed.")
    finally:
        # Ensure the browser quits even if the test fails
        driver.quit()

if __name__ == "__main__":
    test_homepage()
