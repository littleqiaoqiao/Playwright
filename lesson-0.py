from playwright.sync_api import sync_playwright
# import time

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)

page1 = browser.new_page()
page1.goto('https://lumierecreation.com/?srsltid=AfmBOorawjw1Egd6xvpVqBjAAovxNDMZX4GDkKbE0ipnSiuQ6paDZ2m4')

input('1...')
page1.locator('.modal__toggle-open icon icon-search').click()
page1.locator('Search-In-Modal').fill('table')

input('2...')
page1.goto('https://lumierecreation.com/collections/dinning-table')

input('3...')
browser.close()
p.stop()