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
        print(Fore.GREEN + f"Retrieving {URL}...")
        page.goto(url=URL)

        #Wait for the search box to load and add a time.sleep to avoid getting caught
        page.wait_for_selector('input[role="combobox"]')
        time.sleep(random.uniform(0.5, 1.5))

        #Type out our query
        print(Fore.GREEN + "Entering Query...")
        page.locator('input.fontBodyMedium.searchboxinput.xiQnY').click()
        page.locator('input.fontBodyMedium.searchboxinput.xiQnY').type("Gyms in Mumbai", delay=random.uniform(100, 300))
        page.keyboard.press('Enter')
        page.wait_for_selector('div.Ntshyc')

        #We can't perform API interception for google maps, because no valid json is there
        #We will do basic HTML scraping now
        NAME = []
        PHONE_NUMBER = []
        ADDRESS = []
        WEBSITE = []
        RATING = []

        i = 0
        while True:
            print(Fore.RED + "->" + Fore.GREEN + f"Clicking gym card {i + 1}...")
            gym_card = page.locator('a.hfpxzc').nth(i)
            gym_card.hover()
            gym_card.click()
            #wait for the gym_info to load
            page.wait_for_selector('div.m6QErb.DxyBCb.kA9KIf')
            page.wait_for_selector('img[decoding="async"]')
            time.sleep(4)

            #Retrieve the stuff
            name = page.locator('h1.DUwDvf.lfPIob').first
            NAME.append(name.inner_text())

            phone_number_section = page.locator('button[data-item-id^="phone:"] div.rogA2c ').filter(
                has=page.locator('div.HMy2Jf')
            ).filter(
                has=page.locator('div.gSkmPd.fontBodySmall.CuiGbf.DshQNd')
            )
            phone_number = phone_number_section.locator('div.Io6YTe.fontBodyMedium.kR99db.fdkmkc')
            PHONE_NUMBER.append(phone_number.inner_text())
            

            address_element = page.locator('div.Io6YTe.fontBodyMedium.kR99db.fdkmkc ').first
            ADDRESS.append(address_element.inner_text())

            try:
                website_element = page.locator('a[aria-label^="Website:"] div.AeaXub div.rogA2c.ITvuef div.Io6YTe.fontBodyMedium.kR99db.fdkmkc ')
                WEBSITE.append(website_element.inner_text())
            except:
                WEBSITE.append(None)

            rating_element = page.locator('div.F7nice span[aria-hidden="true"]')
            RATING.append(rating_element.inner_text())

            #move to the next card
            gym_card_ = page.locator('a.hfpxzc').nth(i+1)
            gym_card_.hover()
            page.mouse.wheel(0, 1000)

            i+=1






if __name__ == '__main__':
    run()