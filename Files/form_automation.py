import csv
import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(
    filename="submission.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Launch Chrome
driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)

driver.maximize_window()

# Open the local HTML form
file_path = os.path.abspath("form.html")
driver.get("file://" + file_path)

# Read data from CSV
with open("data.csv", newline="", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    # Loop through every record
    for row in reader:

        try:
            # Check for missing required fields
            if not row["Name"] or not row["Email"]:
                logging.warning(f"Skipped row because of missing data: {row}")
                print("Skipped a row due to missing data.")
                continue


            # ---------- Name ----------
            name = driver.find_element(By.ID, "name")
            name.clear()
            name.send_keys(row["Name"])

            # ---------- Email ----------
            email = driver.find_element(By.ID, "email")
            email.clear()
            email.send_keys(row["Email"])

            # ---------- Gender ----------
            if row["Gender"] == "Male":
                driver.find_element(By.ID, "male").click()
            else:
                driver.find_element(By.ID, "female").click()

            # ---------- Experience Dropdown ----------
            experience = Select(driver.find_element(By.ID, "experience"))
            experience.select_by_visible_text(row["Experience"])

            # ---------- Automation Checkbox ----------
            automation = driver.find_element(By.ID, "automation")

            if row["Automation"] == "Yes":
                if not automation.is_selected():
                    automation.click()
            else:
                if automation.is_selected():
                    automation.click()

            # ---------- Submit Form ----------
            driver.find_element(By.TAG_NAME, "button").click()

            # Wait to see the submission
            time.sleep(1)

            # Log successful submission
            logging.info(f"{row['Name']} submitted successfully.")

            print(f"{row['Name']} submitted successfully.")

            # Refresh page for next record
            driver.refresh()
            time.sleep(1)

        except Exception as e:

            logging.error(f"{row['Name']} submission failed. Error: {e}")

            print(f"Error submitting {row['Name']}: {e}")

# Close browser
driver.quit()

print("All records processed.")