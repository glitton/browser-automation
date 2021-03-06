from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/trial-of-the-stones")

# Find elements for Riddle of Stone
stone_locator = "r1Input"
stone_riddle_btn = "//button[@id='r1Btn']"
# Find elements for Riddle of Secrets
secrets_locator = "input[id='r2Input']"
secrets_riddle_btn = "//button[@id='r2Butn']"

# Assign elements for Riddle of Stone
riddle_stone_input = browser.find_element_by_id(stone_locator) # another way to find an element
answer_stone_riddle = browser.find_element_by_xpath(stone_riddle_btn)
# Assign elements for Riddle of Secrets
riddle_secrets_input = browser.find_element_by_css_selector(secrets_locator)
answer_secrets_riddle = browser.find_element_by_xpath(secrets_riddle_btn)

# Manipulate elements for Riddle of Stone
riddle_stone_input.send_keys("rock")
answer_stone_riddle.click()
#Assign password
password = browser.find_elements_by_xpath("//div[@id='passwordBanner']")[0].text

# Manipulate elements for Riddle of Secrets
riddle_secrets_input.send_keys(password)
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
#Find and assign input field and answer for richest merchant
merchant_input = browser.find_element_by_css_selector("input#r3Input") # another way to describe id
answer_merchant_btn = browser.find_element_by_xpath("//button[@id='r3Butn']")
#can also describe id using # so input#r3Input

#Find who is richer and enter name
if jessica_wealth > bernard_wealth:
    #enter name input field
    merchant_input.send_keys(jessica)
else:
    merchant_input.send_keys(bernard)

# click answer
answer_merchant_btn.click()

# Find check answer element and click the button
check_answers = browser.find_element_by_xpath("//button[@id='checkButn']")
check_answers.click()

# Get trial complete element
message = browser.find_element_by_css_selector("div#trialCompleteBanner > h4")
# check if Trial Complete text is found
assert message.text == "Trial Complete"

print("This is the password", password)
print("test complete")

# browser.quit()
