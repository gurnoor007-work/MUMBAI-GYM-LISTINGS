from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
import re
import time
import random
from colorama import Fore, Style, init
init(autoreset=True)

#create a function to organise everything
def run():
    with Stealth().use_sync(sync_playwright()) as p:
        #create a browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        #Go to the desired URL
        URL = "https://www.google.com/maps"
        print(Fore.GREEN + f"Retrieving {URL}")
        page.goto(url=URL)

        #Wait for the search box to load and add a time.sleep to avoid getting caught
        page.wait_for_selector('input[role="combobox"]')
        time.sleep(random.uniform(0.5, 1.5))

        #Type out our query
        page.locator('input.fontBodyMedium.searchboxinput.xiQnY').click()
        page.locator('input.fontBodyMedium.searchboxinput.xiQnY').type("Gyms in Mumbai", delay=random.uniform(100, 300))
        page.keyboard.press('Enter')
        page.wait_for_selector('div.Ntshyc')

        #





if __name__ == '__main__':
    run()