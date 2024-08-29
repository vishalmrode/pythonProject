from playwright.sync_api import  sync_playwright

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/')

    # CSS Selector usage
    # Id - ---  # (pound)
    # Class - ---.(dot)
    # attribute - -- tagname[attribute = "value"]
    page.locator('#email').click()
    page.locator('#email').fill('abc@abc.com')
    page.wait_for_timeout(3000)
    page.click('#enterimg')
    print('email-id entered and clicked on button')
    print(page.title())
    page.wait_for_timeout(3000)

