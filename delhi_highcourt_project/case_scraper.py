from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def fetch_case_details(case_type, case_number, case_year):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # <-- Added this line

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get('https://delhihighcourt.nic.in/app/get-case-type-status')

        wait = WebDriverWait(driver, 30)

        # Fill Case Type
        case_type_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'case_type')))
        case_type_dropdown.send_keys(case_type)

        # Fill Case Number
        case_number_input = wait.until(EC.presence_of_element_located((By.ID, 'case_number')))
        case_number_input.send_keys(case_number)

        # Fill Case Year
        case_year_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'case_year')))
        case_year_dropdown.send_keys(case_year)

        print("\n[Action Required] Please solve the Captcha in the browser.")
        input("After solving, press Enter here to continue...")

        # Click Submit
        submit_button = driver.find_element(By.XPATH, '//button[contains(text(),"Submit")]')
        driver.execute_script("arguments[0].click();", submit_button)

        # Wait for result
        case_table = wait.until(EC.presence_of_element_located((By.ID, 'caseTable')))
        case_table_html = case_table.get_attribute('outerHTML')

        input("\n[INFO] Case details fetched. Check the browser. Press Enter to close it")
        return {'status': 'success', 'case_details_html': case_table_html}

    except Exception as e:
        print(f"\n[ERROR] Something went wrong: {e}")
        input("Check the browser for error. Press Enter to close...")
        return {'status': 'error', 'message': str(e)}

    finally:
        driver.quit()
