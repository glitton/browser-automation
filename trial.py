from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/trial-of-the-stones")

# Find elements for Riddle of Stone
stone_locator = "input[id='r1Input']"
stone_riddle_btn = "//button[@id='r1Btn']"
# Find elements for Riddle of Secrets
secrets_locator = "input[id='r2Input']"
secrets_riddle_btn = "//button[@id='r2Butn']"

# Assign elements for Riddle of Stone
riddle_stone_input = browser.find_element_by_css_selector(stone_locator)
answer_stone_riddle = browser.find_element_by_xpath(stone_riddle_btn)
# Assign elements for Riddle of Secrets
riddle_secrets_input = browser.find_element_by_css_selector(secrets_locator)
answer_secrets_riddle = browser.find_element_by_xpath(secrets_riddle_btn)

# Manipulate elements for Riddle of Stone
riddle_stone_input.send_keys("rock")
answer_stone_riddle.click()

# Manipulate elements for Riddle of Secrets
riddle_secrets_input.send_keys("bamboo")
answer_secrets_riddle.click()

# Find elements for the Two Merchants' names
find_jessica = "//b[text()='Jessica']"
find_bernard = "//b[text()='Bernard']"
# Find elements for the Two Merchants' wealth
find_jessica_wealth = "//b[text()='Jessica']/../../p"
find_bernard_wealth = "//b[text()='Bernard']/../../p"
# Assign elements for Two Merchants
jessica = browser.find_elements_by_xpath(find_jessica)[0].text
bernard = browser.find_elements_by_xpath(find_bernard)[0].text
jessica_wealth = browser.find_elements_by_xpath(find_jessica_wealth)[0].text
bernard_wealth = browser.find_elements_by_xpath(find_bernard_wealth)[0].text










# browser.quit()
